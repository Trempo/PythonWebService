import json

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
from GPGDecrypt.logic import decryptUtil


@csrf_exempt
def decrypt_view(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        passphrase = body['passphrase']
        message = body['message']
        try:
            decrypted_message = decryptUtil.decrypt(message, passphrase)
        except ValueError as e:
            return HttpResponse(e)
        response = {
            "DecryptedMessage": decrypted_message.decode('utf-8')
        }
        return HttpResponse(json.dumps(response), 'application/json')
    else:
        return HttpResponse("Use POST method with JSON payload to decrypt", 'application/json')
