import os
from terralib.dataaccess import (DataSourceFactory, DataSource,
								DataSetTypeConverter, DataSetAdapter)
from terralib.core import URI, CharEncoding
from terralib import core
from terralib import dataaccess
from terralib import datatype
from terralib import geometry
from terralib_helper import PostGISURI, PostGISHelper

def test_read_shp(terralib_initialize):
	filepath = os.path.join(os.path.dirname(__file__), 'data', 'deter-amz-ccst.shp')
	conninfo = 'file://' + filepath
	uri = URI(conninfo)
	assert uri.isValid()
	assert uri.path() == filepath
	assert uri.uri() == conninfo
	ds = DataSourceFactory.make('OGR', uri)
	ds.open()
	assert ds.getNumberOfDataSets() == 1
	dsename = ds.getDataSetNames()[0] 
	assert dsename == 'deter-amz-ccst'
	encoding = ds.getEncoding()
	assert CharEncoding.getEncodingName(encoding) == 'UTF-8'
	dse = ds.getDataSet(dsename)
	assert dse.getNumProperties() == 18
	assert dse.getPropertyName(0) == 'FID'
	assert dse.getPropertyName(17) == 'OGR_GEOMETRY'
	assert dse.getPropertyDataType(0) == datatype.INT32_TYPE
	assert dse.getPropertyDataType(17) == datatype.GEOMETRY_TYPE
	dse.moveFirst()
	assert dse.getInt32(0) == 0
	assert dse.getGeometry(17).getGeometryType() == 'MultiPolygon'
	assert dse.getGeometry(17).getSRID() == 5880
	pointA = dse.getGeometry(17).getCentroid()
	assert pointA.x == 5043043.498324984
	assert pointA.y == 8838576.042765237
	dse.moveLast()
	assert dse.getInt32(0) == 633
	assert dse.getGeometry(17).getGeometryType() == 'MultiPolygon'	
	pointB = dse.getGeometry(17).getCentroid()
	assert pointB.x == 5292183.974363609
	assert pointB.y == 9343686.127080787
	dst = ds.getDataSetType(dsename)
	gp = dataaccess.GetFirstGeomProperty(dst)
	assert gp.getSRID() == 5880
	ds.close()


def test_postgis_export(terralib_initialize):
	shp_path = os.path.join(os.path.dirname(__file__), 'data', 'deter-amz-ccst.shp')
	shp_conninfo = 'file://' + shp_path
	shp_uri = URI(shp_conninfo)
	shp_ds = DataSourceFactory.make('OGR', shp_uri)
	shp_ds.open() 
	shp_ds.setEncoding(core.EncodingType_LATIN1)
	dsename = shp_ds.getDataSetNames()[0]	
	shp_dst = shp_ds.getDataSetType(dsename)
	shp_dse = shp_ds.getDataSet(dsename)
	pg_dse_name = 'deter_amz_ccst'
	shp_dst.setName(pg_dse_name)  # TODO: this shouldn't be necessary
	
	pg_uri = PostGISURI(user='postgres', password='postgres', database='postgis_export')
	PostGISHelper.create(pg_uri, True)
	pg_ds = DataSourceFactory.make('POSTGIS', pg_uri.to_connect())
	pg_ds.open()	

	converter = DataSetTypeConverter(shp_dst, pg_ds.getCapabilities())
	converter.setEncodingType(core.EncodingType_LATIN1)
	dst_result = converter.getResult()
	dse_adapter = dataaccess.CreateAdapter(shp_dse, converter)
	dse_adaptee = dse_adapter.getAdaptee()

	pg_ds.createDataSet(dst_result, {})
	pg_ds.add(pg_dse_name, dse_adaptee, {})

	assert pg_ds.getNumberOfDataSets() == 1
	assert f'public.{pg_dse_name}' == pg_ds.getDataSetNames()[0] 
	assert CharEncoding.getEncodingName(pg_ds.getEncoding()) == 'UTF-8'

	pg_dse = pg_ds.getDataSet(pg_dse_name)
	assert pg_dse.getNumProperties() == 18
	assert pg_dse.getPropertyName(0) == 'fid'
	assert pg_dse.getPropertyName(17) == 'ogr_geometry'
	assert pg_dse.getPropertyDataType(0) == datatype.INT32_TYPE
	assert pg_dse.getPropertyDataType(17) == datatype.GEOMETRY_TYPE
	pg_dse.moveFirst()
	assert pg_dse.getInt32(0) == 0
	assert pg_dse.getGeometry(17).getGeometryType() == 'MultiPolygon'
	assert pg_dse.getGeometry(17).getSRID() == 5880
	pointA = pg_dse.getGeometry(17).getCentroid()
	assert pointA.x == 5043043.498324984
	assert pointA.y == 8838576.042765237
	pg_dse.moveLast()
	assert pg_dse.getInt32(0) == 633
	assert pg_dse.getGeometry(17).getGeometryType() == 'MultiPolygon'	
	pointB = pg_dse.getGeometry(17).getCentroid()
	assert pointB.x == 5292183.974363609
	assert pointB.y == 9343686.127080787
	pg_dst = pg_ds.getDataSetType(pg_dse_name)
	gp = dataaccess.GetFirstGeomProperty(pg_dst)
	assert gp.getSRID() == 5880	

	pg_ds.dropDataSet(pg_dse_name)
	assert pg_ds.dataSetExists(pg_dse_name) is False
	pg_ds.close()
	assert not pg_ds.isOpened()

	PostGISHelper.drop(pg_uri)
	assert PostGISHelper.exists(pg_uri) is False
