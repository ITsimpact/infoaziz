
from django.utils.deprecation import MiddlewareMixin
from .models import PageHit, PageCounter
from django.db.models import F

class HitMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        xff = request.META.get("HTTP_X_FORWARDED_FOR")
        ip = xff.split(",")[0].strip() if xff else request.META.get("REMOTE_ADDR")

        PageHit.objects.create(
            path=request.path,
            ip=ip,
            user=request.user if request.user.is_authenticated else None,
            referer=request.META.get("HTTP_REFERER", ""),
            user_agent=request.META.get("HTTP_USER_AGENT", "")
        )
