# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from DjangoUeditor.models import UEditorField


# Create your models here.


# 金蜘蛛奖
class GoldenSpiderAward(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    sponsor = models.CharField(max_length=100, verbose_name=u"主办方")
    co_sponsor = models.CharField(max_length=100, verbose_name=u"协办方")
    date = models.CharField(max_length=100, verbose_name=u"举办日期")
    address = models.CharField(max_length=300, verbose_name=u"举办地址")
    intro = UEditorField(blank=True, verbose_name=u"奖项介绍", width=900, height=300, imagePath="org/ueditor/",
                                        filePath="org/ueditor/", default='')
    specialists = models.ImageField(blank=True, upload_to="org/%Y/%m", verbose_name=u"专家评审团", max_length=100)
    process = models.ImageField(blank=True, upload_to="org/%Y/%m", verbose_name=u"评选流程", max_length=100)
    co_companies = models.CharField(max_length=1000, verbose_name=u"战略合作单位")
    platforms = models.ImageField(blank=True, upload_to="org/%Y/%m", verbose_name=u"战略合作平台", max_length=100)
    media_orgs = models.ImageField(blank=True, upload_to="org/%Y/%m", verbose_name=u"媒体支持", max_length=100)
    shoot_orgs = models.ImageField(blank=True, upload_to="org/%Y/%m", verbose_name=u"指定拍摄机构", max_length=100)
    order = models.IntegerField(default=0, verbose_name=u"排序")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"金蜘蛛奖"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"文章标题")
    author = models.CharField(max_length=100, verbose_name=u"编辑")
    desc = models.CharField(blank=True, max_length=100, verbose_name=u"文章摘要")
    detail = UEditorField(blank=True, verbose_name=u"文章内容", width=900, height=300, imagePath="org/ueditor/",
                                        filePath="org/ueditor/", default='')
    tag = models.CharField(default="", max_length=100, verbose_name=u"文章标签")
    golden_spider_award = models.ForeignKey(GoldenSpiderAward, verbose_name=u"关联的金蜘蛛奖id", null=True, blank=True)
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(blank=True, upload_to="org/%Y/%m", verbose_name=u"logo", max_length=100)
    url = models.CharField(blank=True, default="", max_length=300, verbose_name=u"文章跳转地址")
    order = models.IntegerField(default=0, verbose_name=u"文章排序")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"资讯"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 金蜘蛛奖奖项
class AwardSort(models.Model):
    golden_spider_award = models.ForeignKey(GoldenSpiderAward, verbose_name=u"关联的金蜘蛛奖id", null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name=u"奖项名称")
    order = models.IntegerField(default=0, verbose_name=u"排序")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"金蜘蛛奖奖项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 金蜘蛛奖参选作品
class AwardIterm(models.Model):
    golden_spider_award = models.ForeignKey(GoldenSpiderAward, verbose_name=u"关联的金蜘蛛奖id")
    award_sort_id = models.ForeignKey(AwardSort, verbose_name=u"关联的奖项id")
    title = models.CharField(max_length=100, verbose_name=u"作品标题")
    image = models.ImageField(blank=True, upload_to="org/%Y/%m", verbose_name=u"作品图片", max_length=100)
    fav_nums = models.IntegerField(default=0, verbose_name=u"投票数")
    order = models.IntegerField(default=0, verbose_name=u"排序")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"金蜘蛛奖参选作品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title