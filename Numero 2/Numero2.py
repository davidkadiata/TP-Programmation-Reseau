import smtplib


fromaddr = 'mongmail@gmail.com'  
toaddrs  = 'phd@gmail.com' 
msg = 'Bonjour Phd, c est David TSHIBANGU KADIATA  DE MASTER 1 UPL. juste le test'  

username = 'davidkadiata'  
password = 'MonPassWord'

server = smtplib.SMTP('smtp.gmail.com', 587)  
server.ehlo()
server.starttls()
server.login(username, password)  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()
