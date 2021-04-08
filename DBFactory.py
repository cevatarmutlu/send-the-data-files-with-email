#### Project Scripts ####
from db.DBEnum import DBEnum
from db.IDB import IDB
from db.MySQL import MySQL
from db.PostgreSQL import PostgreSQL

class DBFactory:
    """
        Return specific database instance.
    """

    @staticmethod
    def getDB(dBType: str):
        """
            Static function. Return specific database instance.

            Args:
                dBType: Database type.

            Returns:
                Db instance:
                    if (dBType == DBEnum.PostgreSQL):
                        return PostgreSQL()
                    elif (dBType == DBEnum.MySQL):
                        return MySQL()
        """

        if not isinstance(dBType, DBEnum):
            raise TypeError('dbType must be DBEnum.')
                
        if dBType not in DBEnum:
            raise TypeError('dbType must be in DBEnum')

        if (dBType == DBEnum.PostgreSQL):
            return PostgreSQL()
        elif (dBType == DBEnum.MySQL):
            return MySQL()

