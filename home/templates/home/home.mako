<h3>Welcome to Magpie</h3>

<button type="button" onclick="location.href='./login'">Sign In!</button>

%if user_name:
<p>You are logged in as: ${ user_name }</p>
<form action="http://localhost:8000/signout" method="post">
    <!-- "came_from", "password" and "login" can all be overwritten -->
    <input type="hidden" value="${request.path_url}" name="came_from" id="came_from">
    <input type="submit" value="Sign Out" name="signout" id="submit">
</form>
% else:
<p>You are not logged in!</p>
% endif