from django.contrib import admin

from bookMS.models import Books, Users, Borrows


class BooksAdmin(admin.ModelAdmin):
    """
    自定义BooksAdmin
    """
    # 需要显示的字段信息
    list_display = ('id', 'book_name', 'book_type', 'book_authors', 'book_publisher', 'book_price', 'book_status')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'book_name')


class UsersAdmin(admin.ModelAdmin):
    """
    自定义UsersAdmin
    """
    # 需要显示的字段信息
    list_display = ('id', 'user_name', 'user_mobile', 'user_sex')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'user_name')


class BorrowsAdmin(admin.ModelAdmin):
    """
    自定义BorrowsAdmin
    """
    # 需要显示的字段信息
    list_display = ('id', 'user_id', 'book_id', 'borrow_time', 'borrow_status', 'return_time')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'user_id', 'book_id', 'borrow_status')


# 注册自定义admin
admin.site.register(Books, BooksAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Borrows, BorrowsAdmin)

# 修改Django管理后台title和站点header。
admin.site.site_title = "图书管理系统后台"
admin.site.site_header = "图书管理系统后台"