# coding=utf-8
from django.conf.urls import url

from apps.core import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    # url(r'^contents/$', views.ContentList.as_view()),
    # url(r'^content/$', views.ContentView.as_view()),
    # url(r'^mine/$', views.Mine.as_view()),
    # url(r'^laud/$', views.Lauds.as_view()),
    # url(r'^notices/$', views.NoticeList.as_view()),
    # url(r'^notice/refresh$', views.RefreshNotice.as_view()),
    # url(r'^newnotice/$', views.NewNotice.as_view()),
    # url(r'^comment/$', views.CommentView.as_view()),
    # url(r'^comments/$', views.CommentList.as_view()),
    # url(r'^upload/$', views.Upload.as_view()),
    # url(r'^auth/$', views.Auth.as_view()),
    # url(r'^user/edit/$', views.EditUserView.as_view()),
    # url(r'^contentadd/$', views.ContentAdd.as_view()),
    # url(r'^usercontents/$', views.UserContents.as_view()),
    # url(r'^attentionadd/$', views.AttentionAdd.as_view()),
    # url(r'^collectadd/$', views.Collectadd.as_view()),
    # url(r'^contentdel/$', views.ContentDel.as_view()),
    # url(r'^usereditupload/$', views.UserEditUoload.as_view()),
    # url(r'^useredit/$', views.UserEdit.as_view()),
    # url(r'^collectlist/$', views.CollectList.as_view()),
    # url(r'^fanslist/$', views.FansList.as_view()),
    # url(r'^attentiondel/$', views.AttentionDel.as_view()),
    # url(r'^attentionlist/$', views.AttentionList.as_view()),
    # url(r'^attentionuserids/$', views.AttentionUserIdList.as_view()),
    # url(r'^attentioncontents/$', views.AttentionContentList.as_view()),
    # url(r'^vedioes/$', views.VideoList.as_view()),
    # url(r'^publicnews/$', views.PublicNewsList.as_view()),
    # url(r'^feedback/$', views.FeedbackView.as_view()),

]