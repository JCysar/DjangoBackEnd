from .models import Produto
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.core import serializers

@csrf_exempt
# Create your views here.
def produtoCadastroView(request):
    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        quantidadeEstoque = data.get('quantidadeEstoque')
        descricao = data.get('descricao')
        nome =  data.get('nome')
        preco = data.get('preco')
        categoria = data.get('categoria')
        tipo = data.get('tipo')
       
        
        if not all([quantidadeEstoque,nome,preco,categoria,tipo]):
            return JsonResponse({'error': 'É necessario preencher todos os campos!'}, status=400)
        elif Produto.objects.filter(nome=nome).exists():
            return JsonResponse({'error': 'Produto já existe!'}, status=409)
        else:
            produto = Produto(quantidadeEstoque=quantidadeEstoque, descricao=descricao, nome=nome, preco=preco, categoria=categoria, tipo=tipo)
            produto.save()
            token = RefreshToken.for_user(produto)
            return JsonResponse({'status': 'Cadastro efetuado com sucesso!','token': str(token.access_token)})
        
    if request.method == 'GET':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        nome = data.get('nome')
        if not nome:
            return JsonResponse({'error': 'É necessario preencher todos os campos!'}, status=400)
        try:
            produto = Produto.objects.get(nome=nome)
            return JsonResponse(
            {
                'name': produto.nome,
                'preco': produto.preco,
                'quantidadeEstoque': produto.quantidadeEstoque,
                'descricao': produto.descricao,
                'categoria': produto.categoria,
                'tipo': produto.tipo                
            })
        except Produto.DoesNotExist:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)  
    
            
    if request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        newQuantidadeEstoque = data.get('quantidadeEstoque')
        newDescricao = data.get('descricao')
        nome =  data.get('nome')
        newPreco = data.get('preco')
        newCategoria = data.get('categoria')
        newTipo = data.get('tipo')
        
        if not all([newQuantidadeEstoque,nome,newPreco,newCategoria,newTipo, newDescricao]):
            return JsonResponse({'error': 'É necessario preencher os campos!'}, status=400)
        try:
            produto = Produto.objects.get(nome=nome)
            produto.quantidadeEstoque = newQuantidadeEstoque
            produto.descricao = newDescricao
            produto.preco = newPreco
            produto.categoria = newCategoria
            produto.tipo = newTipo
            produto.save()
            return JsonResponse({'status': 'Atualizado com sucesso!'}, status=200 )
        except Produto.DoesNotExist:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)  
        
        
    if request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        nome = data.get("nome")
        if not nome:
            return JsonResponse({'error': 'É necessario preencher o campo'}, status=400)
        
        produto = Produto.objects.filter(nome=nome)
        if not produto:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)
        else:
            produto.delete()           
            return JsonResponse({'status': 'produto deletado com sucesso!'}, status=200)
    return JsonResponse({'error': 'Método inválido!'}, status=405)  