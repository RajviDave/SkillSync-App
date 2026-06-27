import requests
import os

headers = {
    'apikey': os.getenv("MY_API_KEY"),
}

params = {
    'url': 'https://assets.apilayer.com/apis/codes/resume_parser/sample_resume.docx',
}

response = requests.get('https://api.apilayer.com/resume_parser/url', params=params, headers=headers)
print(params)