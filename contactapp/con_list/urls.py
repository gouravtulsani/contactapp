from rest_framework.routers import SimpleRouter
from . import views
from django.conf.urls import url

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
]