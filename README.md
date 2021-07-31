# :selfie: Instagram Engagement Data

This repository is an order from a freelance.

### Task
I have one instagram profile with 2 posts on it that I need to find out of each like if they follow the user or not. So for example if the profile has 100k followers and 50k likes on one of their posts, I need to find out how many of those 50k likes follow the profile. If you can write a script where I can easily swap profile usernames if I want to test another instagram profile for the same data extraction that would be great. Please write the script in python if possible. Expected output would be the script code and a csv file with a column for the username "@" of the "likes" on each post, a column with a 1/0 or a Yes/No if that username "@" that liked the post also follows the profile.

### Example
```python
from scraper import Scraper


__USERNAME = "username"     # Your `username` from Instagram account
__PASSWORD = "password"     # Your `password` from Instagram account
profile_name = "profile"    # Instagram profile that interests you, for example: 'endygamedev_' 

scraper = Scraper(__USERNAME, __PASSWORD)
scraper.authentication()
follower_list = scraper.get_followers_list(profile_name)

print(len(follower_list))
print(follower_list)
```

### License
Instagram Engagement Data is licensed under the [GNU General Public License v3.0](./LICENSE).