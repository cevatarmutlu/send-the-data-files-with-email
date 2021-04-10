#### Installed Modules ####
import pandas

#### Project Scripts ####
from DBFactory import DBFactory
from db.DBEnum import DBEnum
from mail.Mail import Mail
from mail.MailEnum import MailEnum
from WriterFactory import WriterFactory
from writer.FileTypeEnum import FileTypeEnum

if __name__ == "__main__":

    try:
        #### Assign this variables ####
        db_type = DBEnum.PostgreSQL
        data_query = ''

        # attach_file_name = ''
        attach_file_type = FileTypeEnum.Excel
        
        mail_service = MailEnum.Hotmail
        auth = {
            'user': '', 
            'password': ''
        }
        mailTo = ''
        mailSubject = ''
        mailMessage = ''
        

        #### Work Zone ####
        db = DBFactory.getDB(db_type)
        db.connect()
        df = db.fetch(data_query)
        db.disconnect()

        WriterFactory.getWriter(attach_file_type)\
            .setDF(df)\
            .generate(attach_file_name)

        Mail() \
                .setServise(MailEnum.Hotmail) \
                .setAuthentication(**auth) \
                .setTo(mailTo) \
                .setMessage(subject=mailSubject, message=mailMessage) \
                .attach(file_name=attach_file_name, file_type=attach_file_type) \
                .send()
    except TypeError as e:
        print('Error: ', e)
    except ValueError as e:
        print('Error: ', e)
    except pandas.io.sql.DatabaseError as e:
        print('Error: DB Query is not correct.')
    except ConnectionError as e:
        print(e)