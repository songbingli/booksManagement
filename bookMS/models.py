from datetime import datetime

from django.db import models


class Books(models.Model):
    """
    图书信息模型
    """
    # 状态选项
    BOOK_STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用'),
    )
    book_name = models.CharField(max_length=50, verbose_name='图书名称')
    book_type = models.CharField(max_length=20, verbose_name='分类')
    book_authors = models.CharField(max_length=50, verbose_name='作者')
    book_publisher = models.CharField(max_length=50, verbose_name='出版社')
    book_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='价格')
    book_add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    book_status = models.IntegerField(choices=BOOK_STATUS_CHOICES, default=0, verbose_name='状态')

    class Meta:
        db_table = "tb_books"  # 更改表名
        verbose_name = "图书管理"
        verbose_name_plural = "图书管理"

    def __str__(self):
        return self.book_name


class Users(models.Model):
    """
    用户信息模型
    """
    # 性别选项
    SEX_CHOICES = (
        (1, '男'),
        (0, '女'),
    )
    # 状态选项
    USER_STATUS_CHOICES = (
        (0, '启用'),
        (1, '禁用'),
    )
    user_name = models.CharField(max_length=32, verbose_name='姓名')
    user_mobile = models.BigIntegerField(default=0, verbose_name='手机号')
    user_sn = models.BigIntegerField(verbose_name='学号')
    user_password = models.CharField(max_length=32, verbose_name='密码')
    user_sex = models.IntegerField(choices=SEX_CHOICES, default=0, verbose_name='性别')
    user_state = models.IntegerField(choices=USER_STATUS_CHOICES, default=0, verbose_name='状态')
    user_add_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    class Meta:
        db_table = "tb_users"  # 更改表名
        verbose_name = "用户管理"
        verbose_name_plural = "用户管理"

    def __str__(self):
        return self.user_name


class Borrows(models.Model):
    """
    图书借阅信息模型
    """
    # 借阅状态选项
    BORROW_STATUS_CHOICES = (
        (0, '借阅中'),
        (1, '已归还'),
    )
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='借阅人')
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='借阅书名')
    borrow_time = models.DateTimeField(default=datetime.now, verbose_name='借阅时间')
    borrow_status = models.IntegerField(choices=BORROW_STATUS_CHOICES, default=0, verbose_name='借阅状态')
    return_time = models.DateTimeField(blank=True, null=True, verbose_name='应还时间')

    class Meta:
        db_table = "tb_borrows"  # 更改表名
        verbose_name = "借阅管理"
        verbose_name_plural = "借阅管理"
