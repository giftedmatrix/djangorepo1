from django.shortcuts import render,redirect
from django.views import View
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile, CustomUser, Movie, Video

user=CustomUser()

class IndexPage(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')

class Home(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('core:profile_list')
        return render(request,'home.html')


@method_decorator(login_required, name="dispatch")
class ProfileList(View):
    def get(self,request, *args, **kwargs):
        profiles=request.user.profiles.all()
        
        context={
            "profiles":profiles,

        }
        return render(request,'profiles.html',context)


@method_decorator(login_required, name="dispatch")
class CreateProfile(View):
    def get(self,request,*args,**kwargs):
        form=ProfileForm()
        return render(request,'profile_create.html',{'form':form})

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            form=ProfileForm(request.POST or None)
            if form.is_valid() and request.user.is_authenticated:
                profiles=Profile.objects.create(**form.cleaned_data)
                context={
                    'form':form
                }
                if request.user.is_authenticated:
                    request.user.profiles.add(profiles)
                    return redirect('core:profile_list')
        return render(request,'profile_create.html',context)


@method_decorator(login_required, name="dispatch")
class MoviesList(View):
    def get(self,request,profile_id,*args,**kwargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)
            movies=Movie.objects.filter(age_limit=profile.age_limit)
            videos = Video.objects.all()
            showcase = movies[0]
            film = videos[2]
            context={'movies':movies , 'showcase':showcase, 'film':film}
            if profile not in request.user.profiles.all():
                return redirect('core:profile_list')
            return render(request,'movies_list.html',context)
        except Profile.DoesNotExist:
            return redirect('core:profile_list')


@method_decorator(login_required, name="dispatch")
class MovieDetails(View):
    def get(self,request,movie_id,*args,**kwargs):
        try:
            movie=Movie.objects.get(uuid=movie_id)
            videos = Video.objects.all()
            context={'movie':movie, 'videos':videos}
            return render(request,'movie_details.html',context)
        except Movie.DoesNotExist:
            return redirect('core:profile_list')

