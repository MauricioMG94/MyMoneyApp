from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100, verbose_name="Nombre completo", validators=
                                 [MinLengthValidator(6, "El nombre debe tener al menos 6 caracteres.")])
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name="Correo electrónico",
        validators=[EmailValidator("El correo proporcionado no es válido."),
                    MinLengthValidator(6, "El nombre debe tener al menos 6 caracteres.")]
    )
    password = models.CharField(
        max_length=20,
        verbose_name="Contraseña",
        validators=[MinLengthValidator(8, "La contraseña debe tener al menos 8 caracteres."), 
                    MaxLengthValidator(12, "La contraseña no puede tener más de 12 caracteres")]
    )
    
    def __str__(self):
        return str(self.email)