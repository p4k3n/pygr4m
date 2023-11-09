import re

with open('followers.txt', 'r', encoding='utf-8') as file:
    followers_data = file.read()
with open('following.txt', 'r', encoding='utf-8') as file:
    following_data = file.read()

formatted_followers = {'www.instagram.com/' + k for k in re.findall(r'href="/([^/]+?)/"', followers_data)}
formatted_following = {'www.instagram.com/' + k for k in re.findall(r'href="/([^/]+?)/"', following_data)}

not_following_back = formatted_following - formatted_followers

print("Users who don't follow you back:")
for idx, user in enumerate(not_following_back, start=1):
    print(f"{idx}) {user}\n")
