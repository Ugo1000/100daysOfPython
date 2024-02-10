import smtplib  # create an smtp server(it's a protocol : port @ 25)

from email.message import EmailMessage  # python built-in modules

email = EmailMessage()
# print(type(email))
email['from'] = 'Eng Ugo_Sammy'
email['to'] = 'ugo.samuel.java@gmail.com'
email['subject'] = 'Congratulation You Won $1,000,000 dollar'

email.set_content("I am Python Beginner!!")


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # The ehlo method (Extended Hello) is used to greet the server and establish a connection.
    smtp.ehlo()
    # TLS (Transport Layer Security) encrypted connection
    smtp.starttls()  # TLS (Transport Layer Security) encrypted connection
    # You need to replace this line with
    smtp.login("samjava18@gmail.com", "domnicano1")
    smtp.send_message(email)
    print("ALL IS GOOD")
