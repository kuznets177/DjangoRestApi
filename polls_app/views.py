from django.shortcuts import render
from .models import PollsDB, Questions, Answers
from .utils import get_client_ip

# Create your views here.

# главная страница
def index(request):
    lists={'polls_db': PollsDB.name_poll,
           'question_text': Questions.question_text,
           'answer_text': Answers.answer_text,
           'client_ip': get_client_ip,
           }
    return render( request, 'index.html', lists )



