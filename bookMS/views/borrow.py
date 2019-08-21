from django.shortcuts import render
from bookMS.models import Borrows, Users, Books
from bookMS.views.common import page


def index(request, book_id):
    """
    图书借阅页面
    :param request:
    :param book_id:
    :return:
    """
    context = None
    if book_id > 0:
        book = Books.objects.get(id=book_id)
        context = {'book': book}
    return render(request, 'bookMS/borrows/borrow.html', context)


def add(request):
    """
    添加图书借阅信息
    :param request:
    :return:
    """
    try:
        ob = Borrows()
        ob.user_id = Users.objects.get(id=request.session['user_id'])
        ob.book_id = Books.objects.get(id=request.POST['book_id'])
        return_time = request.POST['return_time']
        if return_time:
            ob.return_time = return_time
            ob.save()
            context = {'info': '借阅申请成功！'}
        else:
            context = {'info': '归还时间不能为空！'}
    except Exception as err:
        print(err)
        context = {'info': '借阅申请失败！'}
    return render(request, "bookMS/info.html", context)


def his(request, pid):
    """图书借阅历史页面
    :param request:
    :param pid:
    :return:
    """
    borrows = Borrows.objects.filter(user_id=request.session['user_id']).order_by('id')
    borrows = page(request, borrows, pid)
    context = {"borrowsList": borrows}
    return render(request, 'bookMS/borrows/his.html', context)
