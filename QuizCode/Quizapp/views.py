from django.shortcuts import render ,get_object_or_404 , redirect
from Quizapp.models import Subject , Question
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request,"home.html")

def subject_list(request):
    subjects = Subject.objects.all()
    
    return render(request,'subject_list.html',{'subjects':subjects})

def quiz(request,subject_id):
    subject  = get_object_or_404(Subject,pk=subject_id)
    # subject = c
    questions = Question.objects.filter(subject=subject)
    hint = subject.q_hint_text
    # ------- Testing Purpose only -------
    # print(subject.id)
    # print(subject.name)
    # print(subject.q_hint_text)
    # -------------------------------------
    

    if request.method == "POST":
        score = 0
        total = questions.count()
        url_WA_shraing = request.build_absolute_uri(f"/quiz/{subject_id}")
        
        for i in questions:
            selected = request.POST.get(str(i.id))
            if selected and int(selected) == i.correct_option:
                score+=1
            if score<total/2:
                msg = "Don't worry, you'll do better next time! 💪"
            elif score>=total/2:
                msg = "Champion! Keep up the great work! 🏅<br>New adventures await!🤜🤛"
        try:
          return render(request,'result.html',{'score':score,'total':total,'retry':subject.id,"msg":msg,"url_WA_shraing":url_WA_shraing})
        except Exception as e :
          return redirect('invalid_url', xyz='quiz_error')
    
    return render(request,'quiz.html',{'sub':subject,'ques':questions,'hint':hint})


def add_new_question(request):
    all_sub = Subject.objects.all()
    if request.method == 'POST':
        q_name = request.POST.get('sub_name')
        sub_instance = Subject.objects.get(name=q_name)
        q_text = request.POST.get('q_text')
        option1 = request.POST.get('opt1')
        option2 = request.POST.get('opt2')
        option3 = request.POST.get('opt3')
        option4 = request.POST.get('opt4')
        correct_option = request.POST.get('correct_option')
      
        try:
            new_ques = Question(subject=sub_instance,
                            question_text=q_text,
                            option1=option1,
                            option2=option2,
                            option3=option3,
                            option4=option4,
                            correct_option=correct_option)
            
            if new_ques:
                new_ques.save()
                messages.success(request,'Question Added Successfully ')
                return redirect('add_new_question') #it must match to url name
        except Exception as e:
            messages.warning(request,f'ERROR SPOTED {e}')
            
        
        
    
    return render(request,'new_question.html',{'all_sub':all_sub})

def add_new_subject(request):
    all_sub = Subject.objects.all()
    if request.method == 'POST':
        sub = request.POST.get('subname')
        subhint = request.POST.get('subhint')
        
        if sub:
            new_subject = Subject(name=sub,q_hint_text=subhint)
            new_subject.save()
            messages.success(request,'Topic Added Successfully please Add Some Qustions')
            return redirect('add_new_subject') #it must match to url name
        
        
    return render(request,'new_subject.html',{'all_sub':all_sub})

def delete_subject(request,del_id):
    del_sub = get_object_or_404(Subject,pk=del_id)
    del_sub.delete()
    
    
    return redirect('add_new_subject') #it must match to url name

def invalid_url(request, xyz):
    
    return HttpResponse("""
SORRY THERE IS <br> ERROR                        """)


