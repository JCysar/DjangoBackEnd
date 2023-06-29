import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


@csrf_exempt
def cadastroUser(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)        
        login = data.get('login')
        password = data.get('password')
        if not all([login, password]):
            return JsonResponse({'error': 'É necessario preencher o login e a senha!'}, status=400)
        elif User.objects.filter(login=login).exists():
            return JsonResponse({'error': 'Usuario já existe!'}, status=409)
        else:
            user = User(login=login, password=password)
            user.save()
            token = RefreshToken.for_user(user)
            return JsonResponse({'status': 'Cadastro efetuado com sucesso!','token': str(token.access_token)}, status=200)
        
    if request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)        
        login = data.get('login')
        password = data.get('password')
        newPassword = data.get("newPassword")
        
        if not all([login,password,newPassword]):
            return JsonResponse({'error': 'É necessario preencher todos os campos!'}, status=400)
        try:
            user = User.objects.get(login=login,password=password)
            user.password = newPassword
            user.save()
            return JsonResponse({'status': 'Senha atualizado com sucesso!'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuario ou senha incorreta ou usuario não existe!'}, status=409)
            
        
    if request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)        
        login = data.get('login')
        password = data.get('password')
        if not all([login, password]):
            return JsonResponse({'error': 'É necessario preencher o login e a senha!'}, status=400)
        
        user = User.objects.filter(login=login, password=password)
        if not user:
            return JsonResponse({'error': 'Usuario ou senha incorreta ou usuario não existe!'}, status=409)
        else:
            user.delete()
            
            return JsonResponse({'status': 'Usuario deletado com sucesso!'}, status=200)
        
    return JsonResponse({'error': 'Método inválido!'}, status=405)    