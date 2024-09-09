from django.shortcuts import render
from .models import Preamble, FundamentalRights, FundamentalDuties, DirectivePrinciples

# Home Page View
def index(request):
  return render(request, 'samvidhan/index.html')

def about(request):
    return render(request, 'samvidhan/about.html')

def games(request):
    return render(request, 'samvidhan/games.html')

def quiz(request):
    return render(request, 'samvidhan/quiz.html')

def interactive_learning(request):
    return render(request, 'samvidhan/learning.html')

def preamble(request):
    preamble = Preamble.objects.first()  # Fetch the first instance or adjust as needed
    return render(request, 'samvidhan/preamble.html', {'preamble': preamble})

def fundamental_rights(request):
    rights = FundamentalRights.objects.all()  # Fetch all instances of Fundamental Rights
    return render(request, 'samvidhan/fundamental_rights.html', {'rights': rights})

def fundamental_duties(request):
    duties = FundamentalDuties.objects.all()  # Fetch all Fundamental Duties from the database
    return render(request, 'samvidhan/fundamental_duties.html', {'duties': duties})

def directive_principles(request):
    principles = DirectivePrinciples.objects.all()  # Fetch all Directive Principles from the database
    return render(request, 'samvidhan/directive_principles.html', {'principles': principles})