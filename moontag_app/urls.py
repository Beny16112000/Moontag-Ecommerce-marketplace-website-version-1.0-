from django.urls import path,include
from moontag_app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home,name='home'),
    path('register1',views.register1,name='register1'),
    path('login1',views.login1,name='login1'),
    path('logout1',views.logout1,name='log_out1'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('categories',views.categories,name='categories'),
    path('brands',views.brands,name='brands'),
    path('product-list',views.product_list,name='product-list'),
    path('category-product-list/<int:cat_id>',views.category_product_list,name='category-product-list'),
    path('brand-product-list/<int:brand_id>',views.brand_product_list,name='brand-product-list'),
    path('product/<str:slug>/<int:id>',views.product_page,name='product_page'),
    path('search-result',views.search_result,name='search_result'),
    path('filter-data',views.filter_data,name='filter_data'),
    path('add-to-cart',views.add_to_cart,name='add_to_cart'),
    path('cart',views.cart_page,name='cart'),
    path('delete-from-cart',views.delete_cart_item,name='delete_cart_item'),
    path('update-cart',views.update_cart_item,name='update-cart'),
    path('checkout',views.checkout,name='checkout'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('add-product',views.add_product,name='add_product'),
    path('add-category',views.add_category,name='add_category'),
    path('add-brand',views.add_brand,name='add_brand'),
    path('add-color',views.add_color,name='add_color'),
    path('add-size',views.add_size,name='add_size'),
    path('add-banner',views.add_banner,name='add_banner'),
    path('user-dashboard',views.user_dashboard,name='user_dashboard'),
    path('user-orders',views.user_orders,name='user_orders'),
    path('user-orders-items/<int:id>',views.user_orders_items,name='user_orders_items'),
    path('add-attribute',views.add_attribute,name='add_attribute'),
    path('order-search',views.order_search,name='order_search'),
    path('checkout-purchasing',views.checkout_purchasing,name='checkout_purchasing'),
    path('display-product',views.display_product,name='display_product'),
    path('data',views.data,name='data'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)