from multiprocessing import context
import re
from urllib.request import Request
from django.shortcuts import redirect, render
from django.contrib import messages
from .functions import generateBlogIdeas,generateBlogSectionHeadings
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def home(request):
    context = {}
    if request.method == 'POST':
        blogIdea = request.POST['blogIdea']
        Keywords = request.POST['Keywords']
        

        blogTopics = generateBlogIdeas(blogIdea,Keywords)
        if len(blogTopics) > 0:
            request.session['blogTopics'] = blogTopics
            return redirect('blogSection')
        else:
            messages.error(request,"could not generate any ideas for you")
            return redirect('home')


    return render(request,'landing/home.html',context)
@csrf_exempt
def blogSection(request):
    if 'blogTopics' in request.session:
        pass
    else:
        messages.error(request,"start by creating blog topic ideas")
        return redirect('home')

    context = {}
    context['blogTopics'] = request.session['blogTopics']
    return render(request,'landing/blog-section.html',context)
