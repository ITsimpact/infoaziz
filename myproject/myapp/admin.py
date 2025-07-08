from django.contrib import admin
from .models import PageHit
import user_agents


@admin.register(PageHit)
class PageHitAdmin(admin.ModelAdmin):
    list_display = ('path', 'ip', 'user', 'device', 'browser', 'os', 'created')
    list_filter = ('path', 'user', 'ip', 'created')

    def device(self, obj):
        ua = user_agents.parse(obj.user_agent or "")
        return "Mobile" if ua.is_mobile else "PC" if ua.is_pc else "Other"

    def browser(self, obj):
        ua = user_agents.parse(obj.user_agent or "")
        return ua.browser.family

    def os(self, obj):
        ua = user_agents.parse(obj.user_agent or "")
        return ua.os.family
