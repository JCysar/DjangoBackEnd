from .models import RecursosHumanos
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken


@csrf_exempt
# Create your views here.
def recursosHumanosCadastroView(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        funcionario = data.get('funcionario')
        cargo = data.get('cargo')
        salario =  data.get('salario')
        cargaHoraria = data.get('cargaHoraria')
        folhaPonto = data.get('folhaPonto')
        setor = data.get('setor')
       
        
        if RecursosHumanos.objects.filter(funcionario=funcionario).exists():
            return JsonResponse({'error': 'Produto já existe!'}, status=409)
        if not all([funcionario,cargo,salario,cargaHoraria,folhaPonto,setor]):
            return JsonResponse({'error': 'É necessario preencher todos os campos!'})
        else:
            rh = RecursosHumanos(funcionario=funcionario, cargo=cargo, salario=salario, cargaHoraria=cargaHoraria, folhaPonto=folhaPonto, setor=setor)
            rh.save()
            token = RefreshToken.for_user(rh)
            return JsonResponse({'status': 'Cadastro efetuado com sucesso!','token': str(token.access_token)})
    if request.method == 'GET':     
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        funcionario = data.get('funcionario')
        try:
            rh = RecursosHumanos.objects.get(funcionario=funcionario)
            return JsonResponse({
                "funcionario": rh.funcionario,
                "cargo": rh.cargo,
                "salario":  rh.salario,
                "cargaHoraria": rh.cargaHoraria,
                "folhaPonto": rh.folhaPonto,
                "setor": rh.setor
                                })
        except RecursosHumanos.DoesNotExist:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)
            
    if request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        funcionario = data.get('funcionario')
        newCargo = data.get('cargo')
        newSalario =  data.get('salario')
        newCargaHoraria = data.get('cargaHoraria')
        newFolhaPonto = data.get('folhaPonto')
        newSetor = data.get('setor')
        if not all([funcionario,newCargo,newSalario,newCargaHoraria,newFolhaPonto,newSetor]):
            return JsonResponse({'error': 'É necessario preencher todos os campos!'})
        try:
            rh = RecursosHumanos.objects.get(funcionario=funcionario)
            rh.cargo = newCargo
            rh.salario = newSalario
            rh.cargaHoraria = newCargaHoraria
            rh.folhaPonto = newFolhaPonto
            rh.setor = newSetor
            rh.save()
            
            return JsonResponse({'status': 'Atualizado com sucesso!'})
        except RecursosHumanos.DoesNotExist:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)
          
    if request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        funcionario = data.get('funcionario')
        if not funcionario:
            return JsonResponse({'error': 'É necessario preencher todos os campos!'})
        try:
            rh = RecursosHumanos.objects.get(funcionario=funcionario)
            rh.delete()
            return JsonResponse({'status': 'Deletado com sucesso!'})
        except RecursosHumanos.DoesNotExist:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)
    
    return JsonResponse({'error': 'Método inválido!'}, status=405)  
