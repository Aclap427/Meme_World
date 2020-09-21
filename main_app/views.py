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

def user_id(request, user_id):
  memes = Meme.objects.filter(user=user_id)
  return render(request, 'memes/user.html', {'memes': memes})


class MemeCreate(CreateView):
  model = Meme
  fields = ['photo_URL', 'top_text', 'bottom_text', 'text_color', 'font']
  success_url = '/memes/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MemeUpdate(LoginRequiredMixin, UpdateView):
  model = Meme
  fields = ['top_text', 'bottom_text', 'text_color', 'font']
  success_url = '/memes/user/'

  def form_valid(self,form):
    if form.instance.user == self.request.user:
      return super().form_valid(form)
    else:
      return redirect('/memes/user/')

class MemeDelete(DeleteView):
  model = Meme
  success_url = '/memes/'

  def form_valid(self,form):
    if form.instance.user != self.request.user:
      return redirect('/memes/')
  