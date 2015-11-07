from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import BibliographyForm





def citecheckt_submitted(request):
    return render(request, 'citecheck/citecheck_submitted.html') 


def citecheckt_index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BibliographyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            bibliography = form.cleaned_data['bibliography']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'citecheck/citecheck_submitted.html', {'bibliography': bibliography})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BibliographyForm()

    return render(request, 'citecheck/citecheck_base.html', {'form': form})
