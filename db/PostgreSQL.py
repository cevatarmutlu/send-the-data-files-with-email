#### Installed Modules ####
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2 as py

# Dependencies for installation psycopg2
# 1 pip install python-dev-tools
# 2 sudo apt-get install libpq-dev
# 3 pip install psycopg2

#### Project Scripts ####
from db.IDB import IDB

class PostgreSQL(IDB):
	"""
		This class connect to MySQL.
	"""

	def connect(self):
		"""
			Connect to MySQL. MySQL is built-in.

			Returns:
				None	
		"""

		try:
			self.conn = py.connect(
				host="localhost", 
				port=5432, 
				dbname="postgres", 
				user="postgres", 
				password="123"
			)
		except Exception as e:
			print(e)
			exit(1)
		
		print(f"{self.__class__.__name__} DB connection is successful")
	

	def fetch(self, query: str) -> pd.DataFrame:
		"""
			Fetch data from DB and convert to pandas DataFrame.

            Args:
                query: The SQL query that fetch the data.

            Returns:
                df (pandas.DataFrame): Constains the data.
			
			Raises:
				TypeError: if `query` is not instance of `str` then raises `TypeError`.
		"""

		if type(query) != str:
			raise TypeError("PostgreSQL Query argument must be string.")
		
		df = sqlio.read_sql_query(query, self.conn)
		print("Data Fetched successful")
		
		return df
	
	def disconnect(self):
		"""
            Disonnect to DB.

            Returns:
                None
        """

		try:
			self.conn.close()
		except Exception as e:
			print(e)
			exit(1)
		print(f"{self.__class__.__name__} DB connection is closed")

if __name__ == "__main__":
	postgre = PostgreSQL()
	postgre.connect()
	print(postgre.fetch("SELECT * FROM client"))
	postgre.disconnect()
