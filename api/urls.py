from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()
router.register(r'user_cash_tx_types', UserCashTransactionTypeView)
router.register(r'request_cash_tx_types', RequestCashTransactionTypeView)
router.register(r'companies', CompanyView)
router.register(r'accounting', CompanyAccountingView)
router.register(r'requests', RequestView)
router.register(r'coupons', CouponView)
router.register(r'james', JamesView)
router.register(r'lots', LotView)
router.register(r'user_cash_flow', UserCashFlowView)
router.register(r'request_cash_flow', RequestCashFlowView)

urlpatterns = router.urls
