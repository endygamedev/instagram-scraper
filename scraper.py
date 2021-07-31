# Importing modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Constants and variables
__USERNAME = "username"     # Your `username` from Instagram account
__PASSWORD = "password"     # Your `password` from Instagram account
profile_name = "profile"    # Instagram profile that interests you, for example: 'endygamedev_'


class Scraper:
    def __init__(self, username: str, password: str) -> None:
        """
            **Description:** Class for collecting information from Instagram

            :param username: Instagram `username` for authentication
            :type username: str
            :param password: Instagram `password` for authentication
            :type password: str
            :return: Creates a `webdriver` and initializes variables
            :returns: None
        """
        self.driver = webdriver.Firefox()

        self._username = username
        self._password = password

        self.__TIME_SLEEP_AUTH = 5
        self.__TIME_SLEEP_FOLLOWERS = 3

    def authentication(self) -> None:
        """
            **Description:** Instagram authentication function

            :returns: None
        """
        self.driver.get("https://www.instagram.com")
        time.sleep(self.__TIME_SLEEP_AUTH)

        # Typing `username` in authentication system
        action = self.driver.find_element_by_name("username")
        action.clear()
        action.send_keys(self._username)

        # Typing `password` in authentication system
        action = self.driver.find_element_by_name("password")
        action.clear()
        action.send_keys(self._password)

        # Press button to `Sign in`
        action.send_keys(Keys.RETURN)
        time.sleep(self.__TIME_SLEEP_AUTH)

    def get_follower_list(self, profile: str) -> list:
        """
            **Description:** Takes the `user's nickname` and gives a list of usernames that are followed to this user

            :param profile: username on instagram
            :type profile: str
            :return: List of instagram profile followers - `profile`
            :rtype: list
        """
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://www.instagram.com/" + profile)
        time.sleep(self.__TIME_SLEEP_FOLLOWERS)

        # Get the number of followers
        followers_count = int(
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text)

        # Click on the `followers button`
        followers_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='followers']")))
        followers_button.click()
        time.sleep(self.__TIME_SLEEP_FOLLOWERS)
        dialogue_box = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div[role='presentation'] > div > div > div.isgrP")))

        # Scroll the list of followers
        for _ in range(0, followers_count // 6 + 1):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                                       dialogue_box)
            time.sleep(self.__TIME_SLEEP_FOLLOWERS)

        # Get the followers list
        html_list = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
        followers = [html_list.find_element_by_xpath(f"//li[{i}]/div/div[1]/div[2]/div/span/a").get_attribute('title')
                     for i in range(1, followers_count + 1)]
        self.driver.close()  # TODO: Remove this when the list of likes is created
        return followers


scraper = Scraper(__USERNAME, __PASSWORD)
scraper.authentication()
follower_list = scraper.get_follower_list(profile_name)
print(len(follower_list))
print(follower_list)
