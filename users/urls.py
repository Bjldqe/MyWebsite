from django.urls import path
from . import views

app_name = 'users'   # 定义一个命名空间，用来区分不同应用之间的链接地址
urlpatterns = [ 
    path('login', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('active/<active_code>',views.active_user,name='active_user'),
    path('forget_pwd/', views.forget_pwd, name='forget_pwd'),   # 找回密码发送邮件页面
    path('forget_pwd_url/<active_code>', views.forget_pwd_url, name='forget_pwd_url'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('editor_users/', views.editor_users, name='editor_users'), 
    path('logout/', views.logout_view, name='logout'),



]