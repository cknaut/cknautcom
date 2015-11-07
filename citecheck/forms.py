from django import forms

class BibliographyForm(forms.Form):
    bibliography = forms.CharField(label='', widget=forms.Textarea(attrs={'class' : 'bibliography_class'}))
