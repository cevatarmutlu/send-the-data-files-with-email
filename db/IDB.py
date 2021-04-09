#### Installed Modules ####
import pandas as pd

# In-Python module
from abc import ABC, abstractmethod

class IDB(ABC):
    """
        Abstract class for Database classes.
    """
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def fetch(self, query: str):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass