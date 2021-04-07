# In-Python module
from abc import ABC, abstractmethod

#### Installed Modules ####
from pandas import DataFrame

class IWriter:
    """
        Interface of file types
    """

    def setDF(self, df: DataFrame):
        """
            Sets the data that will write.

            Args:
                df: DataFrame object to write.
            
            Returns:
                self: The class instance
        """

        if not isinstance(df, DataFrame):
            raise TypeError('df is not pandas.DataFrame')

        self.df = df

        return self
    
    @abstractmethod
    def generate(self, filename: str):
        """
            Generate the file.

            Args:
                filename: File name to be generated.

            Returns:
                None
        """
        
        pass
