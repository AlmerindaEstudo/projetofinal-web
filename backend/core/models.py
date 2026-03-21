from django.db import models

# 🏢 FORNECEDOR
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


# 📦 PRODUTOS QUE O FORNECEDOR TEM
class ProdutoFornecedor(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    nome_produto = models.CharField(max_length=100)
    quantidade_disponivel = models.IntegerField()
    validade = models.DateField()
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    previsao_entrega = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_produto
    

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

# 📦 SEU ESTOQUE
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Vendido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)