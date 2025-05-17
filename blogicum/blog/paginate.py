from django.core.paginator import Paginator
from django.conf import settings


def get_paginator(request, queryset,
                  number_of_pages=settings.PAGINATOR_BY):
    """Пагинатор."""
    paginator = Paginator(queryset, number_of_pages)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
