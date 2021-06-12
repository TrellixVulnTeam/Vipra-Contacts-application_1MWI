from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Contact
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

def home(request):
    context = {'contacts': Contact.objects.all(),'title': 'Home'}
    return render(request, 'contacts/home.html', context)
# Create your views here.
def DetailView(request,pk):
    contact = get_object_or_404(Contact,id=pk)
    context = {'contact':contact, 'title': contact}
    print(context)
    return render(request,'contacts/details.html',context)

class ContactCreateView(CreateView):
    model = Contact
    fields = ['name','email','Number']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['name','email','Number']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author:
            return True
        else:
            return False

class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.author:
            return True
        return False