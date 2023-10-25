from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name="home"),
    path('blog/<int:pk>',views.blogs,name='blog'),


    path('Signin',views.Signin,name='Signin' ),
    path('Signup',views.regist_view,name='Signup' ),
    path('Signout',views.Signout,name='Signout' ),


    path('create',views.create_Blog,name='create' ),
    path('edit/<int:pk>',views.edit_Blog,name='edit' ),
    path('delete/<int:pk>',views.delete_Blog,name='delete' ),

    path('custom_tag',views.create_tag,name='custom_tag' ),

    path('create_cmt/<int:pk>',views.create_Cmt,name='create_cmt' ),
    path('edit_cmt/<int:pk>/<int:pk1>',views.edit_Cmt,name='edit_cmt' ),
    path('delete_cmt/<int:pk>/<int:pk1>',views.delete_Cmt,name='delete_cmt' ),

    path('approve_blog/<int:pk>',views.approve,name='approve_blog'),
    path('reject_blog/<int:pk>',views.reject,name='reject_blog')

]
