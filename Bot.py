from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Bot:
    id = 0
    def __init__(self):
        self.id = Bot.id+1
        Bot.id += 1



    def load_driver(self, url:str = None, headless: bool = False):
        """loads driver and opens url, default to cms url if not provided
        
        Keyword Arguments:
            url {str} -- url to be loaded (default: {None})
            headless {bool} -- set to True if you want to run in headless mode (default: {False})
        """
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\knaben\AppData\Local\chromedriver.exe",
            options=options,
            )
        if not url:
            url: str = "https://cms.obos.no/EPiServer/Cms/#context=epi.cms.contentdata:///5&viewsetting=viewlanguage:///no" 
        self.driver.get(url)

    def open_additem(self):
        """
        Navigates the menu and opens the add item page
        
        """

        meny=self.driver.find_element_by_class_name("epi-iconTree")
        meny.click()
        omdirigeringer = self.driver.find_element_by_id("uniqName_62_0_tablist_uniqName_2_12")
        omdirigeringer.click()
        obosfelt = self.driver.find_element_by_css_selector("#dijit_InlineEditBox_31")
        obosfelt.click()
        dropdown = self.driver.find_elements_by_css_selector("#uniqName_0_66 > div.dijitTreeRow.dijitTreeRowSelected > span > span.epi-extraIconsContainer > span.epi-extraIcon.dijitTreeIcon.epi-iconContextMenu")
        dropdown[0].click()
        additem = self.driver.find_element_by_css_selector("#uniqName_37_40_text")
        additem.click()

    def add_redirect(self, old: str, new: str):
        """adds redirects
        
        Arguments:
            old {str} -- old url
            new {str} -- new url
        """
        new_url = self.driver.find_element_by_css_selector("#dijit_form_ValidationTextBox_3")
        