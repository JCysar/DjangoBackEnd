from cadastro.models import User
from rest_framework_simplejwt.tokens import RefreshToken
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def loginRequest(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        login = data.get('login')
        password = data.get('password')

        user = User.objects.filter(login=login, password=password).first() 
        if user:    
            token = RefreshToken.for_user(user)
            return JsonResponse({'status':'logado', 'token': str(token.access_token)})  
        else:
            return JsonResponse({'error': 'Usuário ou senha incorreta!'}, status=400)
    
    return JsonResponse({'error': 'Método inválido!'}, status=405)  



    
    
  