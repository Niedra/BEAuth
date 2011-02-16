<%inherit file="base.mako"/>

<%def name="title()">
    BEAuth - List
</%def>

<h2>List</h2>

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

<p class="pagelist">${currentPage.pager(format='$link_first $link_previous ~3~ $link_next $link_last:', symbol_previous='<')}</p>