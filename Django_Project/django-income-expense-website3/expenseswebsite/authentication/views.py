from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json


# Create your views here.
class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric charters'})
        return JsonResponse({'username_valid' : True})
        
        # if User.objects.filter(username=username).exists():
        #     return JsonResponse({'username_error':'username in use , choose another one'},status=409)

        

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

