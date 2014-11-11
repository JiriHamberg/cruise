from django.conf.urls import patterns, url

from cruise import views, json_views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^cabins$', views.CabinView.as_view(), name='cabin_list' ),
    url(r'person/register/$', views.PersonRegister.as_view(), name='person_register'),
    url(r'person/(?P<pk>\d+)/$', views.PersonUpdate.as_view(), name='person_update'),
    url(r'person/edit/$', views.PersonAuthenticate.as_view(), name='person_authenticate_view'),
	url(r'json/cabin_category$', json_views.cabin_categories, name='json_cabin_categories'),
	url(r'json/person_info$', json_views.person_info, name='json_person_info'),
)