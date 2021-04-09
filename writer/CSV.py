#### Installed Modules ####
import pandas

#### Project Scripts ####
from writer.IWriter import IWriter


class CSV(IWriter):
    """
        This class generates the CSV file to attaching to the email.
    """

    def generate(self, filename: str = 'Data'):
        """
            Generate the CSV file.

            Args:
                filename: File name to be generated. Default: Data

            Returns:
                None
            
            Raises:
                TypeError: if `filename` is not instance of `str` raises `TypeError`.
                ValueError: if filename is empty and include '/' then raises ValueError.
        """

        if type(filename) != str:
            raise TypeError(f'filename must be string, not {type(filename).__name__}')
        
        filename = filename.strip()

        if filename == '':
            raise ValueError('filename must not empty')

        if filename.find('/') != -1:
            raise ValueError('filename must not include `/` character.')

        self.df.to_csv(f'{filename}.csv', index=False)

if __name__ == '__main__':
    CSV()\
        .setDF(pandas.DataFrame(['1', '2']))\
        .generate()