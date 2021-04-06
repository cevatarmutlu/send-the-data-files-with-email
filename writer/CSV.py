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
        self.df.to_csv(f'{filename}.csv', index=False)

if __name__ == '__main__':
    CSV()\
        .setDF(pandas.DataFrame(['1', '2']))\
        .generate()