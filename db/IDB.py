#### Installed Modules ####
import pandas as pd

# In-Python module
from abc import ABC, abstractmethod

class IDB(ABC):
    """
        Interface for Database classes.
    """
    
    @abstractmethod
    def connect(self):
        """
            Connect to DB.

            Returns:
                None
        """

        pass
    
    @abstractmethod
    def fetch(self, query: str):
        """
            Fetch data from DB and convert to pandas DataFrame.

            Args:
                query: The SQL query that fetch the data.

            Returns:
                DataFrame: Constains the data.
        """
        
        pass
    
    @abstractmethod
    def disconnect(self):
        """
            Disonnect to DB.

            Returns:
                None
        """

        pass