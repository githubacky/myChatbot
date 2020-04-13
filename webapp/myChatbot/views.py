from django.shortcuts import render, redirect
from django.views import generic
from .models import Chatbot
from .forms import ChatCreateForm
from django.urls import reverse_lazy

# Create your views here.
#def mychatbot_list(request):
def command_create(request):
	command = ChatCreateForm(request.POST or None)
	if request.method == 'POST' and command.is_valid():
		command.save()
		comment = command.cleaned_data.get('comment')
		return redirect('myChatbot:command_create')

	context = {
		'command': command,
		#'comment': request.POST.get('comment'),
	}
	return render(request, 'myChatbot/index.html', context)

class CommandCreate(generic.CreateView):
	model = Chatbot
	form_class = ChatCreateForm
	success_url = reverse_lazy('')

	def form_valid(self, form):
		comment = form.save(commit=False)
		comment.save()
		return redirect('myChatbot:command_create')
