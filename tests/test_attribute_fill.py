import os
from terralib.dataaccess import (DataSourceFactory, DataSourceManager,
								DataSource)
from terralib.maptools import DataSetLayer
from terralib.attributefill_core import VectorToVector
from terralib.core import CharEncoding
from terralib.geometry import GeometryProperty
from terralib import core
from terralib import dataaccess
from terralib import geometry
from terralib import attributefill_core
from terralib_helper import ShapeFileHelper, FileURI
from data import expected_shp_area


def test_shp_area_operation(terralib_initialize):
	filepath1 = os.path.join(os.path.dirname(__file__), 'data', 'deter-amz-ccst.shp')
	from_uri = FileURI(filepath1)
	filepath2 = os.path.join(os.path.dirname(__file__), 'data', 'csAmz_150km_epsg_5880.shp')
	to_uri = FileURI(filepath2)
	filepath3 = os.path.join(os.path.dirname(__file__), '', 'csAmz_150km_epsg_5880_area.shp')
	out_uri = FileURI(filepath3)

	ShapeFileHelper.delete_if_exists(out_uri)
	
	v2v = VectorToVector(from_uri.uri, to_uri.uri, out_uri.uri)
	v2v.execute('FID', attributefill_core.PERCENT_TOTAL_AREA)

	out_ds = DataSourceFactory.make('OGR', out_uri.uri)
	out_ds.open()
	dsename = out_ds.getDataSetNames()[0] 
	assert dsename == 'csAmz_150km_epsg_5880_area'
	encoding = out_ds.getEncoding()
	assert CharEncoding.getEncodingName(encoding) == 'UTF-8'
	
	expected = expected_shp_area.result()
	dse = out_ds.getDataSet(dsename)
	dse.moveBeforeFirst()
	while dse.moveNext():
		# print(f'\'{dse.getString(1)}\': {dse.getDouble(4)},')
		assert expected[dse.getString(1)] == dse.getDouble(4)

	ShapeFileHelper.delete(out_uri)

