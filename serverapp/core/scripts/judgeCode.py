import requests
import json
from django.http import HttpResponse

def postCode(code, language):
    getCode = code.get('code')
    getstdin = code.get('input')
    print(getstdin)
    print(getCode)
    print(language)

    r = requests.post('http://localhost:3000//submissions/?base64_encoded=false&wait=true', data = {
        "source_code": getCode,
        "language_id": language,
        "stdin": getstdin
    })
    print(r)
    print(r.text)
    giveResults = r.json()

    return giveResults