# In-Python module
import unittest

#### Installed Modules ####
import pandas

#### Project Scripts ####
from writer.Excel import Excel

class TestExcel(unittest.TestCase):
    excel = Excel()

    def test1_setDF(self):

        print('\n**Start IWriter setDF() test**\n')

        with self.assertRaises(TypeError):
            TestExcel.excel.setDF(df=5)
            TestExcel.excel.setDF(df='Merhaba')
            TestExcel.excel.setDF(df=[1, 2, 3])
        

        self.assertIsInstance(TestExcel.excel.setDF(df=pandas.DataFrame([1, 2, 3])), Excel)

        print('\n**End IWriter setDF() test**\n')
    
    def test2_generate(self):

        print('\n**Start IWriter generate() test**\n')

        #### Invalid ####
        with self.assertRaises(TypeError):
            TestExcel.excel.generate(filename=5)
            TestExcel.excel.generate(filename=[1, 2, 3, 4])
            TestExcel.excel.generate(filename=pandas.DataFrame([1, 2, 3]))

            TestExcel.excel.generate(sheet=5)
            TestExcel.excel.generate(sheet=[1, 2, 3, 4])
            TestExcel.excel.generate(sheet=pandas.DataFrame([1, 2, 3]))


        
        with self.assertRaises(ValueError):
            TestExcel.excel.generate(filename='')
            TestExcel.excel.generate(filename='/@^+%')
            TestExcel.excel.generate(filename='     ')
            
            TestExcel.excel.generate(sheet='')
            TestExcel.excel.generate(sheet='/@^+%')
            TestExcel.excel.generate(sheet='     ')


        #### Valid ####
        self.assertEqual(TestExcel.excel.generate(), None)
        self.assertEqual(TestExcel.excel.generate(filename='Deneme'), None)
        self.assertEqual(TestExcel.excel.generate(filename='Data1', sheet='Sheet1'), None)
        self.assertEqual(TestExcel.excel.generate(sheet='Sheet1'), None)

        self.assertEqual(TestExcel.excel.generate(filename='den1     '), None)
        self.assertEqual(TestExcel.excel.generate(sheet='     den2     '), None)
        
        print('\n**End IWriter generate() test**\n')
