#### Project Scripts ####
from writer.FileTypeEnum import FileTypeEnum
from writer.IWriter import IWriter
from writer.Excel import Excel
from writer.CSV import CSV

class WriterFactory:
    """
        Return specific FileType instance.

        Examples:
            WriterFactory.getWriter(FileTypeEnum.Excel)
    """

    @staticmethod
    def getWriter(fileType: str):
        """
            Return specific FileType instance.

            Args:
                fileType: File type.

            Returns:
                IWriter subclass: Your FileType instance.
            
            Raises:
                TypeError: if `fileType` is not instance of `FileTypeEnum` raises `TypeError`.

        """

        if not isinstance(fileType, FileTypeEnum):
            raise TypeError('fileType must be FileTypeEnum.')
                

        if (fileType == FileTypeEnum.Excel):
            return Excel()
        elif (fileType == FileTypeEnum.CSV):
            return CSV()
