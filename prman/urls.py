# _*_ encoding:utf-8 _*_
"""prman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.views.static import serve

import xadmin
from article.views import IndexView, ArticleListView, ArticleDetailView, MoreCasesView, AllianceView, CenterView, \
    AllAwardCacesView, GoldenSpiderAwardView, GoldenSpiderPollView, AllAwardHistoryView
from prman.settings import MEDIA_ROOT
from users.views import LogoutView, LoginView, RegisterView, AciveUserView, ForgetPwdView, ResetView, ModifyPwdView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 首页
    url(r'^$', IndexView.as_view(), name="index"),
    # 视频联盟页
    url(r'^alliance/$', AllianceView.as_view(), name="alliance"),
    # 视频研究中心页
    url(r'^center/$', CenterView.as_view(), name="center"),
    # 金蜘蛛奖
    url(r'^spider/$', GoldenSpiderAwardView.as_view(), name="spider_default"),
    url(r'^spider/(?P<spider_id>\w+)/$', GoldenSpiderAwardView.as_view(), name="spider"),
    # 显示全部参奖作品
    url(r'^all_award_cases/(?P<sort>\w+)/$', AllAwardCacesView.as_view(), name="all_award_cases"),
    # 显示全部往期回顾
    url(r'^all_award_history/$', AllAwardHistoryView.as_view(), name="all_award_cases"),
    # 金蜘蛛奖投票
    url(r'^poll/(?P<iterm_id>\w+)/$', GoldenSpiderPollView.as_view(), name="poll"),
    # 更多案例
    url(r'^more_cases/(?P<page>\w+)/$', MoreCasesView.as_view(), name="more_cases"),
    # 文章列表页
    url(r'^article_list/$', ArticleListView.as_view(), name="article_list_default"),
    url(r'^article_list/(?P<tag>.*)/$', ArticleListView.as_view(), name="article_list"),
    # 文章详情页
    url(r'^article_detail/(?P<id>\d+)/$', ArticleDetailView.as_view(), name="article_detail"),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$',  serve, {"document_root":STATIC_ROOT}),

    # 用户相关url配置
    url(r'^users/', include('users.urls', namespace="users")),

    # 富文本相关url
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]

# 全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
