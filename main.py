import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import random

from RedditFetch import RedditFetch
from WeatherFetch import WeatherFetch

while(True):
    fact_til = RedditFetch().hot_post('todayilearned', 3).replace('TIL that ', '').replace('TIL ', '').capitalize()
    if fact_til[-1] not in '.?!':
        fact_til = fact_til + '.'
        
    shower_thought = RedditFetch().hot_post('showerthoughts', 5).capitalize()
    if shower_thought[-1] not in '.?!' :
        shower_thought = shower_thought + '.'
        
    weather = WeatherFetch()
    
    greetings = open('greetings.txt', 'r')
    greeting = random.choice(greetings.readlines()).replace('\n', '').capitalize()
    
    farewells = open('farewells.txt', 'r')
    farewell = random.choice(farewells.readlines()).replace('\n', '').capitalize()
    
    signatures = open('signatures.txt', 'r')
    signature = random.choice(signatures.readlines()).replace('\n', '').capitalize()
    
    mail_content = "<html><body>" + greeting + \
                    "<p><b>Weather</b><br />" + "Current: " + \
                    str(weather.get_temp()[0]) + " F" +"<br /> High: " + \
                    str(weather.get_temp()[1]) + " F" + "<br /> Low: " + \
                    str(weather.get_temp()[2]) + " F" + "<br /> Status: " + \
                    weather.get_status() + "</p><p><b>Fact of the Day</b>" + \
                    "<br />" + fact_til + "</p><p><b>Shower Thought</b>" + "<br />" + \
                    shower_thought + "</p><p>" + farewell + "</p><p>" + signature + \
                    "<br />Dan</p></body></html>"
                    
    if ("08:08:0" in time.ctime(time.time())):
        #The mail addresses and password
        sender_address = 'dftm@wharton.upenn.edu'
        sender_pass = 'gijvgsckkxzoekhr'
        receiver_address = 'dftm@wharton.upenn.edu; niacrob@wharton.upenn.edu;' + \
                            'asharpe@wharton.upenn.edu; bsarti@wharton.upenn.edu' + \
                            'econniff@wharton.upenn.edu; jo.vallurupalli@gmail.com' + \
                            'jbhash65@gmail.com; dzm@wharton.upenn.edu'
        
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Good Morning, WAB!'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        
        print(mail_content)
        
        seconds = time.time()
        local_time = time.ctime(seconds)	
        
        print('Mail Sent @', local_time)
        time.sleep(10)

    '''
    content = "" + greeting + "\n\n<b>Weather</b>" + "\n Current: " + \
                    str(weather.get_temp()[0]) + " F" +"\n High: " + \
                    str(weather.get_temp()[1]) + " F" + "\n Low: " + \
                    str(weather.get_temp()[2]) + " F" + "\n Status: " + \
                    weather.get_status() + "\n\n<b>Fact of the Day</b>" + \
                    "\n" + fact_til + "\n\n<b>Shower Thought</b>" + "\n" + \
                    shower_thought + "\n\n" + farewell + "\n\n" + signature + \
                    "\nDan"
    '''
