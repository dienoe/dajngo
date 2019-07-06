from rest_framework import serializers
from users.models import User
class QAuthQQUserSerializer(serializers.ModelSerializer):
    sms_code = serializers.CharField(label='短信验证码',write_only=True)
    access_token = serializers.CharField(label='操作凭证',write_only=True)
    token=serializers.CharField(read_only=True)
    mobile = serializers.RegexField(label='手机号', regex=r'^1[3-9]\d{9}$')
    # password = serializers.CharField(label='密码', max_length=20, min_length=8)

    class Meta:
        model=User
        firlds=('mobile','password','sms_code','access_token','id','username','token')
        extra_kwargs={
            'username':{
              'read_only':True
            },
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许8-20个字符的密码',
                    'max_length': '仅允许8-20个字符的密码',
                }
            }
        }
        # 校验数据
        def valiadte_access_token(self):
            pass
        def validate(self,attrs):
            return attrs
        def create(self,validated_data):
            pass
        # 判断用户是否存在
        # 如果存在，绑定　创建OAuthQQUser数据
        # 如果不存在,先创建User,创建OAuthQQUser数据
        # 签发JWT_token