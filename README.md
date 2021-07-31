<h1><img alt="instagram-logo" src="./assets/logo.webp" width=30> Instagram Engagement Data</h1>

This repository is an order from a freelance.

### Task
I have one instagram profile with 2 posts on it that I need to find out of each like if they follow the user or not. So for example if the profile has 100k followers and 50k likes on one of their posts, I need to find out how many of those 50k likes follow the profile. If you can write a script where I can easily swap profile usernames if I want to test another instagram profile for the same data extraction that would be great. Please write the script in python if possible. Expected output would be the script code and a csv file with a column for the username "@" of the "likes" on each post, a column with a 1/0 or a Yes/No if that username "@" that liked the post also follows the profile.

### Documentation
`class Scraper(username: str, password: str)` — main class that takes all the information from Instagram

`def Scraper.authentication() -> None` — function with which you can log into Instagram

`def Scraper.get_follower_list(profile: str) -> List[str]` — function that creates a list of followers

`def Scraper.get_likes_list(post: str) -> List[str]` — function that creates a list of users who have liked the post

`def Scraper.end() -> None` — function that exits the `webdriver`

### Example
```python
from scraper import Scraper
from pprint import pprint


__USERNAME = "username"     # Your `username` from Instagram account
__PASSWORD = "password"     # Your `password` from Instagram account
profile_name = "profile"    # Instagram profile that interests you, for example: 'endygamedev_'
post_link = "post_url"      # Instagram post that insterest you, for example: 'https://www.instagram.com/p/CRmQr4yrBz0/'


scraper = Scraper(__USERNAME, __PASSWORD)
scraper.authentication()

follower_list = scraper.get_follower_list(profile_name)
pprint({len(follower_list): follower_list})

likes_list = scraper.get_likes_list(post_link)
pprint({len(likes_list): likes_list})

scraper.end()
```

### Dependencies
For the script to work correctly, you need to install [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Geckodriver](https://github.com/mozilla/geckodriver/releases) or you can use another browser, but for this you need to watch yourself how to connect `webdriver`.

### License
Instagram Engagement Data is licensed under the [GNU General Public License v3.0](./LICENSE).
