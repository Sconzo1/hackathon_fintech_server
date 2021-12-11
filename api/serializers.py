from rest_framework import serializers

from authentication.serializers import UserSerializer
from .models import *


class RequestCashTransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestCashTransactionType
        fields = '__all__'


class UserCashTransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCashTransactionType
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class CompanyAccountingSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = CompanyAccounting
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Request
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    request = RequestSerializer(read_only=True)

    class Meta:
        model = Coupon
        fields = '__all__'


class JamesSerializer(serializers.ModelSerializer):
    request = RequestSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = James
        fields = '__all__'


class LotSerializer(serializers.ModelSerializer):
    request = RequestSerializer(read_only=True)
    seller = UserSerializer(read_only=True)
    buyer = UserSerializer(read_only=True)

    class Meta:
        model = Lot
        fields = '__all__'


class RequestCashFlowSerializer(serializers.ModelSerializer):
    request = RequestSerializer(read_only=True)
    tx_type = RequestCashTransactionTypeSerializer(read_only=True)

    class Meta:
        model = RequestCashFlow
        fields = '__all__'


class UserCashFlowSerializer(serializers.ModelSerializer):
    request = RequestSerializer(read_only=True)
    tx_type = UserCashTransactionTypeSerializer(read_only=True)

    class Meta:
        model = UserCashFlow
        fields = '__all__'
