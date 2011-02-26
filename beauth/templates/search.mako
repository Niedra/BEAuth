<%inherit file="base.mako"/>

<%def name="title()">
    BEAuth - Search
</%def>

<h1>Search</h1>

<form method="POST" action="">
% for field in form:
<div>${ field.label} : ${ field } </div>

    % if field.errors:
        <ul class="errors">
            % for error in field.errors:
                <li>${error}</li>
            % endfor
        </ul>
    % endif

% endfor
</form>

% if users:
<table>
    <tr>
        <th>ID</th>
        <th>Name</th>
    </tr>
    % for user in users:
        <tr>
            <td>${user.id}</td>
            <td><a href="/${user.name}">${user.name}</a></td>
        </tr>
    % endfor
</table>
% else:
<p>Sorry, no users found.</p>
% endif
