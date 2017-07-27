<h3>Create Group</h3>
<form action="${request.path}" method="post">
    <input type="text" name="group_name">

    <input type="submit" value="Create Group" name="create">
</form>


<h3>Delete Group</h3>
<form action="${request.path}" method="post">
 %for group in group_names:
<input type="checkbox" name="group_names" value="${group}" />${group}</br>
%endfor
<input type="submit" value="Delete Group" name="delete">
</form>

<h3>Delete Users From Group</h3>
<form action="${request.path}" method="post">
 %for group_name, user_names in group_users_dict.iteritems():
    <input type="radio" value="${group_name}" name="group_name"/>
    ${group_name}:
    % for user in user_names:
        <input type="checkbox" name="user_names" value="${user}"/>${user}
    %endfor
    </br>
%endfor
<input type="submit" value="Delete Users from Group" name="delete_group_users">
</form>
