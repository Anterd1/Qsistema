from django.urls import path
from core.erp.views import myfirstview, servicios, contacto, tableta, nosotros, casos

urlpatterns = [
    path('home/', myfirstview, name="home"),
    path('servicios/',servicios, name="servicios"),
    path('contacto/',contacto, name="contacto"),
    path('tableta/',tableta, name="tableta"),
    path('nosotros/',nosotros, name="nosotros"),
    path('casos/',casos, name="casos"),
]
