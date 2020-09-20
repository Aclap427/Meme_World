from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Meme
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

def home(request):
  return render(request, 'home.html')

@login_required
def memes_index(request):
  memes = Meme.objects.all()
  return render(request, 'memes/index.html', {'memes': memes})
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def user_view(request):
  memes = Meme.objects.filter(user=request.user)
  return render(request, 'memes/user.html', {'memes': memes})

class MemeCreate(CreateView):
  model = Meme
  fields = ['photo_URL', 'top_text', 'bottom_text']
  success_url = '/memes/'

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)

