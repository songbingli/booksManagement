from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from bookMS.models import Users


def login(request):
    """
    用户登陆界面
    :param request:
    :return:
    """
    return render(request, 'bookMS/users/login.html')


def do_login(request):
    """
    用户登陆操作
    :param request:
    :return:
    """
    # 校验验证码
    verify_code = request.session['verifycode']
    code = str(request.POST['code']).upper()
    if verify_code != code:
        context = {'info': '验证码错误！'}
        return render(request, "bookMS/users/login.html", context)

    try:
        # 根据账号获取登录者信息
        user = Users.objects.get(user_mobile=request.POST['user_mobile'])
        # 验证密码
        import hashlib
        md5 = hashlib.md5()
        pwd = str(request.POST['user_password']).encode(encoding='utf-8')
        md5.update(pwd)
        pwd = str(md5.hexdigest())
        if user.user_password == pwd and user.user_state == 0:
            # 此处登录成功，将当前登录信息放入到session中，并跳转页面
            request.session['user_id'] = user.id
            request.session['user_name'] = user.user_name
            return redirect(reverse('bookMS:bookMS_index'))
        else:
            context = {'info': '登录密码错误！'}
    except Exception as err:
        print(err)
        context = {'info': '登录账号错误！'}
    return render(request, "bookMS/users/login.html", context)


def verify(request):
    """
    用户登陆图形验证码
    :param request:
    :return:
    """
    # 引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (242, 164, 247)
    width = 100
    height = 35
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('static/STXIHEI.TTF', 21)
    # font = ImageFont.load_default().font
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def logout(request):
    """
    用户退出
    :param request:
    :return:
    """
    # 清除登录的session信息
    del request.session['user_id']
    del request.session['user_name']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('bookMS:bookMS_login'))


def register(request):
    """
    用户注册页面跳转
    :param request:
    :return:
    """
    return render(request, 'bookMS/users/register.html')


def do_register(request):
    """
    用户注册操作
    :param request:
    :return:
    """
    try:
        ob = Users()
        ob.user_name = request.POST['user_name']
        ob.user_mobile = request.POST['user_mobile']
        ob.user_sn = request.POST['user_sn']
        import hashlib
        md5 = hashlib.md5()
        pwd = str(request.POST['user_password']).encode(encoding='utf-8')
        md5.update(pwd)
        pwd = str(md5.hexdigest())
        ob.user_password = pwd
        ob.user_sex = request.POST['user_sex']
        ob.save()
        user = Users.objects.get(user_mobile=ob.user_mobile)
        request.session['user_id'] = user.id
        request.session['user_name'] = user.user_name
        context = {'info': '用户注册成功，欢迎使用！'}
    except Exception as err:
        print(err)
        context = {'info': '注册失败，请检查你的输入信息！'}
        return render(request, "bookMS/users/register.html", context)
    return render(request, "bookMS/info.html", context)


def my(request):
    """
    用户个人资料
    :param request:
    :return:
    """
    user = Users.objects.get(id=request.session['user_id'])
    context = {'my': user}
    return render(request, "bookMS/users/my.html", context)
