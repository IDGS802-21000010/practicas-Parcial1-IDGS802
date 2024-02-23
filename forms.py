from wtforms import Form
from wtforms import SearchField, TextAreaField, RadioField, StringField, SelectField,DecimalField
from wtforms import EmailField
from wtforms import validators

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

class DiccionarioForm(Form):
    en=StringField('Ingles', [validators.DataRequired('El campo es requerido'),
                              validators.length(min=1, max=10, message='Ingrese palabra valida')
    ])
    es=StringField('Español', [validators.DataRequired('El campo es requerido'),
                              validators.length(min=1, max=10, message='Ingrese palabra valida')
    ])
    idioma=RadioField('Consulta', choices=[('Ingles', 'Ingles'),('Español','Español')])
    pal=StringField('Palabra', [validators.DataRequired('El campo es requerido'),
                              validators.length(min=1, max=10, message='Ingrese palabra valida')
    ])