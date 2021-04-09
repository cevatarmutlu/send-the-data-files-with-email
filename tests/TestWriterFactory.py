# In-Python module
import unittest

#### Project Scripts ####
from WriterFactory import WriterFactory
from writer.FileTypeEnum import FileTypeEnum
from writer.IWriter import IWriter

class TestWriterFactory(unittest.TestCase):

    def test1_getDB(self):

        print('\n**Start WriterFactory getWriter() test**\n')

        #### Invalid ####
        with self.assertRaises(TypeError):
            WriterFactory.getWriter(fileType=5)
            WriterFactory.getWriter(fileType='')
            WriterFactory.getWriter(fileType='Hello World!')
            WriterFactory.getWriter(fileType='Word')


        #### Valid ####
        self.assertIsInstance(
            WriterFactory.getWriter(FileTypeEnum.Excel),
            IWriter
        )
        
        print('\n**End WriterFactory getWriter() test**\n')
