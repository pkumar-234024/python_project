from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^teacher_home', teacher_home, name='teacher_home'),
    url(r'^show', show, name='show'),
    url(r'^add_new', add_new, name='add_new'),
    url(r'^delete', delete, name='delete'),
    url(r'^teacher_registration',teacher_registration, name = 'teacher_registration')
    # url(r'^edit', edit, name='edit'),
    # url(r'^update', update, name='update'),
]

#     url(r'^Student_first_year$', display_Student_first_year, name="display_Student_first_year"),
#     url(r'^Student_second_year$', display_Student_second_year, name="display_Student_second_year"),
#     url(r'^Student_third_year$', display_Student_third_year, name="display_Student_third_year"),
#     url(r'^Student_fourth_year$', display_Student_fourth_year, name="display_Student_fourth_year"),


#     url(r'^add_Student_first_year$', add_Student_first_year, name="add_Student_first_year"),
#     url(r'^add_Student_second_year$', add_Student_second_year, name="add_Student_second_year"),
#     url(r'^add_Student_third_year$', add_Student_third_year, name="add_Student_third_year"),
#     url(r'^add_Student_four_year$', add_Student_fourth_year, name="add_Student_fourth_year"),
    
#     url(r'^Student_first_years/edit_item/(?P<pk>\d+)$', edit_Student_first_year, name="edit_Student_first_year"),
#     url(r'^Student_second_years/edit_item/(?P<pk>\d+)$', edit_Student_second_year, name="edit_Student_second_year"),
#     url(r'^Student_third_years/edit_item/(?P<pk>\d+)$', edit_Student_third_year, name="edit_Student_third_year"),
#     url(r'^Student_fourth_years/edit_item/(?P<pk>\d+)$', edit_Student_fourth_year, name="edit_Student_fourth_year"),
    

#     url(r'^Student_first_years/delete/(?P<pk>\d+)$', delete_Student_first_year, name="delete_Student_first_year"),
#     url(r'^Student_second_years/delete/(?P<pk>\d+)$', delete_Student_second_year, name="delete_Student_second_year"),
#     url(r'^Student_third_years/delete/(?P<pk>\d+)$', delete_Student_third_year, name="delete_Student_third_year"),
#     url(r'^Student_fourth_years/delete/(?P<pk>\d+)$', delete_Student_fourth_year, name="delete_Student_fourth_year"),
# ]