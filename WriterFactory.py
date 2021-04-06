#### Project Scripts ####
from writer.FileTypeEnum import FileTypeEnum
from writer.IWriter import IWriter
from writer.Excel import Excel
from writer.CSV import CSV

class WriterFactory:

    @staticmethod
    def getWriter(fileType: str):
        if (fileType == FileTypeEnum.Excel):
            return Excel()
        elif (fileType == FileTypeEnum.CSV):
            return CSV()

