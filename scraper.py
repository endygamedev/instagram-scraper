# Importing modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
from typing import List
import time

# Constants and variables
__USERNAME = "username"         # Your `username` from Instagram account
__PASSWORD = "password"         # Your `password` from Instagram account
profile_name = "profile_name"   # Instagram profile that interests you, for example: 'endygamedev_'
post_link = "post_url"          # Instagram post that insterest you, for example: 'https://www.instagram.com/p/CRmQr4yrBz0/'


class Scraper:
    def __init__(self, username: str, password: str) -> None:
        """
            **Description:** Class for collecting information from Instagram

            :param username: Instagram `username` for authentication
            :type username: str
            :param password: Instagram `password` for authentication
            :type password: str
            :returns: Creates a `webdriver` and initializes variables
            :rtype: None
        """
        self._driver = webdriver.Firefox()
        self._start = time.time()

        self._username = username
        self._password = password

        self.__TIME_SLEEP = 3
        self.__TIME_SLEEP_AUTH = 5

    def authentication(self) -> None:
        """
            **Description:** Instagram authentication function

            :returns: None
            :rtype: None
        """
        self._driver.get("https://www.instagram.com")
        time.sleep(self.__TIME_SLEEP_AUTH)

        # Typing `username` in authentication system
        action = self._driver.find_element_by_name("username")
        action.clear()
        action.send_keys(self._username)

        # Typing `password` in authentication system
        action = self._driver.find_element_by_name("password")
        action.clear()
        action.send_keys(self._password)

        # Press button to `Sign in`
        action.send_keys(Keys.RETURN)
        time.sleep(self.__TIME_SLEEP_AUTH)

    def get_follower_list(self, profile: str) -> List[str]:
        """
            **Description:** Takes the `user's nickname` and gives a list of usernames that are followed to this user

            :param profile: username on instagram
            :type profile: str
            :returns: List of instagram profile followers - `profile`
            :rtype: List[str]
        """
        wait = WebDriverWait(self._driver, 10)
        self._driver.get("https://www.instagram.com/" + profile)
        time.sleep(self.__TIME_SLEEP)

        # Get the number of followers
        followers_count = int(
            self._driver.find_element_by_xpath(
                '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text)

        # Click on the `followers button`
        followers_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='followers']")))
        followers_button.click()
        time.sleep(self.__TIME_SLEEP)
        dialogue_box = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div[role='presentation'] > div > div > div.isgrP")))

        # Scroll the list of followers
        for _ in range(0, followers_count // 6):
            self._driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                                        dialogue_box)
            time.sleep(self.__TIME_SLEEP)

        # Get the followers list
        html_list = self._driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
        elements_count = len(html_list.find_elements_by_xpath("./div/*"))
        followers = [html_list.find_element_by_xpath(f"//div/li[{i}]/div/div[1]/div[2]/div/span/a").get_attribute('title')
                     for i in range(1, elements_count + 1)]
        return followers

    def get_likes_list(self, post: str) -> List[str]:
        """
            **Description:** Takes the `URL of the post` and gives a list of usernames that are liked this post

            :param post: URL to the Instagram post that interests you
            :type post: str
            :return: List of instagram usernames who liked the `post`
            :rtype: List[str]
        """
        wait = WebDriverWait(self._driver, 10)
        self._driver.get(post)
        time.sleep(self.__TIME_SLEEP)

        # Get the number of likes
        likes_count = int(
            self._driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/a/span").text)

        # Click on the `likes button`
        likes_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='liked_by']")))
        likes_button.click()
        time.sleep(self.__TIME_SLEEP)
        dialogue_box = self._driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div")

        # Get the likes list
        likes = []
        for _ in range(0, likes_count // 6):
            html_list = self._driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div")
            elements_count = len(html_list.find_elements_by_xpath("./*"))
            for i in range(1, elements_count + 1):
                text = html_list.find_element_by_xpath(f"//div[{i}]/div[2]/div[1]/div/span/a").get_attribute('title')
                likes.append(text)
            self._driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;",
                                        dialogue_box)
            time.sleep(self.__TIME_SLEEP)
        return list(set(likes))

    def end(self) -> None:
        """
            **Description:** Ends the `webdriver` session

            :returns: None
            :rtype: None
        """
        self._driver.close()
        print("\n" + "-".center(100, "-"))
        print("Scraper finished work!".center(100, " "))
        print(f"Program worked {time.time() - self._start} seconds".center(100, " "))
        print("-".center(100, "-"))


if __name__ == "__main__":
    scraper = Scraper(__USERNAME, __PASSWORD)
    scraper.authentication()

    likes_list = scraper.get_likes_list(post_link)
    pprint({len(likes_list): likes_list})

    follower_list = scraper.get_follower_list(profile_name)
    pprint({len(follower_list): follower_list})

    scraper.end()
