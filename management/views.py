from management import *


@view_config(route_name='group_manager', renderer='templates/group_manager.mako')
def group_manager_view(request):
    magpie_url = request.registry.settings['magpie.url']
    if 'create' in request.POST:
        group_name = request.POST.get('group_name')
        data = {'group_name': group_name}
        check_res(requests.post(magpie_url+'/groups', data))

    if 'delete' in request.POST:
        group_names = request.POST.getall('group_names')
        for group_name in group_names:
            check_res(requests.delete(magpie_url+'/groups/'+group_name))

    if 'delete_group_users' in request.POST:
        group_name = request.POST.get('group_name')
        user_names = request.POST.getall('user_names')
        for user_name in user_names:
            check_res(requests.delete(magpie_url+'/users/'+user_name+'/groups/'+group_name))

    res_groups = requests.get(magpie_url+'/groups')

    group_users_dict = {}
    try:
        group_names = res_groups.json()['group_names']
        for group_name in group_names:
            res_group_users = requests.get(magpie_url+'/groups/'+group_name+'/users')
            check_res(res_group_users)
            group_users_dict[group_name] = res_group_users.json()['user_names']
    except:
        raise HTTPBadRequest(detail='Bad Json response')


    return {'group_names': group_names,
            'group_users_dict': group_users_dict}


@view_config(route_name='user_manager', renderer='templates/user_manager.mako')
def user_manager_view(request):
    magpie_url = request.registry.settings['magpie.url']
    if 'delete' in request.POST:
        user_names = request.POST.getall('user_names')
        for user_name in user_names:
            check_res(requests.delete(magpie_url+'/users/'+user_name))



    if 'assign' in request.POST:
        user_name = request.POST.get('user_names')
        group_names = request.POST.getall('group_names')
        for group_name in group_names:
            check_res(requests.post(magpie_url+'/users/'+user_name+'/groups/'+group_name))


    if 'delete_user_groups' in request.POST:
        group_names = request.POST.getall('group_names')
        user_name = request.POST.get('user_name')
        for group_name in group_names:
            check_res(requests.delete(magpie_url+'/users/'+user_name+'/groups/'+group_name))

    res = requests.get(magpie_url+'/users')
    group_res = requests.get(magpie_url+'/groups')

    user_groups_dict = {}

    try:
        user_names = res.json()['user_names']
        group_names = group_res.json()['group_names']

        users = []
        for user_name in user_names:
            user_res = requests.get(magpie_url+'/users/'+user_name)
            check_res(user_res)

            user_data = user_res.json()
            users.append(user_data)
            user_groups_res = requests.get(magpie_url+'/users/'+user_name+'/groups')
            user_groups_dict[user_name] = user_groups_res.json()['group_names']
    except:
        raise HTTPBadRequest(detail='Bad Json response')

    return {'users': users,
            'groups': group_names,
            'user_groups_dict': user_groups_dict}


@view_config(route_name='service_manager', renderer='templates/service_manager.mako')
def service_manager_view(request):
    magpie_url = request.registry.settings['magpie.url']

    if 'register' in request.POST:
        data = {'service_name': request.POST.get('service_name'),
                'service_url': request.POST.get('service_url'),
                'service_type': request.POST.get('service_type')}

        check_res(requests.post(magpie_url+'/services', data=data))

    if 'unregister' in request.POST:
        service_names = request.POST.getall('service_names')
        for service_name in service_names:
            check_res(requests.delete(magpie_url+'/services/'+service_name))

    res = requests.get(magpie_url + '/services')
    check_res(res)
    service_names = res.json()['service_names']
    service_info_list = []
    for service_name in service_names:
        res = requests.get(magpie_url+'/services/'+service_name)
        check_res(res)
        service_info_list.append(res.json())

    return {'service_info_list': service_info_list,
            'service_types': ['wps', 'wms', 'thredds']}

