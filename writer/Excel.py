#### Installed Modules ####
import pandas

#### Project Scripts ####
from writer.IWriter import IWriter


class Excel(IWriter):
    """
        Excel file class. This class generates the Excel file for attaching a Excel file to the email.
    """

    def generate(self, filename: str = 'Data', sheet = 'Sheet1'):
        """
            Generate the Excel file.

            Args:
                filename: File name to be generated. Default: Data
                sheet: Sheet name to be generated. Default: Sheet1

            Returns:
                None
        """

        if type(filename) != str or type(filename) != str:
            raise TypeError(f'filename and sheet must be string not {type(filename).__name__}')
        
        filename = filename.strip()
        sheet = sheet.strip()

        if filename == '' or sheet == '':
            raise TypeError('filename and sheet is not empty.')
        if filename.find('/') != -1 or sheet.find('/') != -1:
            raise TypeError('filename is not include `/` character ')

        writer = pandas.ExcelWriter(f'{filename}.xlsx',options={'remove_timezone': True})
        self.df.to_excel(writer, sheet, index=False)
        writer.save()

if __name__ == '__main__':
    Excel()\
        .setDF(pandas.DataFrame(['1', '2']))\
        .generate()