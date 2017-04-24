from django.views import generic
from django.shortcuts import render,redirect
from .forms import *
from .models import Project,Song
from django.core.urlresolvers import reverse_lazy

class HomeView(generic.TemplateView):

    template_name = 'composer/home.html'

class RegistrationView(generic.TemplateView):

    form_class = UserForm
    template_name = 'composer/registration.html'

    def get(self,request):

        if request.user.is_authenticated :

            return redirect('composer:profile')

        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form })

    def post(self,request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form' : form })

class LoginView(generic.TemplateView):

    form_class = LoginForm
    template_name = 'composer/login.html'

    def get(self,request):

        if request.user.is_authenticated :

            return redirect('composer:home')

        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form })

    def post(self,request):

        form = self.form_class(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username,password=password)

            login(request, user)
            return redirect('composer:profile')

        else:

            return render(request, self.template_name, {'form': form })

class ProfileView(generic.TemplateView):

    template_name = 'composer/profile.html'

    def get(self, request):

        if not request.user.is_authenticated :

            return redirect('composer:home')

        return render(request,self.template_name)

class ProjectsView(generic.ListView):

    template_name = 'composer/projects.html'
    context_object_name = 'all_projects'

    def get_queryset(self):

        return Project.objects.filter(user=self.request.user)

class NewProjectView(generic.TemplateView):

    template_name = 'composer/projects/new.html'
    form_class = ProjectForm

    def get(self, request):

        if not request.user.is_authenticated :

            return redirect('composer:home')

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            project = form.save(commit=False)

            project.user = self.request.user

            project.save()

            return redirect('composer:projects')

        else:

            return render(request, self.template_name, {'form': form})

class CurrentProjectView(generic.CreateView):

    template_name = 'composer/project.html'
    form_class = SongForm

    def get_context_data(self, **kwargs):

        pk = self.kwargs['pk']

        project = Project.objects.get(pk=pk)

        kwargs['all_songs'] = Song.objects.filter(project=project)

        return super(CurrentProjectView,self).get_context_data(**kwargs)

    def post(self, request,pk):

        form = self.form_class(request.POST,request.FILES)

        project = Project.objects.get(pk=pk)

        if form.is_valid():

            song = form.save(commit=False)

            song.project = project

            project.no_of_songs += 1

            project.save()

            song.save()

            return redirect('composer:project',pk=pk)

        else:

            return render(request, self.template_name, {'form': form})

class SongDelete(generic.DeleteView):

    model = Song

    def get_success_url(self):
        project = self.object.project
        return reverse_lazy('composer:project',kwargs={'pk' : project.id})