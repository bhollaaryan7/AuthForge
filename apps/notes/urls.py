from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

router = DefaultRouter()

# IMPORTANT: empty prefix here
router.register(r"", NoteViewSet, basename="notes")

urlpatterns = router.urls
