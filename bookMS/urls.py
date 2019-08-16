from django.urls import path

from bookMS.views import index, books, borrow, users

app_name = 'bookMS'

urlpatterns = [
    # 前台-首页
    path('', index.index, name="bookMS_index"),

    # 前台-用户路由
    path('login', users.login, name="bookMS_login"),
    path('do_login', users.do_login, name="bookMS_do_login"),
    path('logout', users.logout, name="bookMS_logout"),
    path('verify', users.verify, name="bookMS_verify"),
    path('register', users.register, name="bookMS_register"),
    path('do_register', users.do_register, name="bookMS_do_register"),
    path('my', users.my, name="bookMS_my"),


    # 前台-图书路由
    path('books/<int:pid>/', books.index, name="bookMS_books_index"),
    path('books/search', books.search, name="bookMS_books_search"),
    path('books/page/<int:pid>/', books.page, name="bookMS_books_page"),

    # 前台-借阅路由
    path('borrow/<int:book_id>/<', borrow.index, name="bookMS_borrows_index"),
    path('borrow/add/', borrow.add, name="bookMS_borrows_add"),
    path('borrow/his/<int:pid>/', borrow.his, name="bookMS_borrows_his"),
]
