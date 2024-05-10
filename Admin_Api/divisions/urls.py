from django.urls import path 
from divisions import views

urlpatterns = [
path('d/',views.load_districts),
path('s/',views.load_subd),
path('b/',views.load_block),
path('listdistricts/',views.get_districts),
path('listsubdivs/<str:parent>',views.get_subdivs),
path('listblocks/<str:parent>',views.get_blocks),
path('generatespin/<str:parent>',views.generateSPINid)
]