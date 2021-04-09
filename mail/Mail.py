# In-Python module
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from os import remove
import re

#### Project Scripts ####
from mail.MailEnum import MailEnum
from writer.FileTypeEnum import FileTypeEnum

class Mail:
    """Sends e-mail."""

    def setServise(self, service: MailEnum):
        """
            The mail service used by the person who will send the mail.

            Args:
                service: Mail service. Example: `MailEnum.Gmail`.

            Returns: 
                self: Created instance of the class.
            
            Raises:
                TypeError: if `service` is not instance of `MailEnum` 
                then raises `TypeError`.
        """

        if not isinstance(service, MailEnum):
            raise TypeError('service argument must be MailEnum.')

        self.service = smtplib.SMTP(**service.value)
        self.service.ehlo()
        self.service.starttls()

        return self
    
    def setAuthentication(self, user: str, password: str):
        """
            Mail account information(email address and password) of the person who will send mail.

            Args:
                user: Email address.
                password: Password.

            Returns:
                self: Created instance of the class.
            
            Raises:
                TypeError: if `user` and `password` is not instance of `MailEnum` 
                    then raises `TypeError`.
                ValueError: if user is not email then raises ValueError.
        """

        valid_mail_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if not isinstance(user, str) or not isinstance(password, str):
            raise TypeError('user and password must be string')
        if not (re.search(valid_mail_regex, user)):
            raise ValueError('user is not mail.')

        self.service.login(user=user, password=password)
        self.from_ = user

        return self
    
    def setTo(self, to: str):
        """
            The email of the person who will receive email.
        
            Args:
                to: Email address.
            
            Returns:
                self: Created instance of the class.
            
            Raises:
                TypeError: if `to` is not instance of `str` 
                    then raises `TypeError`.
                ValueError: if to is empty then raises ValueError.
        """

        if not isinstance(to, str):
            raise TypeError('to must be str.')
        
        to = to.strip()

        if to == '':
            raise ValueError('to must not be empty.')
        

        self.to = to

        return self
    
    def setMessage(self, subject: str, message: str):
        """
            The message to send.

            Args:
                subject: The subject of email.
                message: The message of email. Must be empty.
            
            Returns:
                self: Created instance of the class.
            
            Raises:
                TypeError: if `subject` and `message` is not instance of `str` 
                    then raises `TypeError`.
                ValueError: if subject is empty then raises ValueError.
        """

        if not isinstance(subject, str) or not isinstance(message, str):
            raise TypeError('subject and message must be string.')
        
        subject = subject.strip()
        message = message.strip()

        if subject == '':
            raise ValueError('subject must not be empty')

        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = subject
        self.msg['From'] = self.from_
        self.msg['To'] = self.to

        self.msg.attach(MIMEText(message, 'plain'))

        return self
    
    def attach(self, file_type: FileTypeEnum, file_name: str = 'Data'):
        """T
            he file that attach to email.

            Args:
                file: The file name.
                tyoe: The type of the file
            
            Returns:
                self: Created instance of the class.
            
            Raises:
                TypeError: if `file_type` is not instance of `FileTypeEnum` or
                    `file_name` is not instance of `str` then raises `TypeError`.
                ValueError: if `file_name` is empty and include '/' 
                    then raises ValueError.
        """

        if not isinstance(file_type, FileTypeEnum):
            raise TypeError('file_type must be FileTypeEnum.')
        
        if not isinstance(file_name, str):
            raise TypeError('file_name must be string.')

        file_name = file_name.strip()

        if file_name == '':
            raise ValueError('file_name must not be empty.')
        
        if file_name.find('/') != -1:
            raise ValueError('file_name is not constains /')

        self.file_path = f'{file_name}.{file_type.value}'
        self.part = MIMEBase('application', "octet-stream")
        self.part.set_payload(open(f"{self.file_path}", "rb").read())
        encoders.encode_base64(self.part)
        self.part.add_header('Content-Disposition', 'attachment; filename="' + f'{self.file_path}"')
        self.msg.attach(self.part)

        return self
    
    def send(self):
        """
            Send the mail.
        
            Returns:
                None
        """

        self.service.sendmail(self.from_, self.to, self.msg.as_string())
        self.service.quit()
        remove(self.file_path)
        print("Email sending is successful.")
