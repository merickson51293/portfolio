from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('index', views.index),
    path('blog', views.blog),
    path('blog_post/<int:blog_id>', views.blog_post),
    path('proj_page/<int:project_id>', views.proj_page),
    path('sweet_petite/index', views.spd),
    path('church_finder/index', views.church_finder),
    path('guest', views.guest),
    path('user_reg', views.user_reg),
    path('church_reg_log', views.church_reg_log),
    path('create_user', views.create_user),
    path('login', views.login),
    path('create_church', views.create_church),
    path('church_login', views.church_login),
    path('logout', views.logout),
    path('church_info', views.church_info),
    path('user_info', views.user_info),
    path('create_church_contact', views.create_church_contact),
    path('create_user_contact', views.create_user_contact),
    path('user_pic', views.user_pic),
    path('church_contact', views.church_contact),
    path('user_contact', views.user_contact),
    path('user_church', views.user_church),
    path('create_user_church', views.create_user_church),
    path('user_info_other', views.user_info_other),
    path('finish_user', views.finish_user),
    path('create_church_beliefs', views.create_church_beliefs),
    path('church_beliefs', views.church_beliefs),
    path('church_pastor', views.church_pastor),
    path('create_pastor', views.create_pastor),
    path('create_church_info_other', views.create_church_info_other),
    path('church_info_other', views.church_info_other),
    path('church_success', views.church_success),
    path('church_profile/<int:church_id>', views. church_profile),
    path('edit_church/<int:church_id>', views.edit_church),
    path('edit/<int:church_id>', views.edit),
    path('edit_user/<int:user_id>', views.edit_user),
    path('user_edit/<int:user_id>', views.user_edit),
    path('add_message', views.add_message),
    path('church_add_message', views.church_add_message),
    path('church_add_comment/<int:message_id>', views.church_add_comment),
    path('user_add_comment/<int:message_id>', views.user_add_comment),
    path('delete/<int:message_id>', views.delete),
    path('delete_comment/<int:comment_id>', views.delete_comment),
    path('delete_church_message/<int:message_id>', views.delete_church_message),
    path('delete_church_comment/<int:comment_id>', views.delete_church_comment),
    path('delete_church/<int:church_id>', views.delete_church),
    path('church_home_page', views.church_home_page),
    path('user_home_page', views.home_page),
    path('user_profile/<int:user_id>', views.user_profile),
    path('upload', views.image_upload_view),
    path('local_people', views.local_people),
    path('area_churches', views.area_churches),
    path('add_direct_message', views.add_direct_message),
    path('direct_messages/<int:user_id>', views.direct_messages),
    path('church_direct_messages/<int:church_id>', views.church_direct_messages),
    path('reviews', views.reviews),
    path('add_review', views.add_review),
    path('photos', views.photos),
    path('celebrations', views.celebrations),
    path('graduation', views.graduation),
    path('misc', views.misc),
    path('menu', views.menu),
    path('contact', views.contact),
    path('success', views.success),
    path('order', views.order),
    path('spblog', views.spblog),
    path('good/<int:goods_id>', views.good)
]