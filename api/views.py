from rest_framework import viewsets

from .serializers import *


class UserCashTransactionTypeView(viewsets.ModelViewSet):
    queryset = UserCashTransactionType.objects.all()
    serializer_class = UserCashTransactionTypeSerializer


class RequestCashTransactionTypeView(viewsets.ModelViewSet):
    queryset = RequestCashTransactionType.objects.all()
    serializer_class = RequestCashTransactionTypeSerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyAccountingView(viewsets.ModelViewSet):
    queryset = CompanyAccounting.objects.all()
    serializer_class = CompanyAccountingSerializer


class RequestView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer


class CouponView(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class JamesView(viewsets.ModelViewSet):
    queryset = James.objects.all()
    serializer_class = JamesSerializer


class LotView(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class RequestCashFlowView(viewsets.ModelViewSet):
    queryset = RequestCashFlow.objects.all()
    serializer_class = RequestCashFlowSerializer


class UserCashFlowView(viewsets.ModelViewSet):
    queryset = UserCashFlow.objects.all()
    serializer_class = UserCashFlowSerializer
