from django.contrib import admin
from .models import MoviePetition, PetitionVote


@admin.register(MoviePetition)
class MoviePetitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at', 'is_active', 'get_vote_count']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description', 'created_by__username']
    readonly_fields = ['created_at']


@admin.register(PetitionVote)
class PetitionVoteAdmin(admin.ModelAdmin):
    list_display = ['petition', 'user', 'voted_at']
    list_filter = ['voted_at']
    search_fields = ['petition__title', 'user__username']
