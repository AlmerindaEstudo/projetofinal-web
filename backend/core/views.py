from rest_framework import viewsets
from .models import Fornecedor, ProdutoFornecedor, Produto,Cliente,Vendido
from .serializers import FornecedorSerializer, ProdutoFornecedorSerializer, ProdutoSerializer,ClienteSerializer
from django.db import models
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# ========================
# API (DRF)
# ========================

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer



@method_decorator(csrf_exempt, name='dispatch')
class ProdutoFornecedorViewSet(viewsets.ModelViewSet):
    queryset = ProdutoFornecedor.objects.all()
    serializer_class = ProdutoFornecedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

# ========================
# VIEWS HTML
# ========================
def home_view(request):
    return render(request, 'core/home.html')

def fornecedor_view(request):
    return render(request, 'core/fornecedor.html')

def comprar_view(request):  # 🔥 FALTAVA ISSO
    return render(request, 'core/comprarproduto.html')

def vender_view(request):
    return render(request, 'core/venderproduto.html')

def estoque_view(request):
    return render(request, 'core/estoque.html')



def listar_vendidos(request):
    vendas = list(
        Vendido.objects.values(
            'id',
            'quantidade',
            'data',
            cliente_nome=models.F('cliente__nome'),
            cliente_telefone=models.F('cliente__telefone'),
            produto_nome=models.F('produto__nome'),
            produto_preco=models.F('produto__preco')
        )
    )

    return JsonResponse(vendas, safe=False)
# ========================
# APIs CUSTOMIZADAS
# ========================

from django.views.decorators.csrf import csrf_exempt
from .models import Produto

@csrf_exempt
def comprar_produto(request):
    if request.method == "POST":
        data = json.loads(request.body)

        produto_fornecedor = ProdutoFornecedor.objects.get(id=data["produto_fornecedor"])
        quantidade = int(data["quantidade"])

        if produto_fornecedor.quantidade_disponivel < quantidade:
            return JsonResponse({"erro": "Estoque insuficiente"})

        # 🔥 DIMINUI FORNECEDOR
        produto_fornecedor.quantidade_disponivel -= quantidade
        produto_fornecedor.save()

        # 🔥 ADICIONA NO SEU ESTOQUE
        produto, criado = Produto.objects.get_or_create(
            nome=produto_fornecedor.nome_produto,
            defaults={"preco": produto_fornecedor.preco_compra}
        )

        produto.quantidade += quantidade
        produto.save()

        return JsonResponse({"status": "ok"})

def listar_produtos(request):
    produtos = list(
        ProdutoFornecedor.objects.values(
            'id',
            'nome_produto',
            'preco_compra',
            'quantidade_disponivel',
            nome_fornecedor=models.F('fornecedor__nome')  # 🔥 mais limpo
        )
    )
    return JsonResponse(produtos, safe=False)

# ================= VENDER =================

@csrf_exempt
def vender_produto(request):
    if request.method == "POST":
        data = json.loads(request.body)

        produto = Produto.objects.get(id=data["produto"])
        quantidade = int(data["quantidade"])

        if produto.quantidade < quantidade:
            return JsonResponse({"erro": "Estoque insuficiente"})

        # diminui estoque
        produto.quantidade -= quantidade
        produto.save()

        # cria cliente
        cliente = Cliente.objects.create(
            nome=data["nome_cliente"],
            telefone=data["telefone"]
        )

        # registra venda
        Vendido.objects.create(
            cliente=cliente,
            produto=produto,
            quantidade=quantidade
        )

        return JsonResponse({"status": "ok"})