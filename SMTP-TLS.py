def sendmail(MailList):
    import smtplib, ssl
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "jici5565@gmail.com"
    password = "kolp9824"
    receiver_email = MailList
    message = """\
    Subject: SMTP Test

    This message is sent from jici.ca SMTP server using tls security."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        for receiver in receiver_email:
            server.sendmail(sender_email, receiver, message)

if __name__ == "__main__":
    receiverlist = ["jcdan960@gmail.com"]
    sendmail(receiverlist)