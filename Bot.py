from selenium import webdriver


def main():
    options = webdriver.ChromeOptions()
    #options.add_argument("headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\knaben\AppData\Local\chromedriver.exe",
        options=options,
        )  # options=options

    url: str = "https://cms.obos.no/EPiServer/Cms/#context=epi.cms.contentdata:///5&viewsetting=viewlanguage:///no" 

    meny=driver.find_element_by_class_name("epi-iconTree")
    meny.click()
    omdirigeringer = driver.find_element_by_id("uniqName_62_0_tablist_uniqName_2_12")
    omdirigeringer.click()
    obosfelt = driver.find_element_by_css_selector("#dijit_InlineEditBox_31")
    obosfelt.click()
    dropdown = driver.find_elements_by_css_selector("#uniqName_0_66 > div.dijitTreeRow.dijitTreeRowSelected > span > span.epi-extraIconsContainer > span.epi-extraIcon.dijitTreeIcon.epi-iconContextMenu")
    dropdown[0].click()
    additem = driver.find_element_by_css_selector("#uniqName_37_40_text")
    additem.click()