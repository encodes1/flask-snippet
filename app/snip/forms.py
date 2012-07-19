from flask.ext.wtf import Form, TextField, TextAreaField, PasswordField, BooleanField, RecaptchaField, SelectField
from flask.ext.wtf import Required, Email, EqualTo


class snipForm(Form):
    name = TextField('Name', [Required()])
    code = TextAreaField('Code', [Required()])


class TransactionForm(Form):
    name = TextField('NickName', [Required()])
    frequency = SelectField('Frequency', choices=[("Monthy", "Monthly"), ("weekly", "weekly"), ("annual", "annual")])
