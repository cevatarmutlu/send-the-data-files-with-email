# In-Python module
import unittest

#### Installed Modules ####
import pandas

#### Project Scripts ####
from writer.IWriter import IWriter

class TestIWriter(unittest.TestCase):
    iwriter = IWriter()

    def test1_setDF(self):

        print('\n**Start IWriter setDF() test**\n')

        #### Invalid ####
        with self.assertRaises(TypeError):
            TestIWriter.iwriter.setDF(df=5)
            TestIWriter.iwriter.setDF(df='Merhaba')
            TestIWriter.iwriter.setDF(df=[1, 2, 3])
        
        #### Valid ####
        self.assertIsInstance(TestIWriter.iwriter.setDF(df=pandas.DataFrame([1, 2, 3])), IWriter)

        print('\n**End IWriter setDF() test**\n')
