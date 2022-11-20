from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import *
from django.urls import reverse_lazy
from .models import *
from registration.views import username_
from django.shortcuts import redirect
# Create your views here.
# from django.contrib.auth.decorators import login_required

# @login_required
def createPost(request):
    if request.method == 'POST':
        form = postInfo(request.POST,request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            post = form.cleaned_data.get('image')
            # print('dsf') username=username_ username_id = username_.values_list('id',flat=True).get(pk=1) 
            post_ = Post.objects.create(caption=title,post1=post,like=0)

            post_.save()
            
            return redirect('/post/home')
        else:
            print(form)
    else:
        form = postInfo()
    
    return render(request, 'createPost.html',{'form':form})

# class createPost(FormView):
#     form_class = postInfo
#     template_name='createPost.html'
#     success_url = reverse_lazy('home')

class AllPost(ListView):
    model = Post
    fields = ('caption','post','comments','like')
    template_name = 'home.html'
    

    def get_context_data(self,*args,**kwargs):
        context = super(AllPost, self).get_context_data(*args,**kwargs)
        all_post= Post.objects.all() 
        for post in all_post:
            p = post.post1
            # print()
            # p = p[]
        context['data'] = all_post
        return context
    # context_object_name={'data':data}


