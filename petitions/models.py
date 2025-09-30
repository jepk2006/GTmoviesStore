from django.db import models
from django.contrib.auth.models import User


class MoviePetition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.id} - {self.title}"
    
    def get_vote_count(self):
        return self.petitionvote_set.count()
    
    def has_user_voted(self, user):
        if not user.is_authenticated:
            return False
        return self.petitionvote_set.filter(user=user).exists()


class PetitionVote(models.Model):
    petition = models.ForeignKey(MoviePetition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('petition', 'user')  # Prevents duplicate votes
    
    def __str__(self):
        return f"{self.user.username} voted for {self.petition.title}"
