from django.shortcuts import render, get_object_or_404
from item.models import *
from blog.models import *
#from openpyxl import load_workbook
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from order.models import *
from cart.models import Cart
from django.http import Http404
import settings

def order(request, order_code):
    try:
        order = Order.objects.get(order_code=order_code)
    except:
        order=None

    if order:
        return render(request, 'page/order_complete.html', locals())
    else:
        raise Http404

def send_cb(request):
    print(request.POST)
    if not request.POST.get('agree') and not request.POST.get('comment') and len(request.POST.get('name')) > 3 and len(request.POST.get('phone')) == 18:
        msg_html = render_to_string('email/test.html', {'name': request.POST.get('name'),
                                                        'phone': request.POST.get('phone')}
                                    )

        send_mail('Форма обратного звонка', None, 'info@ideahome74.ru', (settings.MAIL_TO,),
                  fail_silently=False, html_message=msg_html)
        messages.add_message(request, messages.INFO, 'Hello world.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def index(request):
    all_categories = Category.objects.filter(is_active=True, is_in_index_catalog=True)
    banners = Banner.objects.filter(at_home_page=True, is_active=True)
    banners2 = Banner.objects.filter(at_home_page2=True, is_active=True)
    banners3 = Banner.objects.filter(at_home_page3=True, is_active=True)
    all_manufacturers = Manufactor.objects.all()
    return render(request, 'page/index.html', locals())

def allPosts(request):
    postactive = 'active'
    canonical_url = 'posts/'
    pageTitle = ''
    pageDescription = ''
    pageKeywords = ''
    allPost = BlogPost.objects.filter(is_active=True)
    return render(request, 'page/posts.html', locals())

def showPost(request,slug):
    canonical_url = request.get_full_path()
    postactive = 'active'
    post = get_object_or_404(BlogPost, name_slug=slug)
    pageTitle = post.page_title
    pageDescription = post.page_description
    canonical_url = f'posts/{post.name_slug}/'
    return render(request, 'page/post.html', locals())


def search(request):
    all_categories = Category.objects.filter(is_active=True)
    print(request.POST)
    breadcrumb_item = f'Результаты поиска по запросу: {request.POST.get("query")}'
    items = Item.objects.filter(name_lower__contains=request.POST.get("query").lower())
    return render(request, 'page/items_page.html', locals())

def partner(request):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/partner.html', locals())
def register(request):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/register.html', locals())
def login(request):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/login.html', locals())
def sale(request):
    all_categories = Category.objects.filter(is_active=True)
    breadcrumb_item = f'Товары со скидками'
    items = Item.objects.filter(discount__gt=0)
    banners = Banner.objects.filter(at_sale_page=True,is_active=True)
    show_banner = True
    return render(request, 'page/items_page.html', locals())

def manufactor(request,manufactor_slug):
    all_categories = Category.objects.filter(is_active=True)
    manufactor = Manufactor.objects.get(name_slug=manufactor_slug)

    breadcrumb_item = f'Товары производителя: {manufactor.name}'
    breadcrumb_return = 'Производители'
    breadcrumb_return_url = '/manufacturers/'
    items_temp = Item.objects.filter(manufactor=manufactor)
    print('items_temp',items_temp)
    count = request.GET.get('count')
    page = request.GET.get('page')
    if count:
        items_paginator = Paginator(items_temp, int(count))
        param_count = count
    else:
        items_paginator = Paginator(items_temp, 12)

    print('items_paginator', items_paginator)
    try:
        items = items_paginator.get_page(page)
    except PageNotAnInteger:
        items = items_paginator.page(1)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)
    return render(request, 'page/items_page.html', locals())


def about(request):
    all_categories = Category.objects.filter(is_active=True, is_in_index_catalog=True)
    return render(request, 'page/about.html', locals())



def contacts(request):

    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/contacts.html', locals())


def delivery(request):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/delivery.html', locals())


def manufacturers(request):
    all_categories = Category.objects.filter(is_active=True)
    all_manufacturers = Manufactor.objects.all()
    return render(request, 'page/manufacturers.html', locals())

def catalog(request):
    all_categories = Category.objects.all()
    return render(request, 'page/catalog.html', locals())


def manufacturers_cat(request,slug):
    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/manufacturers.html', locals())



def category(request, category_slug):
    all_categories = Category.objects.filter(is_active=True)
    category = Category.objects.get(name_slug=category_slug)

    # remove_items = Item.objects.filter(category_id=21)
    # print(remove_items)
    # for item in remove_items:
    #     item.category_id=10
    #     item.save()
    items_qs = Item.objects.filter(category=category,is_active=True)
    items = items_qs
    manufactors = category.manufactor.all()
    qs_filtered = False
    search_res = False
    count = request.GET.get('count')
    page = request.GET.get('page')
    order = request.GET.get('order')
    filter_manufactor = request.GET.get('manufactor')
    search_q = request.GET.get('search')


    if search_q:
        items = items_qs.filter(name_lower__contains=search_q.lower())
        search_res = True
        param_search = search_q

    if filter_manufactor:
        if search_res:
            items = items.filter(manufactor__name_slug=filter_manufactor)
        else:
            items = items_qs.filter(manufactor__name_slug=filter_manufactor)
        qs_filtered = True
        param_manufactor = filter_manufactor

    if order == 'price_gte':
        if qs_filtered or search_res:
            items = items.order_by('-price')
        else:
            items = items_qs.order_by('-price')
        param_order = order

    if order == 'price_lte':
        if qs_filtered or search_res:
            items = items.order_by('price')
        else:
            items = items_qs.order_by('price')
        param_order = order

    if order == 'name_az':
        if qs_filtered or search_res:
            items = items.order_by('name')
        else:
            items = items_qs.order_by('name')
        param_order = order

    if order == 'name_za':
        if qs_filtered or search_res:
            items = items.order_by('-name')
        else:
            items = items_qs.order_by('-name')
        param_order = order

    if count:
        items_paginator = Paginator(items, int(count))
        param_count = count
    else:
        items_paginator = Paginator(items, 18)

    print('items_paginator',items_paginator)
    try:
        items = items_paginator.get_page(page)
    except PageNotAnInteger:
        items = items_paginator.page(1)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)

    return render(request, 'page/category.html', locals())

def subcategory(request, category_slug, subcategory_slug):
    all_categories = Category.objects.filter(is_active=True)
    category = Category.objects.get(name_slug=category_slug)
    subcategory = SubCategory.objects.get(name_slug=subcategory_slug)
    items_qs = Item.objects.filter(subcategory=subcategory,is_active=True)
    items = items_qs
    manufactors = subcategory.manufactor.all()
   # manufactors = subcategory.manufactor_set.all()
    qs_filtered = False
    search_res = False
    count = request.GET.get('count')
    page = request.GET.get('page')
    order = request.GET.get('order')
    filter_manufactor = request.GET.get('manufactor')
    search_q = request.GET.get('search')

    if search_q:
        items = items_qs.filter(name_lower__contains=search_q.lower())
        search_res = True
        param_search = search_q

    if filter_manufactor:
        if search_res:
            items = items.filter(manufactor__name_slug=filter_manufactor)
        else:
            items = items_qs.filter(manufactor__name_slug=filter_manufactor)
        qs_filtered = True
        param_manufactor = filter_manufactor

    if order == 'price_gte':
        if qs_filtered or search_res:
            items = items.order_by('-price')
        else:
            items = items_qs.order_by('-price')
        param_order = order

    if order == 'price_lte':
        if qs_filtered or search_res:
            items = items.order_by('price')
        else:
            items = items_qs.order_by('price')
        param_order = order

    if order == 'name_az':
        if qs_filtered or search_res:
            items = items.order_by('name')
        else:
            items = items_qs.order_by('name')
        param_order = order

    if order == 'name_za':
        if qs_filtered or search_res:
            items = items.order_by('-name')
        else:
            items = items_qs.order_by('-name')
        param_order = order
    if count:
        items_paginator = Paginator(items, int(count))
        param_count = count
    else:
        items_paginator = Paginator(items, 18)

    print('items_paginator', items_paginator)
    try:
        items = items_paginator.get_page(page)
    except PageNotAnInteger:
        items = items_paginator.page(1)
    except EmptyPage:
        items = items_paginator.page(items_paginator.num_pages)


    return render(request, 'page/category.html', locals())

def item_page(request,category_slug,item_slug,subcategory_slug=None):
    if subcategory_slug:
        subcategory = get_object_or_404(SubCategory, name_slug=subcategory_slug)
    category = get_object_or_404(Category, name_slug=category_slug)
    all_categories = Category.objects.filter(is_active=True)

    item = get_object_or_404(Item, name_slug=item_slug)
    item.views += 1
    item.save()

    if subcategory_slug:
        recomended_items = Item.objects.filter(subcategory=subcategory,views__gt=10).order_by('-views')
    else:
        recomended_items = Item.objects.filter(category=category, views__gt=20).order_by('-views')

    filter_qs(1,None,{'dsf':'sada'})
    return render(request, 'page/item.html', locals())

def filter_qs(qs,*args,**kwargs):
    print('filter')
    print(qs)
    print(**kwargs)

def create_password():
    from random import choices
    import string
    password = ''.join(choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    return password

def checkout(request):
    if request.POST:
        order_code = create_password()
        order = Order.objects.create(order_code=order_code,
                                     delivery=request.POST.get('delivery'),
                                     fio=request.POST.get('fio'),
                                     email=request.POST.get('email'),
                                     phone=request.POST.get('phone'),
                                     comment=request.POST.get('comment'),
                                     )
        if request.user.is_authenticated:
            all_cart_items = Cart.objects.filter(client_id=request.user.id)
            order.client = request.user
            order.save()
        else:
            s_key = request.session.session_key
            guest = Guest.objects.get(session=s_key)
            all_cart_items = Cart.objects.filter(guest_id=guest.id)


        for item in all_cart_items:
            ItemsInOrder.objects.create(order_id=order.id, item_id=item.item.id, number=item.number,
                                        current_price=item.item.price)
            item.item.buys = item.item.buys + 1
            item.item.save(force_update=True)
        all_cart_items.delete()


        msg_html = render_to_string('email/order.html', {'order_id': order.id,
                                                        'fio': request.POST.get('fio'),
                                                        'email': request.POST.get('email'),
                                                        'phone': request.POST.get('phone'),
                                                        'delivery': request.POST.get('delivery'),
                                                        'comment': request.POST.get('comment')
                                                         })
        msg_html_client = render_to_string('email/order_client.html', {'order_code': order_code})
        send_mail('Новый заказ', None, 'info@ideahome74.ru', (settings.MAIL_TO,),
                  fail_silently=False, html_message=msg_html)
        send_mail('Заказ создан', None, 'info@ideahome74.ru', (request.POST.get('email'),),
                  fail_silently=False, html_message=msg_html_client)
        return HttpResponseRedirect('/order/{}'.format(order.order_code))



    all_categories = Category.objects.filter(is_active=True)
    return render(request, 'page/checkout.html', locals())
