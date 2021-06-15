from django.shortcuts import render
from .models import Questions

from django.shortcuts import redirect
from .forms import NameForm

from .models import Questions
from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from .services import QuizResultService

# Create your views here.
def index(request):
    questions = Questions.objects.all()
    ids = questions.values_list('id',flat=True)
    data = min(ids)
    return render(request, 'main/index.html',{'data':data})



def end_result(request):
    questions = list(Questions.objects.all())

    dto_questions = []
    dto_answers = []
    for i in questions:
        true_answer = i.true_answer

        turple_true_ans=true_answer.rstrip().split(',')

        user_answer = []
        for ans in i.user_answer:
            if(ans =='A'):
                user_answer.append(str(i.id)+'-1')
            elif(ans == 'B'):
                user_answer.append(str(i.id)+'-2')
            elif (ans == 'C'):
                user_answer.append(str(i.id)+'-3')
            elif (ans == 'D'):
                user_answer.append(str(i.id)+'-4')


        user_ans = AnswerDTO(question_uuid=i.id, choices=user_answer)

        dto_choice1 = ChoiceDTO(uuid=(str(i.id)+'-1'), text= i.answer1, is_correct=(i.answer1 in turple_true_ans))
        dto_choice2 = ChoiceDTO(uuid=(str(i.id)+'-2'), text=i.answer2, is_correct=(i.answer2 in turple_true_ans))
        dto_choice3 = ChoiceDTO(uuid=(str(i.id)+'-3'), text=i.answer3, is_correct=(i.answer3 in turple_true_ans))
        dto_choice4 = ChoiceDTO(uuid=(str(i.id)+'-4'), text=i.answer4, is_correct=(i.answer4 in turple_true_ans))
        choices =[]
        choices.append(dto_choice1)
        choices.append(dto_choice2)
        choices.append(dto_choice3)
        choices.append(dto_choice4)


        dto_question = QuestionDTO(choices=choices, text= i.question, uuid=i.id)

        dto_questions.append(dto_question)
        dto_answers.append(user_ans)


    quiz = QuizDTO('1','QUUIIIZZ',dto_questions)
    answers = AnswersDTO('1',dto_answers)

    quiz_result = QuizResultService(quiz,answers)

    data = quiz_result.get_result()




    return render(request, 'main/end.html',{'data':data})




def get_result(request,pk):
    questions = Questions.objects.filter(id=pk)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)

        # check whether it's valid:

        ans1 = request.POST.getlist('choice_field1')
        questions.update(user_answer = ''.join(ans1))


        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        maxid =max(Questions.objects.values_list('id', flat=True))
        if(pk!=maxid):

            return redirect('questions_detail', pk=pk+1)
        else:
            return redirect('endpage')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()



    return render(request, 'main/about.html', {'form': form, 'quest':questions.values().get()})