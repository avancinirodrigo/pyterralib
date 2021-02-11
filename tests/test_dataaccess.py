import os
from terralib.dataaccess import DataSourceFactory
from terralib.core import URI
from terralib import datatype
from terralib import geometry


def test_read_shp(terralib_initialize):
	filepath = os.path.join(os.path.dirname(__file__), 'data', 'es-protected_areas_sirgas2000_5880.shp')
	conninfo = 'file://' + filepath
	uri = URI(conninfo)
	assert uri.isValid()
	assert uri.path() == filepath
	assert uri.uri() == conninfo
	ds = DataSourceFactory.make('OGR', uri)
	ds.open()
	assert ds.getNumberOfDataSets() == 1
	dsename = ds.getDataSetNames()[0] 
	assert dsename == 'es-protected_areas_sirgas2000_5880'
	dse = ds.getDataSet(dsename)
	assert dse.getNumProperties() == 18
	assert dse.getPropertyName(0) == 'FID'
	assert dse.getPropertyName(17) == 'OGR_GEOMETRY'
	assert dse.getPropertyDataType(0) == datatype.INT32_TYPE
	assert dse.getPropertyDataType(17) == datatype.GEOMETRY_TYPE
	dse.moveFirst()
	assert dse.getInt32(0) == 0
	assert dse.getGeometry(17).getGeometryType() == 'MultiPolygon'
	pointA = dse.getGeometry(17).getCentroid()
	assert pointA.x == 6361726.323583894
	assert pointA.y == 7727417.2463137
	dse.moveLast()
	assert dse.getInt32(0) == 89
	assert dse.getGeometry(17).getGeometryType() == 'MultiPolygon'	
	pointB = dse.getGeometry(17).getCentroid()
	assert pointB.x == 6499487.664695099
	assert pointB.y == 7921585.813169297
