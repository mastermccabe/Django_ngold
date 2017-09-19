from django.shortcuts import render, HttpResponse, redirect
import re
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random, string, math
import datetime


def index(request):
    if 'gold' not in request.session:

        request.session['gold'] = 0
        request.session['activity'] = []
        # gold = request.session['gold']

    else:
        # print request.session['counter']
        request.session['gold'] = request.session['gold']

    return render(request,'ninjagold/index.html')

def reset(request):
    request.session['gold'] = 0
    request.session['activity']=[]
    request.session['DateTime'] = ''
    return redirect('/ninjagold')

def activity(request):
    #  DateTime =
    #  request.session['time']= datetime.datetime.now()
    #  request.session['date']= DateTime
     activity = request.session['activity']
     request.session['activity']
    #  .append(request.session['activity'])
     print request.session['activity']
    #  request.session['acvitity']+=('Earned',request.session['gold'],' gold from the',hiddenVal,'! @Time:' ,datetime.now().strftime("%Y/%m/%d %I:%M %p"))
    #  if (loc == 'farm' or loc == 'cave' or loc == 'house' or loc == 'casino' and winLose == 0):
    #     #  request.session['activity'].append("working")
    #      request.session['activity'].append('Earned {} gold from the {}! @Time: {}'.format(value, loc, DateTime))
    #  elif (loc == 'casino' and winLose == 1):
    #      request.session['activity'].append('Lost {} gold from the {}! @Time: {}'.format(value, loc, DateTime))
    #  else:
    #      request.session['activity'].append('Error occured..')
     return redirect('/ninjagold')

def process_money(request):
    #
    # DateTime = datetime.datetime.now()
    if request.method == 'POST':
        hiddenVal = request.POST['hidden']

    # hiddenVal = request.POST['hidden']
        if hiddenVal == 'farm':
            # print hiddenVal
            farmVal = random.randrange(10,21)
            winLose = 'Earned'
            request.session['gold']+= farmVal
            request.session['activity'] += [{'location':hiddenVal, 'gold':farmVal, 'winLose':winLose}]

            # print request.session['gold']
    #     print
    #     # add activity here
    #
        # activity(farmVal, winLose, 'farm')
        elif hiddenVal == 'cave':
            caveVal = random.randrange(5,11)
            request.session['gold'] += caveVal

            winLose = 'Earned'
            request.session['activity']+= [{'location':hiddenVal, 'gold':caveVal, 'winLose':winLose}]
        elif hiddenVal == 'house':
            houseVal = random.randrange(2,6)
            request.session['gold'] += houseVal
            winLose = 'Earned'
            request.session['activity']+= [{'location':hiddenVal, 'gold':houseVal, 'winLose':winLose}]
        elif hiddenVal == 'casino':
            chance = random.randrange(0,2)
            casinoVal = random.randrange(0,51)
            if chance == 0:
                winLose = 'Won'
                request.session['gold'] += casinoVal
                request.session['activity']+= [{'location':hiddenVal, 'gold':casinoVal, 'winLose':winLose}]

            else:
                request.session['gold'] -= casinoVal

                winLose = "Lost"
                request.session['activity']+= [{'location':hiddenVal, 'gold':casinoVal, 'winLose':winLose}]
    else:
        print "something went wrong..."
    return redirect('/ninjagold/activity')
