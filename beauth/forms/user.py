from wtforms import Form, BooleanField, PasswordField, SubmitField, TextField, validators

class RegistrationForm(Form):
    name         = TextField(u'Username', [validators.Length(min=4, max=25)])
    password     = PasswordField(u'Password', [validators.Length(min=4, max=25)])
    email        = TextField(u'Email Address', [validators.Length(min=6, max=35),
                                                validators.Email()])
    accept_rules = BooleanField(u'I accept the site rules', [validators.Required()])

class LoginForm(Form):
    name         = TextField(u'Username', [validators.Length(min=4, max=25)])
    password     = PasswordField(u'Password', [validators.Length(min=4, max=25)])
    submit       = SubmitField(u'Submit')

class SearchForm(Form):
    name         = TextField(u'Username', [validators.Length(min=3, max=25)])
    submit       = SubmitField(u'Submit')

class EditForm(Form):
    password     = PasswordField(u'Password', [validators.Length(min=4, max=25)])
    email        = TextField(u'Email Address', [validators.Length(min=6, max=35),
                                                validators.Email()])
