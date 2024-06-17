from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer

bot = ChatBot('chatbot',read_only=False,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation",
                  {
                      'import_path':'chatterbot.logic.BestMatch'
                    #   'default_response':'Sorry, I dont know what that means',
                    #   'maximum_similarity_threshold':0.90
                   }
                   ])

list_to_train = [
    "hi", #question
    "hi, there", #answer
    "What's your name",
    "Im just a chatbot",
    "What is your fav food",
    "I like cheese"
]

trainer = ChatterBotCorpusTrainer(bot)

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)

trainer.train("chatterbot.corpus.english")

def index(request):
    return render(request,'myapp/index.html')


def specific(request):

    return HttpResponse("This is the specific url")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))

    return HttpResponse(chatResponse)