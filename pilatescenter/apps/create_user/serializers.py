from rest_framework.serializers import  ModelSerializer
from .models import CustomUser



class CustomUserSeliazer(ModelSerializer):
		class Meta:
			model 	= CustomUser
			fields 	= (
							'username',
							'first_name',
							'last_name',
						)


