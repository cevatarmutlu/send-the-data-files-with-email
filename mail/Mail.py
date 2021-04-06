# In-Python module
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from os import remove

#### Project Scripts ####
from mail.MailEnum import MailEnum
from writer.FileTypeEnum import FileTypeEnum

class Mail:
    """Sends e-mail."""

    def setServise(self, service: dict):
        """
            The mail service used by the person who will send the mail.

            Args:
                service: Mail service. Example: `MailEnum.Gmail`.

            Returns: 
                self: Created instance of the class.
        """

        self.service = smtplib.SMTP(**service)
        self.service.ehlo()
        self.service.starttls()

        return self
    
    def setAuthentication(self, user: str, password: str):
        """Mail account information(email address and password) of the person who will send mail.

        Args:
            user: Email address.
            password: Password.

        Returns:
            self: Created instance of the class.
        """

        self.service.login(user=user, password=password)
        self.from_ = user

        return self
    
    def setTo(self, to: str):
        """The email of the person who will receive email.
        
        Args:
            to: Email address.
        
        Returns:
            self: Created instance of the class.
        """

        self.to = to

        return self
    
    def setMessage(self, subject: str, message: str):
        """The message to send.

        Args:
            subject: The subject of email.
            message: The message of email.
        
        Returns:
            self: Created instance of the class.
        """

        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = subject
        self.msg['From'] = self.from_
        self.msg['To'] = self.to

        self.msg.attach(MIMEText(message, 'plain'))

        return self
    
    def attach(self, file_type: FileTypeEnum, file_name: str = 'Data'):
        """The file that attach to email.

        Args:
            file: The file name.
            tyoe: The type of the file
        
        Returns:
            self: Created instance of the class.
        """
        self.file_path = f'{file_name}.{file_type.value}'
        self.part = MIMEBase('application', "octet-stream")
        self.part.set_payload(open(f"{self.file_path}", "rb").read())
        encoders.encode_base64(self.part)
        self.part.add_header('Content-Disposition', 'attachment; filename="' + f'{self.file_path}"')
        self.msg.attach(self.part)

        return self
    
    def send(self):
        """Send the mail.
        
        Returns:
            None

        """

        self.service.sendmail(self.from_, self.to, self.msg.as_string())
        self.service.quit()
        remove(self.file_path)
        print("Email sending is successful.")
