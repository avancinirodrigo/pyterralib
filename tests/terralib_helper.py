import os 
import glob
from pathlib import Path
from terralib.dataaccess import DataSource

# class ExportHelper:
    
#     @staticmethod
#     def shp_to_postgis(shp_path, pg_info):


# class URIHelper:

#     @staticmethod
#     def create_postgis_uri(user, password, host='localhost',
#                             port=5432, database, encoding)


class FileURI:
	def __init__(self, filepath: str):
		self._filepath = filepath
		self._uri = 'file://' + filepath
	
	@property
	def uri(self) -> str:
		return self._uri

	@property
	def path(self) -> str:
		return self._filepath


class ShapeFileHelper:
	@staticmethod
	def delete(uri: FileURI):
		path = uri.path.replace('.shp', '.')
		for file in glob.glob(f'{path}*'):
			os.remove(file)

	@staticmethod 
	def delete_if_exists(uri: FileURI):
		if Path(uri.path).is_file():
			ShapeFileHelper.delete(uri)


class PostGISURI:
	def __init__(self, user, password, database, 
				encoding='ISO-8859-1', host='localhost', port=5432):
		self.user = user
		self.password = password
		self.database = database
		self.encoding = encoding
		self.host = host
		self.port = port
		self.base = f'pgsql://{user}:{password}@{host}:{port}'
		self.query = ('&PG_CLIENT_ENCODING=' + encoding
					+ '&PG_CONNECT_TIMEOUT=10'
					+ '&PG_MAX_POOL_SIZE=4'
					+ '&PG_MIN_POOL_SIZE=2'
					+ '&PG_HIDE_SPATIAL_METADATA_TABLES=FALSE'
					+ '&PG_HIDE_RASTER_TABLES=FALSE'
					+ '&PG_CHECK_DB_EXISTENCE=' + database)

	def to_create(self):
		return (self.base + '/?'
				+ '&PG_NEWDB_NAME=' + self.database
				+ '&PG_NEWDB_OWNER=' + self.user
				+ '&PG_NEWDB_ENCODING=' + self.encoding
				+ '&PG_DB_TO_DROP=' + self.database
				+ self.query)

	def to_connect(self):
		return f'{self.base}/{self.database}?{self.query}'

	def to_drop(self):
		# TODO: ERROR: it cannot drop the currently open database	
		return f'{self.base}/postgres?{self.query}&PG_DB_TO_DROP={self.database}'

class PostGISHelper:
	@staticmethod
	def create(uri: PostGISURI, overwrite=False):
		conn_info = uri.to_create()
		if overwrite:
			if DataSource.exists('POSTGIS', conn_info):
				DataSource.drop('POSTGIS', conn_info)
		DataSource.create('POSTGIS', conn_info)                    

	@staticmethod 
	def drop(uri: PostGISURI):
		conn_info = uri.to_drop()
		DataSource.drop('POSTGIS', conn_info)

	@staticmethod
	def exists(uri: PostGISURI):
		conn_info = uri.to_create()
		return DataSource.exists('POSTGIS', conn_info)

	@staticmethod
	def import_from_shp(filepath):
		# shp_path = os.path.join(os.path.dirname(__file__), 'data', 'deter-amz-ccst.shp')
		# shp_conninfo = 'file://' + shp_path
		shp_uri = FileURI(filepath)
		# shp_uri = URI(shp_conninfo)
		shp_ds = DataSourceFactory.make('OGR', shp_uri.uri)
		shp_ds.open() 
		# shp_ds.setEncoding(core.EncodingType_LATIN1)
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