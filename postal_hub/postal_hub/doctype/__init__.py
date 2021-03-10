import frappe
import requests
from instabot import Bot
from postal_hub.postal_hub import access_token

@frappe.whitelist()
def insta(caption):
    btot = Bot()
    btot.login()
    btot.upload_photo()
    btot.login()


@frappe.whitelist()
def facebook(caption):
    response =  requests.post()


@frappe.whitelist()
def twitter(caption):
    response = requests.post()




