# In-Python module
import unittest

#### Installed Modules ####
import pandas

#### Project Scripts ####
from writer.CSV import CSV

class TestCSV(unittest.TestCase):
    csv = CSV()

    def test1_setDF(self):

        print('\n**Start IWriter setDF() test**\n')

        with self.assertRaises(TypeError):
            TestCSV.csv.setDF(df=5)
            TestCSV.csv.setDF(df='Merhaba')
            TestCSV.csv.setDF(df=[1, 2, 3])
        

        self.assertIsInstance(TestCSV.csv.setDF(df=pandas.DataFrame([1, 2, 3])), CSV)

        print('\n**End IWriter setDF() test**\n')
    
    def test2_generate(self):

        print('\n**Start IWriter generate() test**\n')

        #### Invalid ####
        with self.assertRaises(TypeError):
            
            TestCSV.csv.generate(filename=5)
            TestCSV.csv.generate(filename=[1, 2, 3, 4])
            TestCSV.csv.generate(filename=pandas.DataFrame([1, 2, 3]))

        with self.assertRaises(ValueError):
            TestCSV.csv.generate('')
            TestCSV.csv.generate(filename='/@^+%')
            TestCSV.csv.generate(filename='     ')


        #### Valid ####
        self.assertEqual(TestCSV.csv.generate(filename='Deneme'), None)
        self.assertEqual(TestCSV.csv.generate(), None)
        self.assertEqual(TestCSV.csv.generate(filename='den1     '), None)
        self.assertEqual(TestCSV.csv.generate(filename='     den2     '), None)
        self.assertEqual(TestCSV.csv.generate(filename='den3     '), None)

        print('\n**End IWriter generate() test**\n')
