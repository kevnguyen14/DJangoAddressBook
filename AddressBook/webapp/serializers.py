from rest_framework import serializers
from . models import Contact

# Create new class for each model class, these new serialized classes will contain only json data that you want to return on a request
class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        # return only selected field properties
        #fields = ('first_name', 'last_name', 'street')
        # returns all field properties of Contact
        fields = "__all__"
