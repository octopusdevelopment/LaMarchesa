from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

from livraison.models import Wilaya, Commune



class WilayaSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Wilaya)

    class Meta:
        model = Wilaya
        fields = ('id', 'translations')



class CommuneSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Commune)

    class Meta:
        model = Commune
        fields = ('id', 'Wilaya', 'translations')