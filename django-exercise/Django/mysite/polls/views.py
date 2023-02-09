from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from .models import Question,Choice,Vote
from django.views import generic
from django.utils import timezone
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib  import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

arr_id = []

class IndexView(LoginRequiredMixin,generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(LoginRequiredMixin,generic.DetailView):
    model  = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(LoginRequiredMixin,generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def vote(request, question_id):
#     #return HttpResponse("You're voting on question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
    
    
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#         if question.id not in arr_id:
#             arr_id.append(question.id)
#         print(arr_id)
#         if len(arr_id)>=3:
#             handle_vote_submission(request=request)

#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         #return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            Vote.objects.get(question=question, voter=request.user)
        except Vote.DoesNotExist:
            selected_choice.votes += 1
            selected_choice.save()
            arr_id.append(selected_choice)
            
            Vote.objects.create(question=question, answer=selected_choice, user=request.user,voter=request.user)
        else:
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You have already voted on this question.",
            })
    print(arr_id)
    if len(arr_id)>=3:
        handle_vote_submission(request=request)
    return redirect('polls:results', question_id)



def send_thanks_email(user_id):
    user = User.objects.get(id=user_id)
    subject = 'Thanks for voting'
    message = 'Thanks for submitting a vote for more than three questions!'
    from_email = 'karan.b@auberginesolutions.com'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration successful.")
            return redirect("login")
        messages.error(request,'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request=request,template_name="polls/register.html",context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}.")
                return redirect("polls:index")
            else:
                messages.error(request,"Invalid username or password.")
        
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,template_name='polls/login.html',context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def handle_vote_submission(request):
    
    if len(arr_id)>=3:
        send_thanks_email(request.user.id)
        print("mail done.....")

if __name__ == "__main__":
    handle_vote_submission()