
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    # path('cats/', views.cats, name='cats'),
    # path('manuf/', views.manuf, name='manuf'),
    # path('itemm/', views.itemm, name='itemm'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('delivery/', views.delivery, name='delivery'),
    path('catalog/', views.catalog, name='catalog'),
    path('checkout/', views.checkout, name='checkout'),
    path('manufacturers/', views.manufacturers, name='manufacturers'),
    path('manufacturers/<manufactor_slug>', views.manufactor, name='manufactor'),
    path('category/<category_slug>/', views.category, name='category'),
    path('category/<category_slug>/<subcategory_slug>/', views.subcategory, name='subcategory'),
    path('category/<category_slug>/<item_slug>', views.item_page, name='item_page'),
    path('category/<category_slug>/<subcategory_slug>/<item_slug>', views.item_page, name='item_page'),
    path('search/', views.search, name='search'),
    path('sale/', views.sale, name='sale'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('partner/', views.partner, name='partner'),

    path('posts/', views.allPosts, name='allposts'),
    path('posts/<slug>/', views.showPost, name='showpost'),
    path('send_cb', views.send_cb, name='send_cb'),
    path('order/<order_code>', views.order, name='order'),
    # path('subcategory/<subcat_slug>/', views.subcategory, name='subcategory'),
    path('robots.txt', views.robots, name='robots'),
    path('index.html', RedirectView.as_view(url='/', permanent=True), name='index1'),
    path('index.php', RedirectView.as_view(url='/', permanent=True), name='index2'),


]
