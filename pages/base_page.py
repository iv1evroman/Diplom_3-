from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_main_page(self):
        return self.driver.get(data.MAIN_PAGE_URL)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def def_drag_and_drop_element_chrome(self, locator_from, locator_to):
        source_element = self.find_element_with_wait(locator_from)
        dest_element = self.find_element_with_wait(locator_to)
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()

    def drag_and_drop_element_firefox(self, locator_from, locator_to):
        self.find_element_with_wait(locator_from)
        self.find_element_with_wait(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                           var source = arguments[0];
                           var target = arguments[1];
                           var evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           source.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           target.dispatchEvent(evt);
                           evt = document.createEvent("DragEvent");
                           evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                           source.dispatchEvent(evt);
                       """, element_from, element_to)