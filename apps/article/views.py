# _*_ encoding:utf-8 _*_
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger

from .models import Article, GoldenSpiderAward, AwardSort, AwardIterm


# Create your views here.


class IndexView(View):
    """
    首页内容
    """

    def get(self, request):
        # 所有文章
        all_articles = Article.objects.all()

        # 轮播图列表
        banners = all_articles.filter(tag='banner').order_by("order")[0:3]

        # 我们的服务
        our_services = all_articles.filter(tag='our_services').order_by("order")[0:3]

        # 我们的案例
        our_cases = all_articles.filter(tag='our_cases').order_by("order")[0:10]

        # 战略平台
        our_platforms = all_articles.filter(tag='our_platforms').order_by("order")[0:3]

        # 合作伙伴
        our_friends = all_articles.filter(tag='our_friends').order_by("order")[0:1]

        # 合作伙伴
        our_contacts = all_articles.filter(tag='our_contacts').order_by("order")

        return render(request, "index.html", {
            "banners": banners,
            "our_services": our_services,
            "our_cases": our_cases,

            "our_platforms": our_platforms,
            "our_friends": our_friends,
            "our_contacts": our_contacts,
        })


class AllianceView(View):
    """
    视频联盟页面内容
    """
    def get(self, request):
        # 所有文章
        all_articles = Article.objects.all()

        # 联盟轮播资讯top5
        alliance_news = all_articles.filter(tag='alliance_news').order_by("order")[0:3]

        # 联盟简介
        alliance_intro = all_articles.get(tag='alliance_intro')

        # 合作伙伴
        our_friends = all_articles.filter(tag='our_friends').order_by("order")[0:1]

        # 联系方式
        our_contacts = all_articles.filter(tag='our_contacts').order_by("order")

        return render(request, "alliance.html", {
            "alliance_news": alliance_news,
            "alliance_intro": alliance_intro,
            "our_friends": our_friends,
            "our_contacts": our_contacts,
        })


class CenterView(View):
    """
    视频中心页面内容
    """
    def get(self, request):
        # 所有文章
        all_articles = Article.objects.all()

        # 视频中心轮播资讯top5
        center_news = all_articles.filter(tag='center_news').order_by("order")[0:5]

        # 视频中心简介
        center_intro = all_articles.get(tag='center_intro')

        # 合作伙伴
        our_friends = all_articles.filter(tag='our_friends').order_by("order")[0:1]

        # 联系方式
        our_contacts = all_articles.filter(tag='our_contacts').order_by("order")

        return render(request, "center.html", {
            "center_news": center_news,
            "center_intro": center_intro,
            "our_friends": our_friends,
            "our_contacts": our_contacts,
        })


class MoreCasesView(View):
    """
    更多案例
    """

    def get(self, request, page='2'):
        # 更多案例
        page = int(page)
        begin_index = 5 + (page - 1) * 5
        end_index = 10 + (page - 1) * 5
        more_cases = Article.objects.all().filter(tag='our_cases').order_by("order")[begin_index:end_index]
        if more_cases is None:
            return HttpResponse('{"status":"fail", "msg":"没有更多案例了！"}', content_type='application/json')
        else:
            more_cases = serializers.serialize("json", more_cases)
            return HttpResponse('{"status":"success", "msg":"success", "list":' + more_cases + '}',
                                content_type='application/json')


class ArticleListView(View):
    """
    资讯列表，默认展示联盟资讯
    """

    def get(self, request, tag='alliance_news'):
        # 所有文章
        all_articles = Article.objects.all()

        # 资讯
        alliance_news = all_articles.filter(tag=tag).order_by("order")[0:10]
        # 对资讯进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(alliance_news, 5, request=request)
        alliance_news = p.page(page)

        # 联系方式
        our_contacts = all_articles.filter(tag='our_contacts').order_by("order")

        return render(request, "article_list.html", {
            "alliance_news": alliance_news,
            "our_contacts": our_contacts,
        })


class ArticleDetailView(View):
    """
    轮播图列表
    """

    def get(self, request, id):
        # 所有文章
        all_articles = Article.objects.all()

        # 资讯详情
        news_detail = all_articles.get(id=id)

        # 联系方式
        our_contacts = all_articles.filter(tag='our_contacts').order_by("order")
        return render(request, "article_detail.html", {
            "news_detail": news_detail,
            "our_contacts": our_contacts,
        })


class GoldenSpiderAwardView(View):
    """
    金蜘蛛奖页面内容
    """
    def get(self, request):
        # 最近三届
        awards = GoldenSpiderAward.objects.all().order_by("order")[0:3]

        # 最近一届金蜘蛛奖的内容
        award = awards[0]

        # 战略合作单位需要特殊处理一下
        co_companies = award.strip('|').split('|')

        # 奖项设置
        award_sorts = AwardSort.objects.filter(golden_spider_award=award.id).all()

        # 奖项下的参赛作品
        award_iterms = []
        for award_sort in award_sorts:
            award_iterms.append(AwardIterm.objects.filter(award_sort=award_sort.id).order_by("order")[0:4])

        # 联系方式
        our_contacts = Article.objects.filter(tag='our_contacts').order_by("order")

        return render(request, "center.html", {
            "award": award,
            "co_companies": co_companies,
            "award_sorts": award_sorts,
            "award_iterms": award_iterms,
            "our_contacts": our_contacts,
        })
