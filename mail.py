import smtplib


def mail(message):

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

    smtpObj.starttls()
    smtpObj.login('jmcducker@gmail.com', 'yzrmqrnxbzmbfapm')

    # smtpObj.sendmail('jmcducker@gmail.com', '11101419afbntu@gmail.com', message)
    # smtpObj.sendmail('jmcducker@gmail.com', 'fundog2001@gmail.com', message)
    smtpObj.sendmail('jmcducker@gmail.com', 'platongulik@gmail.com', message)

    smtpObj.quit()
