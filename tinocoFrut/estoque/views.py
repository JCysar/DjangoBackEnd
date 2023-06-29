from .models import Estoque
from produtos.models import Produto
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken


@csrf_exempt
def estoqueView(request):

    if request.method == 'POST':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        setor = data.get('setor')
        corredor = data.get('corredor')
        prateleira =  data.get('prateleira')
        produto = data.get('produto')
               
        if Estoque.objects.filter(produto=produto).exists() or not Produto.objects.filter(nome=produto).exists():
            return JsonResponse({'error': 'Estoque do produto já existe ou não existe produto cadastrado com esse nome!'}, status=409)
        elif not all([setor, corredor, prateleira, produto]):
            return JsonResponse({'error': 'É necessario preencher todos os campos!'}, status=400)
        else:
            estoque = Estoque(setor=setor, corredor=corredor, prateleira=prateleira, produto=produto)
            estoque.save()
            token = RefreshToken.for_user(estoque)
            return JsonResponse({'status': 'Cadastro efetuado com sucesso!','token': str(token.access_token)})
        
    if request.method == 'GET':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        produto = data.get('produto')
        if not produto:
            return JsonResponse({'error': 'É necessario preencher todos os campos!'}, status=400)
        try:
            estoque = Estoque.objects.get(produto=produto)
            
            response_data = {
                'produto': estoque.produto,
                'setor': estoque.setor,
                'corredor': estoque.corredor,
                'prateleira': estoque.prateleira,
            }
            return JsonResponse(response_data)
        except Estoque.DoesNotExist:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)
        
    if request.method == 'DELETE':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        produto = data.get("produto")
        if not produto:
            return JsonResponse({'error': 'É necessario preencher o campo'}, status=400)
        
        estoque = Estoque.objects.get(produto = produto)
        if not estoque:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)
        else:
            estoque.delete()           
            return JsonResponse({'status': 'Estoque deletado com sucesso!'}, status=200)
        
    if request.method == 'PUT':
        decode_json = request.body.decode('utf-8')
        data = json.loads(decode_json)
        newSetor = data.get('setor')
        newCorredor = data.get('corredor')
        newPrateleira =  data.get('prateleira')
        produto = data.get('produto')
        
        
        if not all([newSetor,newCorredor,newPrateleira,produto]):
            return JsonResponse({'error': 'É necessario preencher o campo'}, status=400)
        try: 
            estoque = Estoque.objects.get(produto = produto)
            estoque.setor = newSetor
            estoque.corredor = newCorredor
            estoque.prateleira = newPrateleira
            estoque.save()       
            return JsonResponse({'status': 'Estoque atualizado com sucesso!'}, status=200)
        except:
            return JsonResponse({'error': 'Produto não existe!'}, status=409)
       
        
        
    return JsonResponse({'error': 'Método inválido!'}, status=405)

    

 

    