import smtplib, ssl

email_address = 'ECE422SMTPTEST@gmail.com'
email_password = 'Ece422-001SmtpTEST123'

context = ssl.create_default_context() #Using Python recommended module to initiate TLS-encrypted connection

#Implicit TLS
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: #Creates secure connection from the start
    print("Logging in...")
    smtp.login(email_address, email_password) #Logging In
    
    receiver_email = input('Who do you want to email? ')
    subject = input('What is the subject? ')
    body = input('What is the body of your email? ')
    msg = f'Subject: {subject}\n\n{body}'

    confirmation = input("Send Email? y/n: ")
    loopconfirmation = 1
    while loopconfirmation == 1:
        if confirmation == 'y':
            print("Sending Email...")
            smtp.sendmail(email_address, receiver_email, msg) #format --- (sender, reciever, msg)
            print("Email Sent Successfully")
            loopconfirmation = 0
        elif confirmation == 'n':
            loopconfirmation = 0
        else:
            confirmation = input("Please input 'y' or 'n': ")
    print('Logging Out...')        
    smtp.quit() #Logs Out
