# In-Python module
from abc import ABC, abstractmethod

#### Installed Modules ####
from pandas import DataFrame

class IWriter:
    """
        Interface of file types
    """

    @abstractmethod
    def setDF(self, df: DataFrame):
        """
            Sets the data that will write.

            Args:
                df: DataFrame object to write.
            
            Returns:
                self: The class instance
        """

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
