from django.contrib import admin
from .models import LoginLevel, UserLogin, Selecao


class detDefault(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10


admin.site.register(LoginLevel, detDefault)
admin.site.register(UserLogin, detDefault)
admin.site.register(Selecao, detDefault)
