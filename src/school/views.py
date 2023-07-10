from django.shortcuts import render

from school.models import Group


def all_groups_view(request):
    data_dict_with_groups = Group.objects.all()
    return render(request, 'group_html', context={'groups': data_dict_with_groups})
    # Create your views here.
