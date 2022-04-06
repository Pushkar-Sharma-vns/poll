from  django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
#from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question,Choice

# Create your views here.
class IndexView(generic.ListView):
    """latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #output=','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    
    #template=loader.get_template('polls/index.html')
    context={
        'latest_question_list':latest_question_list,
    }
    #return HttpResponse(template.render(context,request))
    This code loads the template called polls/index.html and passes it a 
    //context. The context is a dictionary mapping template variable names to
    //Python objects. 
    
    return render(request,'polls/index.html',context)
    """
    template_name='polls/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):
        #return frdt 5 questions
        return Question.objects.order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    """try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    #return HttpResponse("You're looking at question %s."%question_id)
    
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    """
    model=Question
    template_name='polls/deatil.html'

class ResultsView(generic.DetailView):
    """question=get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question':question})
    """
    model=Choice
    template_name='polls/results.html'

def vote(request,question_id):
    question=get_object_or_404(Question, pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        #re-dsplay the question voting form
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #always return an HttpResponseRedirect after successfully dealing with POST data.
        #This prevents data from being posted twice if a user hits the back button.
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
     



     