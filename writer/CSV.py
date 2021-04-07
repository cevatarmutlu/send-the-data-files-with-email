#### Installed Modules ####
import pandas

#### Project Scripts ####
from writer.IWriter import IWriter


class CSV(IWriter):
    """
        CSV file class. This class generates the CSV file for attaching a CSV file to the email.
    """

    def generate(self, filename: str = 'Data'):
        """
            Generate the CSV file.

            Args:
                filename: File name to be generated. Default: Data


            Returns:
                None
        """

        if type(filename) != str:
            raise TypeError(f'filename must be string not {type(filename).__name__}')
        
        filename = filename.strip()

        if filename == '':
            raise TypeError('filename is not empty.')
        if filename.find('/') != -1:
            raise TypeError('filename is not include `/` character ')

        self.df.to_csv(f'{filename}.csv', index=False)

if __name__ == '__main__':
    CSV()\
        .setDF(pandas.DataFrame(['1', '2']))\
        .generate()