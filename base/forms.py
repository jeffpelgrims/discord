from django.forms import ModelForm
from .models import Room

# Création automatique du formulaire pour ajouter une room sur le site
class RoomForm(ModelForm):
    class Meta:
        # On définit le nom du modèle, ensuite les champs que l'on veut afficher
        model = Room
        fields = '__all__'