# In-Python module
from enum import Enum

class MailEnum(Enum):
    """This Enum contains STMP connection information (host and port) of Mail services."""

    Hotmail = {'host': 'smtp.live.com', 'port': 587}
