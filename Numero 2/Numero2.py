import smtplib


fromaddr = 'davidkadiata@gmail.com'  
toaddrs  = 'jusksp@gmail.com' 
msg = 'Bonjour Phd, c est David TSHIBANGU KADIATA  DE MASTER 1 UPL. juste le test'  

username = 'davidkadiata'  
password = 'Jolibor@1990'

server = smtplib.SMTP('smtp.gmail.com', 587)  
server.ehlo()
server.starttls()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()