#### Project Scripts ####
from writer.FileTypeEnum import FileTypeEnum
from writer.IWriter import IWriter
from writer.Excel import Excel
from writer.CSV import CSV

class WriterFactory:

    @staticmethod
    def getWriter(fileType: str):
        """
            Static function. Return specific FileType instance.

            Args:
                fileType: File type.

            Returns:
                FileType instance:
                    if (fileType == FileTypeEnum.Excel):
                        return Excel()
                    elif (fileType == FileTypeEnum.CSV):
                        return CSV()
        """

        if not isinstance(fileType, FileTypeEnum):
            raise TypeError('fileType must be FileTypeEnum.')
                
        if fileType not in FileTypeEnum:
            raise TypeError('fileType must be in FileTypeEnum')

        if (fileType == FileTypeEnum.Excel):
            return Excel()
        elif (fileType == FileTypeEnum.CSV):
            return CSV()

