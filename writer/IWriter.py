# In-Python module
from abc import ABC, abstractmethod

#### Installed Modules ####
from pandas import DataFrame

class IWriter:
    """
        Abstract class of file types.
    """

    def setDF(self, df: DataFrame):
        """
            Sets the data that will write.

            Args:
                df: `DataFrame` object.
            
            Returns:
                self: The class instance.
            
            Raises:
                TypeError: if `df` is not instance of `pandas.DataFrame` raises `TypeError`.
        """

        if not isinstance(df, DataFrame):
            raise TypeError(f'df must be pandas.DataFrame, , not {type(filename).__name__}')
            

        self.df = df

        return self
    
    @abstractmethod
    def generate(self, filename: str):
        pass
