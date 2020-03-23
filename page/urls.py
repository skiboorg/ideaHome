
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('manufacturers/', views.manufacturers, name='manufacturers'),
    path('manufacturers/<slug>/', views.manufacturers_cat, name='manufacturers_cat'),
    path('category/<category_slug>/', views.category, name='category'),
    path('category/<category_slug>/<subcategory_slug>/', views.subcategory, name='subcategory'),
    path('category/<category_slug>/<item_slug>', views.item_page, name='item_page'),
    path('category/<category_slug>/<subcategory_slug>/<item_slug>', views.item_page, name='item_page'),

    # path('subcategory/<subcat_slug>/', views.subcategory, name='subcategory'),


]
