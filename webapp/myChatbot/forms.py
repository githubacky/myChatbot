from django import forms
from .models import Chatbot

class ChatCreateForm(forms.Form):
	class Meta:
		model = Chatbot
		text = forms.CharField(label='コマンド', widget=forms.Textarea)
		#fields = '__all__'
