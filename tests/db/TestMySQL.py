# In-Python module
import unittest

#### Installed Modules ####
import pandas

#### Project Scripts ####
from db.MySQL import MySQL

class TestMySQL(unittest.TestCase):
    mysql = MySQL()

    def test1Connect(self):
        # Test DB Connection.
        print('\n**Start MySQL connect() test**\n')
        self.assertEqual(TestMySQL.mysql.connect(), None)
        print('\n**End MySQL connect() test**\n')


    def test2Fetch(self):

        print('\n**Start MySQL fetch() test**\n')    
        with self.assertRaises(TypeError):
            TestMySQL.mysql.fetch(query=5)
            TestMySQL.mysql.fetch(query=[1, 2, 3])
            TestMySQL.mysql.fetch(query=pandas.DataFrame([1, 2, 3]))
            TestMySQL.mysql.fetch(query='SELECT * FROM client')
        
        with self.assertRaises(pandas.io.sql.DatabaseError):
            TestMySQL.mysql.fetch(query='merhaba dunya')
            TestMySQL.mysql.fetch(query='SELECT * FROM client where order=5')

        self.assertEqual(type(TestMySQL.mysql.fetch(query='SELECT * FROM client')), type(pandas.DataFrame()))

        print('\n**End MySQL fetch() test**\n')   


    def test3Disconnect(self):
        # Test DB Connection.

        print('\n**Start MySQL disconnect() test**\n')  
        self.assertEqual(TestMySQL.mysql.disconnect(), None)
        print('\n**End MySQL disconnect() test**\n')  
