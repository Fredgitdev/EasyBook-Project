
from django.contrib import admin
from django.urls import path
from easybookapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('pages-blank/', views.pagesblank, name='pages-blank'),
    path('pages-contact/', views.pagescontact, name='pages-contact'),
    path('pages-faq/', views.pagesfaq, name='pages-faq'),
    path('pages-login/', views.pageslogin, name='pages-login'),
    path('', views.pagesregister, name='pages-register'),
    path('tables-data/', views.tablesdata, name='tables-data'),
    path('tables-general/', views.tablesgeneral, name='tables-general'),
    path('users-profile/', views.usersprofile, name='users-profile'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('oneway/', views.oneway, name='oneway'),
    path('hire/', views.hire, name='hire'),
    path('onewayconfirmation/', views.onewayconfirmation, name='onewayconfirmation'),
    path('bushireconfirmation/', views.bushireconfirmation, name='bushireconfirmation'),
    path('contactshow/', views.contactshow, name='contactshow'),  # New route for contact data display

    # path('delete/<int:id>', views.delete),
    path('delete_oneway/<int:id>', views.delete_oneway, name='delete_oneway'),
    path('delete_bushire/<int:id>', views.delete_bushire, name='delete_bushire'),
    path('onewayedit/<int:id>', views.onewayedit,name='onewayedit'),
    path('bushireedit/<int:id>', views.bushireedit,name='bushireedit'),
    path('update/<int:id>', views.update,name='update'),
    path('update_oneway/<int:id>', views.update_oneway,name='update_oneway'),

    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]
