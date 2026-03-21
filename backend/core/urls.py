from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProdutoViewSet,
    FornecedorViewSet,
    ProdutoFornecedorViewSet,
    ClienteViewSet,
    listar_vendidos,
    fornecedor_view,
    estoque_view,
    comprar_view,
    home_view,
    vender_view,
    listar_produtos,
    vender_produto,
    comprar_produto
)

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'fornecedores', FornecedorViewSet)
router.register(r'produtos-fornecedor', ProdutoFornecedorViewSet)
router.register(r'clientes', ClienteViewSet)
urlpatterns = [
    # páginas
    path('', home_view, name='home'),
    path('fornecedor/', fornecedor_view, name='fornecedor'),
    path('estoque/', estoque_view, name='estoque'),  # 🔥 IMPORTANTE
    path('comprar/', comprar_view, name='comprar'),
    path('vender/', vender_view, name='vender'),
    path('api/vendidos/', listar_vendidos, name='vendidos'),
    # APIs personalizadas
    path('api/listar-produtos-fornecedor/', listar_produtos),
    path('api/comprar-produto/', comprar_produto),
    path('api/vender-produto/', vender_produto),

    # API automática (DRF)
    path('api/', include(router.urls)),
]

