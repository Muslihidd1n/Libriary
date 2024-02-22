from django.contrib import admin
from django.urls import path
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kitoblar/', hamma_kitoblar),
    path('talabalar/', hamma_studentlar),
    path('hamma_kutubxonachilar', hamma_kutubxonachilar),
    path('h_mualliflar/', hamma_mualliflar),
    path('hamma_recordlar/', hamma_recordlar),
    path('talaba_update/<int:pk>/', talaba_update ),
    path('kitob_update/<int:pk>/', kitob_update ),
    path('kutubxonachi_update/<int:pk>/', kutubxonachi_update),
    path('muallif_update/<int:pk>/', muallif_update),
    path('record_update/<int:pk>/', record_update),


    path('bitta_talaba/<int:pk>/', bitta_talaba),
    path('bitta_kitob/<int:pk>', bitta_kitob),



    path('talaba_ochir/<int:pk>', talaba_ochir),
    path('kitob_ochir/<int:pk>', kitob_ochir),
    path('muallif_ochir/<int:pk>', muallif_ochir),
    path('record_ochir/<int:pk>', record_ochir),

]
