from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.teachers, name="home"),
    path('subjects/', views.subjects, name="subjects"),
    path('upload_teachers/', views.upload_teachers, name="upload_teachers"),
    path('teachers/', views.teachers, name="teachers"),
    path('delete_teacher/<str:pk>/', views.delete_teacher, name="delete_teacher"),
    path('update_teacher/<str:pk>/', views.update_teacher, name="update_teacher"),
    path('add_teacher/', views.add_teacher, name="add_teacher"),
    path('teacher_subjects/<str:pk>/', views.teacher_subjects, name="teacher_subjects"),
    path('create_subject/', views.create_subject, name="create_subject"),
    path('update_subject/<str:pk>', views.update_subject, name="update_subject"),
    path('delete_subject/<str:pk>', views.delete_subject, name="delete_subject"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout")
] \
    + static("/static/", document_root=settings.STATIC_ROOT) \
    + static("/media/",document_root=settings.MEDIA_ROOT)

