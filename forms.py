from wtforms import Form
from wtforms import SearchField, TextAreaField, RadioField, StringField, SelectField,DecimalField

class UserForm(Form):
    x1=DecimalField("x1")
    y1=DecimalField("y1")
    x2=DecimalField("x2")
    y2=DecimalField("y2")

class ResistenciaForm(Form):
    banda1=SelectField("Color 1", choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'), ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde'), ('Azul', 'Azul'), ('Violeta', 'Violeta'), ('Gris', 'Gris'), ('Blanco', 'Blanco')])
    banda2=SelectField("Color 2", choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'), ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde'), ('Azul', 'Azul'), ('Violeta', 'Violeta'), ('Gris', 'Gris'), ('Blanco', 'Blanco')])
    banda3=SelectField("Color 3", choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'), ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde'), ('Azul', 'Azul'), ('Violeta', 'Violeta'), ('Gris', 'Gris'), ('Blanco', 'Blanco')])
    resColor=RadioField("", choices=[('Oro', 'Oro'), ('Plata', 'Plata')], default='Oro')

