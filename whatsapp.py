from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = 'Peace 😌😌'

input('Enter anything after scanning QR code')

#to find user in lef side
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

#to find msg box 
msg_box = driver.find_element_by_class_name('_1Plpp')

#to find emoji 
#button1 = driver.find_element_by_class_name('hnQHL')
#button1.click()
#button2 = driver.find_element_by_class_name('_3B8vA')
#button1.send_keys("smile")
#button1.send_keys(Keys.ENTER)

msg = 'Go Corona, *Corona Go* '
msg_box.send_keys(msg)
for i in range(50):
    #to type
    msg_box.send_keys(msg)







    
    
    
    
    
    
    
    
    
    
    
    
    
    #to locate send button 
    button = driver.find_element_by_class_name('_35EW6')
    #to click on button
    button.click()