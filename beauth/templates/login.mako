<%inherit file="base.mako"/>

<%def name="title()">
    BEAuth - Login
</%def>

<h1>Login</h1>

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
