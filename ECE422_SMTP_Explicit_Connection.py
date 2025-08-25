import smtplib

email_address = ''
email_password = ''

#Explicit TLS
with smtplib.SMTP('smtp.gmail.com', 587) as smtp: #Creates unsecure connection
    smtp.ehlo() #Identifies ourselves with the mail server (Called in background when first setting up, just a fail safe)
    print('Encrypting traffic using .starttls()')
    smtp.starttls() #Encrypts traffic using ssl/tls
    print('Identifying ourselves with mail server as an encrypted connection')
    smtp.ehlo() #Re-identifies as an encrypted connection

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

