<h2>Services Manager</h2>

<form action="${request.path}" method="post">
    service name (unique): <input type="text" value="" name="service_name" placeholder="emu">
    </br>
    service url: <input type="text" value="" name="service_url" placeholder="http://localhost:8093">
    </br>
    service type:
    %for service_type in service_types:
        <input type="radio" name="service_type" value="${service_type}"> ${service_type}
    %endfor
    </br>
    <input type="submit" value="register" name="register">
</form>

<h3>Service List</h3>
%for service in service_info_list:
    ${service['service_name']}, ${service['service_type']}, ${service['service_url']}
    </br>
%endfor

<h3>Delete Service</h3>
<form action="${request.path}" method="post">
%for service in service_info_list:
    <input type="checkbox" value="${service['service_name']}" name="service_names">${service['service_name']}
    </br>
%endfor
<input type="submit" value="unregister" name="unregister">
</form>