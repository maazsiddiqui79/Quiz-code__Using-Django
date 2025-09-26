from django.shortcuts import render ,get_object_or_404 , redirect
from Quizapp.models import Subject ,Question
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
    questions = Question.objects.filter(subject=subject)
    

    if request.method == "POST":
        score = 0
        total = questions.count()
        for i in questions:
            selected = request.POST.get(str(i.id))
            if selected and int(selected) == i.correct_option:
                score+=1
            if score<total/2:
                msg = "Don't worry, you'll do better next time! 💪"
            elif score>=total/2:
                msg = "Champion! Keep up the great work! 🏅<br> New adventures await!🤜🤛"
        try:
          return render(request,'result.html',{'score':score,'total':total,'retry':subject.id,"msg":msg})
        except Exception as e :
          return redirect('invalid_url', xyz='quiz_error')
    
    return render(request,'quiz.html',{'sub':subject,'ques':questions})


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
        
        if sub:
            new_subject = Subject(name=sub)
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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr"
      crossorigin="anonymous"
    />
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q"
      crossorigin="anonymous"
    ></script>

  <title>Page Not Found</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(270deg, #ee097868, #06beb56e, #48b1bf81);
      background-size: 800% 800%;
      animation: gradientMove 12s ease infinite;
    }

    @keyframes gradientMove {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    .error-card {
      background: rgba(255, 255, 255, 0.9);
      padding: 50px;
      border-radius: 20px;
      box-shadow: 5px 5px 20px 5px rgba(0,0,0,0.29);
      text-align: center;
      max-width: 500px;
      transition: all 0.3s ease-in-out;
    }

    .error-card:hover {
      transform: translateY(-5px);
      box-shadow: 5px 5px 25px 5px rgba(0,0,0,0.4);
    }

    .error-card h1 {
      font-size: 80px;
      margin-bottom: 10px;
      color:cornflowerblue;
      
    }

    .error-card h2 {
      margin: 10px 0;
      color: #333;
    }

    .error-card p {
      font-size: 18px;
      margin: 10px 0 20px 0;
      color: #555;
    }

    .mybtn:hover {
    box-shadow: 5px 5px 20px 5px rgba(0, 0, 0, 0.29);
    background-color: antiquewhite;
    color: black;
    transform: translatey(-5px);
  }

  .mybtn {
    transition: all 0.3s ease;
  }

  </style>
</head>
<body>
  <div class="error-card">
    <h1>404</h1>
    <h2>Oops!</h2>
    <p> You are trying to access a URL that does not exist or has never been created.</p>
    <a href="/" class="mybtn btn btn-light btn-dark mt-auto">Go to Home Page</a>
</div>

</body>
</html>
   
                        """)


