# In-Python module
from enum import Enum

class FileTypeEnum(Enum):
    """
        File types that can be attached to the email.
    """

    CSV = 'csv'
    Excel = 'xlsx'