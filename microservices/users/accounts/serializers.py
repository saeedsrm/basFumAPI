from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from accounts.models import Account


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['id']=user.id
        token['email']=user.email
        return token
# for check the access token data you can decode it in https://token.dev/

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'password',)


class ShowMyInformationsSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('picrure', 'first_name', 'last_name', 'phone_number', 'State', 'city', 'address', 'National_Code',
                  'Student_Number', 'email', 'Score')
