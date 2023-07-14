import ssl
import smtplib
from email.message import EmailMessage
from string import ascii_uppercase
from random import choice


PASSWORD = "mjyxrtiakbxkvbet"
SENDER = "jeremikress@gmail.com"
PORT = 465
HOST = 'smtp.gmail.com'
CHARS = ascii_uppercase.replace('O', '') + ("123456789" * 2)

class Email:
    def __init__(self, receiver, name) -> None:
        self.receiver = receiver
        self.name = name
        self.em = EmailMessage()
        self.ssl_context = ssl.create_default_context()


    def construct_message(self, body, subject) -> None:
        self.em['From'] = SENDER
        self.em['To'] = self.receiver
        self.em['subject'] = subject
        self.em.set_content(body)

    def send_email(self) -> None:
        with smtplib.SMTP_SSL(HOST, PORT, context=self.ssl_context) as smtp:
            smtp.login(SENDER, PASSWORD)
            smtp.sendmail(SENDER, self.receiver, self.em.as_string())





    def send_otp(self, name) -> None:
        otp = ''.join(choice(CHARS) for _ in range(5))

        message = f'''
        Dear, {name}

        Please provide the officer with the following code to finalise the docket creation proccess 

        {otp}

        Kind Regards,
        South African Police Service
        '''


    def send_initial_info(self, docket_id) -> None:
        message = f'''
        Dear, {self.name}

        Your docket, with docket id {docket_id}, has been successfully stored. 

        SAPS uses blockchain technology to verify and validate this process.

        blah blah blah

        Kind Regards,
        South African Police Service
        '''

        self.construct_message(message, "Docket Creation Successful")
        self.send_email()

    def send_final_info(self) -> None:
        message = f'''


        Kind Regards,
        South African Police Service
        '''


# e = Email(
#     receiver="kgomari88@gmail.com",
#     name="Katlego Kgomari"
# )

# e.send_initial_info("123456789")