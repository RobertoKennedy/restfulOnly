from django.contrib import admin
from django.urls import path, include
from core.views import LivroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'livros', LivroViewSet,base_name='MyBook')

urlpatterns = [
	path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
