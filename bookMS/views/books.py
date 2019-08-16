from django.db.models import Q
from django.shortcuts import render


from bookMS.models import Books
from bookMS.views.common import page


def index(request, pid):
    """查看所有图书
    :param request:http请求
    :param pid: 页码
    :return:图书列表
    """
    books = Books.objects.filter(book_status=0)
    books = page(request, books, pid)
    context = {"booksList": books}
    return render(request, 'bookMS/books/books.html', context)


def search(request):
    """搜索图书
    :param request:
    :return: 匹配到的图书列表
    """
    key_word = request.GET['key_word']
    books = Books.objects.filter(Q(book_name__contains=key_word) | Q(book_authors__contains=key_word))
    books = page(request, books, 1)
    context = {"booksList": books, "key_word": key_word}
    return render(request, 'bookMS/books/books.html', context)

