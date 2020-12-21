# This script should add 10 views to an object on ebay
import requests
import pyperclip

# If the user copied the link, then pyperclip can get it instead of the user having to input the link in the terminal
url = pyperclip.paste()

response = input("Is {} the correct link? [Y/N]: ".format(url))
response = response.lower()

if response == "y":

    for iterate in range(0, 10):
        r = requests.get(url)
        print("Adding...")

    print("A total of 10 views have been added!")

else:
    new_response = input("Please type link to item on ebay: ")

    for iterate in range(0, 10):
        r = requests.get(new_response)
        print("Adding...")

    print("A total of 10 views have been added!")
