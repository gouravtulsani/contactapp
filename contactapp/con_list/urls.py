from rest_framework.routers import SimpleRouter
from . import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


router = SimpleRouter()

router.register(r'contact', views.ContactViewSet)

urlpatterns = router.urls


app_name = 'con_list'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<contact_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<contact_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^create_contact/$', views.create_contact, name='create_contact'),
    url(r'^(?P<contact_id>[0-9]+)/delete_contact/$', views.delete_contact, name='delete_contact'),
	url(r'^api/$', views.contact_list),
    url(r'^api/register$', views.apiregisteration),
    url(r'^api/(?P<pk>[0-9]+)/', views.contact_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)