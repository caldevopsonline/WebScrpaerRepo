import string

import requests
from bs4 import BeautifulSoup
import argparse


# request_data = requests.get('https://www.bbc.co.uk/')
# generate_text = request_data.text
# sys_status = request_data.status_code
# print(generate_text,sys_status)


# Function to Request URL
def request_url():
    # Request User to enter a website Address

    web_view = argparse.ArgumentParser(description='A tutorial of argparse!')

    web_view.add_argument("--webdata",required=True,
                          type=str, help="my data url")

    web_url_pull = web_view.parse_args().webdata

    # Concatenate the web adDress with HTTPS://WWW.
    web_main = requests.get("https://www." + web_url_pull + "/")

    # Initialize fetch connection with the help of BeautifulSoup Library
    fetch_data = BeautifulSoup(web_main.content, 'html.parser')
    return fetch_data


# Function to capture body content of URL
def display_data():
    # Get BBC Main Body
    bbc_body = request_url().body.text
    return bbc_body


# Create a .TXT File
data_output = open("DATA_FROM_URL.txt", 'w')

# Push web content to the file created
data_output.write(display_data())

# Close the opened file
data_output.close()
