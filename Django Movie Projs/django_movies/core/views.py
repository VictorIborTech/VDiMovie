from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile
from .models import Movie


from .form import ProfileForm


# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:profile_list')
        return render(request, 'index.html')
    

@method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profile.all()

        context ={
            'profiles' : profiles
        }
        return render(request, 'profileList.html', context)
    
@method_decorator(login_required, name='dispatch')
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        # Create Profile Form
        form = ProfileForm()

        context ={
            form : 'form'
        }
        return render(request, 'profileCreate.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)

        context ={
            form : 'form'
        }

        if form.is_valid():
           profile = Profile.objects.create(**form.cleaned_data)
           if profile:
               request.user.profile.add(profile)
               return redirect('core:profile_list')

        return render(request, 'profileCreate.html', context)
    

@method_decorator(login_required, name='dispatch')
class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid = profile_id)
            movies = Movie.objects.filter(age_limit = profile.age_limit)

            try:
                showcase = movies[0]
            except:
                showcase = None

            context ={
                'movies' : movies,
                'showcase' : showcase
            }

            if profile not in request.user.profile.all():
                return redirect('core:profile_list')
            
            return render(request, 'movieList.html', context)
        
        except Profile.DoesNotExist:
            return redirect('core:profile_list')
            

@method_decorator(login_required, name='dispatch')
class ShowMovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid= movie_id)

            context ={
                'movie' : movie
            }

            return render(request, 'movieDetail.html', context)
        except Movie.DoesNotExist:
            return render('core:movies_list')


@method_decorator(login_required, name='dispatch')
class ShowMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid= movie_id)
            movie = movie.videos.values()

            context = {
                'movie' : list(movie)
            }
            
            return render(request, 'showMovie.html', context)



        except Movie.DoesNotExist:
            return render('core:movies_list')
            


            
