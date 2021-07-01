from rest_framework import serializers
from core.models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields =['Isbn','nombre','autor','descripcion','categoria']
