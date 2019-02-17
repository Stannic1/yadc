<<<<<<< HEAD
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
=======
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
>>>>>>> 411d5fe5ad1d3d1fb234dbfe2d4b142ebe2e9656
