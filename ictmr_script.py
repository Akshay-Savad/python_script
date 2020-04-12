from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://ictmr.mgmnavimumbai.com/MGM/')

driver.find_elements_by_name("loginid")[0].send_keys("EMP109")
driver.find_elements_by_name("password")[0].send_keys("1234567")
driver.find_elements_by_class_name("login_btn")[0].click()

driver.implicitly_wait(10)

driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[1]/td/table/tbody/tr/td[2]/a")[0].click()

driver.implicitly_wait(10)

driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[7]/td/form/table/tbody/tr/td[1]/table/tbody/tr[11]/td/b/font/a")[0].click()

driver.implicitly_wait(10)

driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[7]/td/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/font/a")[0].click()

height = 0

for x in range(12, 42):

    select_element = driver.find_element_by_id('standard')
    select_object = Select(select_element)

    std = select_object.select_by_visible_text('IX')

    select_element = driver.find_element_by_id('division')
    select_object = Select(select_element)

    std = select_object.select_by_visible_text('B SEMI ENGLISH')

    driver.find_element_by_css_selector("input[value='R']").click()

    driver.find_element_by_css_selector("input[name='search']").click()

    #number 10 link
    x_path = "/html/body/form/table/tbody/tr[7]/td/form/table[2]/tbody/tr["+str(x)+"]/td[6]/a"
    driver.find_elements_by_xpath(x_path)[0].click()

    height = driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[7]/td/form/center/table[1]/tbody/tr[5]/td[2]/input")[0].get_attribute("value")
    weight = driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[7]/td/form/center/table[1]/tbody/tr[5]/td[4]/input")[0].get_attribute("value")

    height = float(height) + float(2.00)
    #height = str(height)
    print("height = ",height)
    driver.implicitly_wait(10)
    height = str(height)

    weight = float(weight) + float(2.00)
    #weight = str(weight)
    print("weight = ",weight)
    driver.implicitly_wait(10)
    weight = str(weight)
    driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[7]/td/form/center/table[1]/tbody/tr[5]/td[4]/input")[0].send_keys(weight, Keys.TAB)

    driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[7]/td/form/center/table[1]/tbody/tr[5]/td[2]/input")[0].send_keys(height, Keys.TAB)


    driver.implicitly_wait(10)

    #condition = element_to_be_clickable(driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[7]/td/form/center/table[1]/tbody/tr[16]/td/input[1]"))
    #WebDriverWait(driver, timeout=3).until(str(condition))

    #submit button
    driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[7]/td/form/center/table[1]/tbody/tr[16]/td/input[1]")[0].click()