from django.shortcuts import render
from django import views
from django.http.response import JsonResponse
from .forms import ApplicationForm
from .models import JobApplication
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

class HomeView(views.View):
    def get(self,request):
        form = ApplicationForm()
        return render(request,"application_form.html",{"form":form})

    def post(self,request):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            print("valid")
            return render(request,"application_form.html",{"success":True})
        print(form.errors)
        return render(request,"application_form.html",{"form":form,"success":False})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('job_application:home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class ApplicantListView(LoginRequiredMixin,PermissionRequiredMixin,views.generic.ListView):
    model = JobApplication
    # queryset = JobApplication.objects.all().order_by("email","-application_date").distinct("email")
    context_object_name = "applicants"
    template_name = "applicants_list.html"

    def has_permission(self):
        return self.request.user.is_superuser

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        queryset = JobApplication.objects.all().order_by("email","-application_date","id").distinct("email")
        if self.request.GET.get("q"):
            queryset = JobApplication.objects.search_term(self.request.GET.get("q")).distinct("email")
        # for obj in qs:
        #     queryset = queryset.filter(email=obj)
        context['applicants'] = queryset
        return context

class SaveNotes(views.View):
    def post(self,request,pk):
        applicant = JobApplication.objects.get(pk=pk)
        applicant.notes = request.POST.get("notes")
        applicant.save()
        return JsonResponse({"success":True})
