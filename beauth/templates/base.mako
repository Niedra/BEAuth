<!DOCTYPE html>
<head>
    <title>${self.title()}</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/login">Login</a>/<a href="/logout">Logout</a></li>
            <li><a href="/debug">Debug</a></li>
            <li><a href="/list">List Users</a></li>
            <li><a href="/register">Register</a></li>
    ${self.body()}
</body>
</html>
