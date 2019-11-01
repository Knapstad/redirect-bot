from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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
        self.driver.implicitly_wait(2)
        header=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body div nav header")))
        try:
            header.find_element_by_xpath("//span[contains(text(),'Edit')]").click()
        except Exception:
            try:
                header.find_element_by_xpath("//span[contains(text(),'Edit)]").click()
            except:
                pass
        meny = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#uniqName_116_0 > div > div.epi-toolbarLeading.epi-toolbarGroup > span:nth-child(1) > span.dijit.dijitReset.dijitInline.epi-leadingToggleButton.epi-mediumButton.dijitToggleButton")))
        try:
            meny: self.driver.find_elements_by_css_selector("#uniqName_116_0 > div > div.epi-toolbarLeading.epi-toolbarGroup > span:nth-child(1) > span.dijit.dijitReset.dijitInline.epi-leadingToggleButton.epi-mediumButton.dijitToggleButton")
        except Exception:
            pass
        meny.click()

        # extend_meny = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#uniqName_62_0_tablist_menuBtn > img")))
        # extend_meny.click()

        omdirigeringer = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#uniqName_62_0_tablist_uniqName_2_12")))
        self.driver.execute_script("arguments[0].scrollIntoView();", omdirigeringer)
        omdirigeringer.click()

        obosfelt =  WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.epi-hierarchicalList div.dijitLayoutContainer span.dijitTreeContent")))
        try:
            obosfelt= self.driver.find_elements_by_css_selector("div.epi-hierarchicalList div.dijitLayoutContainer span.dijitTreeContent")
            obosfelt[2].click()
        except Exception:
            try:
                obosfelt= self.driver.find_element_by_css_selector("div.epi-hierarchicalList div.dijitLayoutContainer span.dijitTreeContent")
                obosfelt[2].click()
            except Exception:
                pass

        dropdown =  WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"div.epi-hierarchicalList div.dijitLayoutContainer span.dijitTreeContent span.epi-extraIcon.epi-iconContextMenu")))
        dropdown.click() 

        additem =  WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#uniqName_37_40_text")))
        additem.click()

        

    def add_redirect(self, old: str, new: str):
        """adds redirects
        
        Arguments:
            old {str} -- old url
            new {str} -- new url
        """
        self.driver.implicitly_wait(3)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.dijitStackContainer.dijitContainer.dijitLayoutContainer"))
        )
        action = ActionChains(self.driver)
        action.send_keys(old)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ENTER)
        action.send_keys(Keys.TAB)
        action.send_keys(Keys.TAB)
        action.send_keys(new)
        action.perform()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Create')]").click()
        # old_url = self.driver.find_element_by_id("dijit_form_ValidationTextBox_6")
        # old_url.send_keys(old)
        # self.driver.find_element_by_css_selector("#uniqName_81_0").click()
        # self.driver.find_element_by_css_selector("#dijit_MenuItem_11_text").click()
        # new_url = self.driver.find_element_by_id("dijit_form_ValidationTextBox_7")
        # new_url.send_keys(new)

