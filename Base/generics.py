from selenium.webdriver.common.by import By
from time import sleep
from traceback import print_stack
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import *
class Generics:
    def __init__(self,driver):
        self.driver=driver

    # logging.basicConfig(filename='testlog3', level=logging.INFO,
    #                     format="%(asctime)s: %(levelname)s: %(message)s")

    def getByType(self,locatortype):
        locator=locatortype.lower()
        if locator=='id':
            return By.ID
        elif locator=='name':
            return By.NAME
        elif locator=='class_name':
            return By.CLASS_NAME
        elif locator=='xpath':
            return By.XPATH
        else:
            print(('locator ',locatortype,' is not found'))
        return False

    def getElement(self,locatortype,locatorvalue):
        try:
            bytype=self.getByType(locatortype)
            element=self.driver.find_element(bytype,locatorvalue)
            print(('element with locator type ',locatortype,' and locator value ',
                  locatorvalue,'is found'))
        except:
            print(('element with locator type ', locatortype, ' and locator value ',
                  locatorvalue, 'is not found'))
        return element

    def sendData(self,locatortype,locatorvalue,data):
        try:
            getelement=self.getElement(locatortype,locatorvalue)
            getelement.send_keys(data)
            print(('data ',data,' sent to the element with locator type ',
                  locatortype,' with locator value ',locatorvalue))
        except:
            print(('data ', data, ' is not sent to the element with locator type ',
                  locatortype, ' with locator value ',locatorvalue))

    def ClickOn(self,locatortype,locatorvalue):
        try:
            getelement=self.getElement(locatortype,locatorvalue)
            sleep(10)
            getelement.click()

            print(('clicked on a element with locator type ',locatortype,' and locator value ',
                  locatorvalue))
        except:
            print(('cannot click on a element with locator type ', locatortype,
                  ' and locator value ', locatorvalue))