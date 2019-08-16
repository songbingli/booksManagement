# -*- coding:utf-8 -*-
from django.core.paginator import Paginator


def page(request, obs, pid):
    """分页查询
    :param request:
    :param obs:
    :param pid:
    :return:
    """
    pag = Paginator(obs, 10)
    obs = pag.page(int(pid))
    return obs