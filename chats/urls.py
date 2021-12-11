from rest_framework import routers

from chats.views import ChatView, MessageView

router = routers.DefaultRouter()

router.register(r'msg', MessageView)
router.register(r'', ChatView)

urlpatterns = router.urls
