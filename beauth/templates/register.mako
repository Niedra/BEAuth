<%inherit file="base.mako"/>

<%def name="title()">
    BEAuth - Register
</%def>

<h1>Register</h1>

<form method="POST" action="">
    <div>${ form.name.label }: ${ form.name() }</div>
    
    % if form.name.errors:
        <ul class="errors">
            % for error in form.name.errors:
                <li>${error}</li>
            % endfor
        </ul>
    % endif

    <div>${ form.password.label }: ${ form.password() }</div>
    
    % if form.password.errors:
        <ul class="errors">
            % for error in form.password.errors:
                <li>${error}</li>
            % endfor
        </ul>
    % endif

    <div>${ form.email.label }: ${ form.email() }</div>
    
    % if form.email.errors:
        <ul class="errors">
            % for error in form.email.errors:
                <li>${error}</li>
            % endfor
        </ul>
    % endif

    <div>${ form.accept_rules.label }: ${ form.accept_rules() }</div>
    
    % if form.accept_rules.errors:
        <ul class="errors">
            % for error in form.accept_rules.errors:
                <li>${error}</li>
            % endfor
        </ul>
    % endif

    <input type="submit" value="Submit" />
</form>
