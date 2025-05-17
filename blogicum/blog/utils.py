# from datetime import datetime

from django.db.models import Count
from django.utils import timezone


from .models import Post


def optimal_queryset(
        manager=Post.objects,
        filter_published=False,
        annotate_comments=True):
    queryset = manager.select_related(
        'category',
        'location',
        'author')
    if filter_published:
        queryset = queryset.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )
    if annotate_comments:
        queryset = queryset.annotate(
            comment_count=Count('comments')).order_by('-pub_date')

    return queryset
