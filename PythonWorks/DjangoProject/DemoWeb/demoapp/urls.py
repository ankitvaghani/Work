from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^default/$', views.default, name="default"),		
	url(r'^details/$', views.details, name="view_detail_page"),
	# url(r'^(?P<per1>[0-9]+)/details/$', views.details, name="emp_deatails"),)	
	url(r'^details/(?P<per1>[0-9]+)/(?P<per2>[a-z]+)/$', views.getDetails, name="get_emp_deatails"),			
	url(r'^register/$', views.registerUser, name="Register User"),

	url(r'^home/$', views.home, name="home"),

	url(r'^newuser/$', views.addNewUser, name="Add_New_User"),
	# url(r'^allusers/$', views.getAllUsers, name="Get_All_Users"),

	url(r'^home/(?P<rid>[0-9]+)/remove/$', views.removeUser, name="Remove user"),

	url(r'^home/(?P<eid>[0-9]+)/change/$', views.changeUser, name="Edit user"),
	url(r'^home/(?P<eid>[0-9]+)/edituser/$', views.edituser, name="Edit user"),

	url(r'^login/$', views.doLogin, name="Login"),

	url(r'^logout/$', views.logout, name="logut"),

]