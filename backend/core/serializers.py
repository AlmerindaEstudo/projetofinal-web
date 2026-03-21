from rest_framework import serializers
from .models import Fornecedor, ProdutoFornecedor, Produto,Cliente,Vendido

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class ProdutoFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoFornecedor
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VendidoSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)

    class Meta:
        model = Vendido
        fields = '__all__'