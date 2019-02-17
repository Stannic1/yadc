import requests
import json
from django.http import HttpResponse

def postCode(code, language):
    getCode = code.get('code')
    print(getCode)
    print(language)

    r = requests.post('http://localhost:3000//submissions/?base64_encoded=false&wait=true', data = {
        "source_code": getCode,
        "language_id": language
    })
    print(r)
    print(r.text)
