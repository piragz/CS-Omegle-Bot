from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time,os

def space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1
		
os.system('cls' if os.name == 'nt' else 'clear')
space(8);print "---------------------------------------------"
space(8);print "| CyberSucks Omegle Spam Bot                |"
space(8);print "| Coded by D@rk TruTH                       |"
space(8);print "| Version : 1.1                             |"
space(8);print "| CyberSucks.TK                             |"
space(8);print "| Twitter @darktruth190                     |"	
space(8);print "| Facebook: Fb.me/CyberSec007               |"
space(8);print "---------------------------------------------\n\n"


interest = raw_input("Enter the interests Example. friends,girls,fag, >> ")
msg1 = raw_input("Enter your first message (1/4) >> ")
msg2 = raw_input("Enter your second message (2/4) >> ")
msg3 = raw_input("Enter your third message (3/4) >> ")
msg4 = raw_input("Enter your fourth message (4/4) >> ")
p = raw_input("Enter y to use proxy >> ")
if p == "y":
	prox = raw_input("Enter proxy in format of ip:port >> ")
	display = Display(visible=1, size=(800, 600))
	display.start()
	PROXY = prox
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=socks5://' + PROXY)
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get('http://www.omegle.com')
	interest1 = driver.find_element_by_xpath('//input[@class="newtopicinput"]')
	interest1.send_keys(interest)
	btn = driver.find_element_by_id("textbtn")
	btn.click()
	def main():
		try:
			driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
			message = driver.find_element_by_xpath('//textarea[@rows="3"]')
			message.send_keys(msg1)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg2)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg3)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg4)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
		except InvalidElementStateException:
			main2()
		
		
	def main2():
		try:
			driver.get('http://www.omegle.com')
			interest1 = driver.find_element_by_xpath('//input[@class="newtopicinput"]')
			interest1.send_keys(interest)
			btn = driver.find_element_by_id("textbtn")
			btn.click()
			time.sleep(5)
			driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
			message = driver.find_element_by_xpath('//textarea[@rows="3"]')
			message.send_keys(msg1)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg2)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg3)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg4)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
		except InvalidElementStateException:
			main2()
	while True:
		time.sleep(8)
		try:
			main()
		except InvalidElementStateException:
			main2()
elif p == "n":
	display = Display(visible=1, size=(800, 600))
	display.start()
	driver = webdriver.Chrome()
	driver.get('http://www.omegle.com')
	interest1 = driver.find_element_by_xpath('//input[@class="newtopicinput"]')
	interest1.send_keys(interest)
	btn = driver.find_element_by_id("textbtn")
	btn.click()
	def main():
		try:
			driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
			message = driver.find_element_by_xpath('//textarea[@rows="3"]')
			message.send_keys(msg1)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg2)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg3)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg4)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
		except InvalidElementStateException:
			main2()
		
		
	def main2():
		try:
			driver.get('http://www.omegle.com')
			interest1 = driver.find_element_by_xpath('//input[@class="newtopicinput"]')
			interest1.send_keys(interest)
			btn = driver.find_element_by_id("textbtn")
			btn.click()
			time.sleep(5)
			driver.find_element_by_xpath('//textarea[@rows="3"]').clear()
			message = driver.find_element_by_xpath('//textarea[@rows="3"]')
			message.send_keys(msg1)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg2)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg3)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			message.send_keys(msg4)
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			send = driver.find_element_by_xpath('//button[@class="sendbtn"]')
			send.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
			disconnect = driver.find_element_by_xpath('//button[@class="disconnectbtn"]')
			disconnect.click()
		except InvalidElementStateException:
			main2()
	while True:
		time.sleep(8)
		try:
			main()
		except InvalidElementStateException:
			main2()
