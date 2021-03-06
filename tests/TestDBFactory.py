# In-Python module
import unittest

#### Project Scripts ####
from DBFactory import DBFactory
from db.DBEnum import DBEnum
from db.IDB import IDB

class TestDBFactory(unittest.TestCase):

    def test1_getDB(self):

        print('\n**Start DBFactory getDB() test**\n')

        #### Invalid ####
        with self.assertRaises(TypeError):
            DBFactory.getDB(dBType=5)
            DBFactory.getDB(dBType='')
            DBFactory.getDB(dBType='Hello World!')
            DBFactory.getDB(dBType='MongoDB')


        #### Valid ####
        self.assertIsInstance(
            DBFactory.getDB(DBEnum.PostgreSQL),
            IDB
        )
        
        print('\n**End DBFactory getDB() test**\n')
