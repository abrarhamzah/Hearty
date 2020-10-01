from django import forms

class PatientForm(forms.Form):
  typical_chest_pain = forms.ChoiceField(choices = [(1,'Yes'), (0,'No')])
  age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient age'}))
  dm = forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  ht = forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  fh = forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  tg = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient TG'}))
  k = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient K'}))
  region_rwma = forms.ChoiceField(choices=[(0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4')])
  bbb = forms.ChoiceField(choices=[(0,'Yes'), (1,'No')])
  tinversion = forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  fbs = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient FBS'}))
  esr = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient ESR'}))
  ef_tte = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter patient EF-TTE'}))
  dlp = forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])
  diastolic_murmur = forms.ChoiceField(choices=[(1,'Yes'), (0,'No')])


