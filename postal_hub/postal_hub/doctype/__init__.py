import frappe
import requests
from instabot import Bot
from postal_hub.postal_hub import access_token

@frappe.whitelist()
def insta(caption,img,user,passw):
    bot = Bot()
    bot.api.login(username=user,password= passw)
    bot.upload_photo(caption=caption,photo=img)


@frappe.whitelist()
def facebook(caption):
    
    payload = {'post': caption, 
            'platforms': ['twitter', 'facebook', 'instagram', 'linkedin'],
            'media_urls': ['https://images.ayrshare.com/imgs/GhostBusters.jpg'],
            'unsplash': 'random' }
    headers = {'Content-Type': 'application/json', 
            'Authorization': 'Bearer 49GR8W3-C3145DB-JZ341GR-DF6WCMY'}

    r = requests.post('https://app.ayrshare.com/api/post', 
        json=payload, 
        headers=headers)
        
    print(r.json())
    print("completed")

    # response =  requests.post()


@frappe.whitelist()
def twitter(caption):
    response = requests.post()




