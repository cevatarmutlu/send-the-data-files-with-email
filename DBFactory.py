#### Project Scripts ####
from db.DBEnum import DBEnum
from db.IDB import IDB
from db.MySQL import MySQL
from db.PostgreSQL import PostgreSQL

class DBFactory:
    """
        Return specific database instance.

        Examples:
            DBFactory.getDB(DBEnum.MySQL)
    """

    @staticmethod
    def getDB(dbType: DBEnum):
        """
            Return specific database instance.

            Args:
                dbType: Database type.

            Returns:
                IDB subclass: Your DB instance.
            
            Raises:
                TypeError: if `dbType` is not instance of `DBEnum` raises `TypeError`.
            

                    
        """

        if not isinstance(dbType, DBEnum):
            raise TypeError('dbType must be DBEnum type.')
                

        if (dbType == DBEnum.PostgreSQL):
            return PostgreSQL()
        elif (dbType == DBEnum.MySQL):
            return MySQL()

