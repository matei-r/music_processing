from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

app_name = 'composer'

urlpatterns = [

    # /composer/
    url(r'^$', views.HomeView.as_view(), name='home'),

    # /composer/registration
    url(r'^registration$', views.RegistrationView.as_view(), name='registration'),

    # /composer/login
    url(r'^login$', views.LoginView.as_view(), name='login'),

    # /composer/profile
    url(r'^profile$', views.ProfileView.as_view(), name='profile'),

    # /composer/logout
    url(r'^logout$', logout, {'next_page': '/composer/'},name='logout'),

    # /composer/projects
    url(r'^projects$', views.ProjectsView.as_view() ,name='projects'),

    # /composer/projects/new
    url(r'^projects/new$', views.NewProjectView.as_view() ,name='new_project'),

    # /composer/project/<pk>
    url(r'^project/(?P<pk>[0-9]+)/$', views.CurrentProjectView.as_view() ,name='project'),

    # /composer/project/<pk>/delete
    url(r'^project/(?P<pk>[0-9]+)/delete/', views.SongDelete.as_view() ,name='delete-song'),

]
