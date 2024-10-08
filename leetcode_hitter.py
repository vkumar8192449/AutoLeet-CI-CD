import requests
import os
import random
from sourceCode import sourceCode
from quesLink import quesLink

# Retrieve the CSRF token from environment variable
csrf_token = os.getenv("LEETCODE_CSRF_TOKEN")
cookie = os.getenv("LEETCODE_COOKIE")

ques = random.randint(0, 5)

print(quesLink[ques])

# Define the URL and the payload
url = quesLink[ques]
payload = {
    "lang": "cpp",
    "question_id": "1",
    "typed_code": sourceCode[ques]
}

# # Define the headers
headers = {
    "authority": "leetcode.com",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "content-type": "application/json",
    "origin": "https://leetcode.com",
    "referer": "https://leetcode.com/problems/two-sum/submissions/1402595395/",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36",
    "x-csrftoken": csrf_token,
    "cookie": cookie
}

# # Send the POST request
response = requests.post(url, json=payload, headers=headers)

# # Print response
print(response.status_code)
print(response.json())
