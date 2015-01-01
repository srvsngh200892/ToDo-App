from django.conf.urls import patterns, include, url
from task_manager.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'task_manager.views.auth_login', name='user_login'),
    url(r'^logout/$', 'task_manager.views.user_logout', name='user_logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^home/add/task/$', 'task_manager.views.add_task',name='add_task'),
    url(r'^home/edit/task/(?P<tid>[a-zA-Z0-9]+)/$', 'task_manager.views.edit_task',name='edit_task'),
)



 
