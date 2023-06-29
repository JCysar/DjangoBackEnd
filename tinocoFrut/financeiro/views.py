from .models import Financeiro
from estoque.models import Estoque
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.core import serializers


@csrf_exempt
def financeiroCadastroView(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        comprar = data.get('comprar')
        vender = data.get('vender')
        fiscal =  data.get('fiscal')
        relatorioCompra = data.get('relatorioCompra')
        relatorioVenda = data.get('relatorioVenda')
        
        if not all([comprar, vender, fiscal, relatorioCompra, relatorioVenda]):
            return JsonResponse({'error': 'É necessario preencher todos os campos!'}, status=400)        
            
        financeiro = Financeiro(comprar=comprar, vender=vender, fiscal=fiscal, relatorioCompra=relatorioCompra, relatorioVenda=relatorioVenda)
        financeiro.save()
        
        token = RefreshToken.for_user(financeiro)
        
        return JsonResponse({'status': 'Cadastro efetuado com sucesso!','token': str(token.access_token)})
        
    if request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        id = data.get('id')
        newComprar = data.get('comprar')
        newVender = data.get('vender')
        newFiscal =  data.get('fiscal')
        newRelatorioCompra = data.get('relatorioCompra')
        newRelatorioVenda = data.get('relatorioVenda')
        
        if not id:
            return JsonResponse({'error': 'É necessario preencher todos os campos!'}, status=400)
        try:
            financeiro = Financeiro.objects.get(id=id)
            financeiro.comprar = newComprar
            financeiro.vender = newVender
            financeiro.fiscal = newFiscal
            financeiro.relatorioCompra = newRelatorioCompra
            financeiro.relatorioVenda = newRelatorioVenda
        except Financeiro.DoesNotExist:
            return JsonResponse({'error': 'Id não existe!'}, status=409)  
            
    if request.method == 'GET':
        financeiros = Financeiro.objects.all().values()
        return JsonResponse(list(financeiros), safe=False)
    
    if request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        fiscal = data.get('fiscal')
        if not fiscal:
            return JsonResponse({'error': 'É necessario preencher todos os campos!'}, status=400)
        try:
            financeiro = Financeiro.objects.get(fiscal=fiscal)
            financeiro.delete()
            return JsonResponse({'status': 'Delete efetuado com sucesso!'}, status = 200)
        except Financeiro.DoesNotExist:
            return JsonResponse({'error': 'Id não existe!'}, status=409)
          
    return JsonResponse({'error': 'Método inválido!'}, status=405)  
