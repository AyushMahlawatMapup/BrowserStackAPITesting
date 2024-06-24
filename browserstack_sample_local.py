

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Options for the first test
options = UiAutomator2Options().load_capabilities({
    "platformName": "android",
    "platformVersion": "9.0",
    "deviceName": "Google Pixel 3",
    "app": "bs://8e8bbdef5f45bc070eba851590771abbc4de5fd4",
    'bstack:options': {
        "projectName": "First Python project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test",
        "userName": "YOUR_USERNAME",
        "accessKey": "YOUR_ACCESS_KEY"
    }
})

# Initialize the remote Webdriver using BrowserStack remote URL and options defined above
driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

# Test case for the BrowserStack sample Android app
search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()

search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")

time.sleep(5)

search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
assert len(search_results) > 0

driver.quit()

# Options for the second test
desired_cap = {
    "browserstack.user": "ayushmahlawat_LGJqU4",
    "browserstack.key": "M7udwuRGEtPWQqsB1b1H",
    "app": "bs://8e8bbdef5f45bc070eba851590771abbc4de5fd4",
    "device": "Xiaomi Redmi Note 8",
    "os_version": "9.0",
    "autoGrantPermissions": "true",
    "autoAcceptAlerts": "true",
    "project": "Test Python project", 
    "build": "BrowserStack-build-1",
    "name": "notes_app_test"
}

driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)

time.sleep(5)

el_createnote = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Tap to create a text note. Press and hold to create a voice note. Release the button to stop recording and create the note, or slide up to cancel.')
el_createnote.click()

el_notetitle = driver.find_element(AppiumBy.ID, 'com.miui.notes:id/note_title')
el_notetitle.click()
el_notetitle.send_keys("Watch Later")

el_note = driver.find_element(AppiumBy.ID, 'com.miui.notes:id/rich_editor')
el_note.click()
el_note.send_keys("Naruto\nWandaVision\nThe Little Mermaid")

back = driver.find_element(AppiumBy.ID, 'com.miui.notes:id/home')
back.click()

driver.quit()
