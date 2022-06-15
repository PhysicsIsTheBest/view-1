from pydoc import describe
import undetected_chromedriver as uc
from undetected_chromedriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
import configparser, multiprocessing, time

config = configparser.ConfigParser()
config.read("config.ini")

settings = {"streamer": config["default"]["streamer"]}
PATH = r'D:\chromedriver_win32\chromedriver.exe'

def SpawnBot(i, **args):
    options = webdriver.ChromeOptions()
    options.add_extension(r'C:\Users\Mehr\AppData\Local\Google\Chrome\User Data\Default\Extensions\mjnbclmflcpookeapghfhapeffmpodij\1.6.7_0.crx')
    time.sleep(5)
    
    driver = webdriver.Chrome(PATH, options=options)
    time.sleep(5)
    driver.get("http://ipinfo.io")
    driver.get('https://www.myexternalip.com/raw')
    time.sleep(10)
    driver.get("https://www.twitch.tv/rr11111111")


    while True:
        pass

if __name__ == "__main__":
    for i in range(20):
        process = multiprocessing.Process(target=SpawnBot, args=(i,))
        process.start()

