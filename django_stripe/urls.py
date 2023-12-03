from django.contrib import admin
from django.urls import path

from app.views import index, stripe_config, create_checkout_session

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>/', create_checkout_session, name='buy'),
    path('item/<int:item_id>', index, name='index'),
    path('config/', stripe_config, name='config'),
]
