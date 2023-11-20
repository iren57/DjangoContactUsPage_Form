from django.shortcuts import render, redirect
from .forms import UserForm
from .forms import Contactus


def contactus(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            contact = form.save()
            request.session['contact_id'] = contact.id
            return redirect('results')
    else:
            form = UserForm()
    return render(request, 'contact_us.html', {'form': form})


def results(request):
    contact_id = request.session.get('contact_id')
    if contact_id is not None:
        contact = Contactus.objects.get(id=contact_id)
        return render(request, 'results.html', {'contact': contact})
    else:
        return redirect('contact')
