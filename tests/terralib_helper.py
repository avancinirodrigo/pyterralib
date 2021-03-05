from terralib.dataaccess import DataSource

# class ExportHelper:
    
#     @staticmethod
#     def shp_to_postgis(shp_path, pg_info):


# class URIHelper:

#     @staticmethod
#     def create_postgis_uri(user, password, host='localhost',
#                             port=5432, database, encoding)

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