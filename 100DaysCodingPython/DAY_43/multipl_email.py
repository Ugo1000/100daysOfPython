from smtp_email_sender import smtplib


# list of email_id to send the mail
li = ["uronaldo@live.com", "ugos9628@gmail.com"]

for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("samjava18@gmail.com", "domnicano1")
    message = "This Message Was Sent from Smtp_Multy Email Sender"
    s.sendmail("samjava18@gmail.com", dest, message)
    print('All done')
    s.quit()
