# In-Python module
import unittest

#### Installed Modules ####
import pandas

#### Project Scripts ####
from mail.Mail import Mail
from mail.MailEnum import MailEnum
from writer.FileTypeEnum import FileTypeEnum

class TestMail(unittest.TestCase):
    mail = Mail()

    def test1_setService(self):

        print('\n**Start Mail setService() test**\n')

        with self.assertRaises(TypeError):
            TestMail.mail.setServise(service=5)
            TestMail.mail.setServise(service='')
            TestMail.mail.setServise(service=[1, 2, 3])
            TestMail.mail.setServise(service=pandas.DataFrame([1, 2, 3]))
            TestMail.mail.setServise(service='Merhaba dünya')

            TestMail.mail.setServise(service={'host': 'adsf', 'cort': 'ad'})
            TestMail.mail.setServise(service={'most': 'adsf', 'port': 'ad'})
            TestMail.mail.setServise(service={})
            TestMail.mail.setServise(service={'host': 'adsf', 'port': 'ad', 'cort': 'asdf'})

        self.assertIsInstance(TestMail.mail.setServise(MailEnum.Hotmail), Mail)

        print('\n**End Mail setService() test**\n')
    
    def test2_setAuthentication(self):

        print('\n**Start Mail setAuthentication() test**\n')

        with self.assertRaises(TypeError):
            TestMail.mail.setAuthentication(user=5, password=5)
            TestMail.mail.setAuthentication(user='aaa', password='bbb')
            TestMail.mail.setAuthentication(user='', password='mahmut')
        
        self.assertIsInstance(
            TestMail.mail.setAuthentication(user='', password=''), 
            Mail
        )

        print('\n**End Mail setAuthentication() test**\n')
    
    def test3_setTo(self):

        print('\n**Start Mail setTo() test**\n')

        with self.assertRaises(TypeError):
            TestMail.mail.setAuthentication(to=5)
            TestMail.mail.setAuthentication(to=[1, 2, 3])
            TestMail.mail.setAuthentication(to={'a': 1, 'b': 2})
            TestMail.mail.setAuthentication(to='')
        
        self.assertIsInstance(
            TestMail.mail.setTo(to=''),
            Mail
        )

        print('\n**End Mail setTo() test**\n')

    def test4_setMessage(self):

        print('\n**Start Mail setMessage() test**\n')

        with self.assertRaises(TypeError):
            TestMail.mail.setMessage(subject=5, message='')
            TestMail.mail.setMessage(subject='', message='')

        self.assertIsInstance(
            TestMail.mail.setMessage(subject='Konu', message=''),
            Mail
        )

        self.assertIsInstance(
            TestMail.mail.setMessage(subject='Konu', message='Merhaba'),
            Mail
        )

        print('\n**End Mail setMessage() test**\n')

    
    def test5_attach(self):

        print('\n**Start Mail attach() test**\n')

        with self.assertRaises(TypeError):
            TestMail.mail.attach(file_type='')
            TestMail.mail.attach(file_type=[1, 2, 3])
            TestMail.mail.attach(file_type=FileTypeEnum.Excel, file_name=5)
            TestMail.mail.attach(file_type=FileTypeEnum.Excel, file_name='')
            TestMail.mail.attach(file_type=FileTypeEnum.Excel, file_name='/')
            TestMail.mail.attach(file_type=FileTypeEnum.Excel, file_name=[1, 2, 3])
        
        self.assertIsInstance(
            TestMail.mail.attach(file_type=FileTypeEnum.Excel, file_name='Data'),
            Mail
        )

        print('\n**End Mail attach() test**\n')
    
    def test6_send(self):

        print('\n**Start Mail send() test**\n')

        self.assertEqual(TestMail.mail.send(), None)

        print('\n**End Mail send() test**\n')
        