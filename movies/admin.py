from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'user', 'comment_preview', 'date']
    list_filter = ['date', 'movie']
    search_fields = ['comment', 'user__username', 'movie__name']
    ordering = ['-date']
    
    def comment_preview(self, obj):
        return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
    comment_preview.short_description = 'Comment Preview'

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
