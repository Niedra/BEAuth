<%inherit file="base.mako"/>

<%def name="title()">
    BEAuth - View ${ user.name }
</%def>

<ul>
    <li><strong>Name:</strong> ${ user.name }</li>
    <li><strong>Password:</strong> ${ user.password }</li>
    <li><strong>Email:</strong> ${ user.email }</li>
</ul>
