from django import forms
from .models import Chatbot

class ChatCreateForm(forms.ModelForm):
	class Meta:
		model = Chatbot
		#text = forms.CharField(label='コマンド', widget=forms.Textarea)
		fields = '__all__'
		widgets = {
			'comment': forms.Textarea(attrs={'class': 'textarea'})
		}
