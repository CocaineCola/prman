# -*- coding: utf-8 -*-
__author__ = 'bobby'
__date__ = '2016/10/25 23:52'
import xadmin

from .models import Article, GoldenSpiderAward, AwardSort, AwardIterm


class ArticleAdmin(object):
    list_display = ['title', 'author', 'desc', 'order', 'detail', 'tag', 'golden_spider_award', 'url', 'image', 'click_nums',
                    'fav_nums', 'add_time']
    search_fields = ['title', 'author', 'desc', 'order', 'detail', 'tag', 'golden_spider_award', 'url', 'image', 'click_nums',
                     'fav_nums']
    list_filter = ['title', 'author', 'desc', 'order', 'detail', 'tag', 'golden_spider_award', 'url', 'image', 'click_nums',
                   'fav_nums', 'add_time']
    relfield_style = 'fk-ajax'
    style_fields = {"detail": "ueditor"}
    model_icon = 'fa fa-university'


# 金蜘蛛奖
class GoldenSpiderAwardAdmin(object):
    list_display = ['title', 'sponsor', 'co_sponsor', 'date', 'address', 'intro', 'specialists', 'process',
                    'co_companies', 'platforms', 'media_orgs', 'shoot_orgs', 'order', 'add_time']
    search_fields = ['title', 'sponsor', 'co_sponsor', 'date', 'address', 'intro', 'specialists', 'process',
                     'co_companies', 'platforms', 'media_orgs', 'shoot_orgs', 'order']
    list_filter = ['title', 'sponsor', 'co_sponsor', 'date', 'address', 'intro', 'specialists', 'process',
                    'co_companies', 'platforms', 'media_orgs', 'shoot_orgs', 'order', 'add_time']
    relfield_style = 'fk-ajax'
    style_fields = {"intro": "ueditor"}
    model_icon = 'fa fa-university'


# 金蜘蛛奖奖项
class AwardSortAdmin(object):
    list_display = ['golden_spider_award', 'title', 'order', 'add_time']
    search_fields = ['golden_spider_award', 'title', 'order']
    list_filter = ['golden_spider_award', 'title', 'order', 'add_time']
    relfield_style = 'fk-ajax'
    model_icon = 'fa fa-university'


# 金蜘蛛奖参选作品
class AwardItermAdmin(object):
    list_display = ['golden_spider_award', 'award_sort_id', 'title', 'image', 'order', 'fav_nums', 'add_time']
    search_fields = ['golden_spider_award', 'award_sort_id', 'title', 'image', 'order', 'fav_nums']
    list_filter = ['golden_spider_award', 'award_sort_id', 'title', 'image', 'order', 'fav_nums', 'add_time']
    relfield_style = 'fk-ajax'
    model_icon = 'fa fa-university'

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(GoldenSpiderAward, GoldenSpiderAwardAdmin)
xadmin.site.register(AwardSort, AwardSortAdmin)
xadmin.site.register(AwardIterm, AwardItermAdmin)
