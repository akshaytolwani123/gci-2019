from selenium import webdriver
from time import  sleep

# Open codeforces contests in Chrome
browser = webdriver.Chrome()
browser.get('https://codeforces.com/contests')

#Click on the register now button in the attention tab via copy full xxpath in developer tools
contests = browser.find_element_by_xpath("/html/body/div[5]/div[4]/div[1]/div/div[4]/div[1]/a[2]")
contests.click()
sleep(10)

handle_or_email = browser.find_element_by_xpath('/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[1]/td[2]/input')
login1 = input('Please input your codeforces handle/email: ')
handle_or_email.send_keys(login1)

password = browser.find_element_by_xpath('/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[2]/td[2]/input')
login2 = input("Please input your codeforces password: ")
password.send_keys(login2)

submit = browser.find_element_by_xpath('/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[4]/td/div[1]/input')
submit.click()
sleep(10)
register = browser.find_element_by_xpath('/html/body/div[5]/div[4]/div[2]/form/table/tbody/tr[3]/td/div/input')
register.click()
