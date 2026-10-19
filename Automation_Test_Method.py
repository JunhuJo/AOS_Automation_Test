from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import functools
common_delay = 3

def Try_Except(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            print("PASS")
            return result
        except Exception as log:
            self.driver.save_screenshot(f"{func.__name__}.png")
            print("FAIL", log)
            raise
    return wrapper

class AOS_Automation_Test:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @Try_Except
    def Login_Error(self):
        id_input = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/et_username")))
        id_input.clear()
        id_input.send_keys("tester1")

        pw_input = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/et_password")))
        pw_input.clear()
        pw_input.send_keys("test1234")

        comform = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/btn_login")))
        comform.click()

        error_check = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_login_error")))
        assert error_check.text == "아이디 또는 비밀번호가 올바르지 않습니다"

    @Try_Except
    def Login(self):
        id_input = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/et_username")))
        id_input.clear()
        id_input.send_keys("tester")

        pw_input = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/et_password")))
        pw_input.clear()
        pw_input.send_keys("test1234")

        remember = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/cb_remember")))
        remember.click()

        comform = self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/btn_login")))
        comform.click()

        check_text = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_welcome")))
        assert check_text.text == "tester님, 환영합니다!"

    @Try_Except
    def Logout(self):
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/btn_logout"))).click()
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))).click()
        logout_check = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_login_subtitle")))
        assert logout_check.text == "모험을 시작하려면 로그인하세요"

    @Try_Except
    def join_membership(self):
        #self.Login()
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/btn_menu_form"))).click()

        page_check = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_label_name")))
        assert page_check.text == "캐릭터 이름 *"

        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/btn_submit"))).click()
        name_error = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_form_error")))
        assert name_error.text == "캐릭터 이름을 입력하세요"
        
        name_input = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/et_name")))
        name_input.send_keys("test_user")

        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/btn_submit"))).click()
        email_error = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_form_error")))
        assert email_error.text == "올바른 이메일 형식이 아닙니다"

        mail_input = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/et_email")))
        mail_input.send_keys("test@mail.com")

        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/btn_submit"))).click()
        terms_error = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_form_error")))
        assert terms_error.text == "이용약관에 동의해야 합니다"

        self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/et_phone"))).send_keys("12345")
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/rb_male"))).click()
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/sp_class"))).click()
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("전사")'))).click()
    

        self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/sb_age"))).send_keys("30")
        age = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_age_value")))
        assert age.text == "나이: 30"

        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/sw_notification"))).click()
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/cb_terms"))).click()
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.qa.practiceapp:id/btn_submit"))).click()

        join_completion = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/alertTitle")))
        assert join_completion.text == "모험가 등록 완료"
        self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button1"))).click()

        check_text = self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, "com.qa.practiceapp:id/tv_welcome")))
        assert check_text.text == "tester님, 환영합니다!"

