from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MoviePetition, PetitionVote


def index(request):
    petitions = MoviePetition.objects.filter(is_active=True).order_by('-created_at')
    template_data = {
        'title': 'Movie Petitions',
        'petitions': petitions
    }
    return render(request, 'petitions/index.html', {'template_data': template_data})


@login_required
def create(request):
    template_data = {'title': 'Create Movie Petition'}
    
    if request.method == 'GET':
        return render(request, 'petitions/create.html', {'template_data': template_data})
    
    elif request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        
        if not title or not description:
            template_data['error'] = 'Please fill in both title and description.'
            template_data['title_value'] = title
            template_data['description_value'] = description
            return render(request, 'petitions/create.html', {'template_data': template_data})
        
        petition = MoviePetition.objects.create(
            title=title,
            description=description,
            created_by=request.user
        )
        messages.success(request, 'Your movie petition has been created successfully!')
        return redirect('petitions.show', id=petition.id)


def show(request, id):
    petition = get_object_or_404(MoviePetition, id=id)
    template_data = {
        'title': petition.title,
        'petition': petition,
        'vote_count': petition.get_vote_count(),
        'user_has_voted': petition.has_user_voted(request.user)
    }
    return render(request, 'petitions/show.html', {'template_data': template_data})


@login_required
def vote(request, id):
    if request.method != 'POST':
        return redirect('petitions.show', id=id)
    
    petition = get_object_or_404(MoviePetition, id=id)
    
    # Check if user already voted
    if petition.has_user_voted(request.user):
        messages.warning(request, 'You have already voted on this petition.')
        return redirect('petitions.show', id=id)
    
    # Create the vote
    PetitionVote.objects.create(petition=petition, user=request.user)
    messages.success(request, 'Your vote has been recorded!')
    return redirect('petitions.show', id=id)
