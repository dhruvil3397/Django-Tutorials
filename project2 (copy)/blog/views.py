from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post,Blogcomment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def bloghome(request):
    allPost = Post.objects.all()

    return render(request,'blog/bloghome.html',{'allPost':allPost})



def blogpost(request,slug):
    post = Post.objects.filter(slug = slug).first()
    post.views = post.views +1
    post.save()


    comments = Blogcomment.objects.filter(post=post,parent = None)
    replies = Blogcomment.objects.filter(post=post).exclude(parent = None)
    #print(comments,replies)

    replyDict = {}  
    for reply in replies:
        if reply.parent.com_id not in replyDict.keys():
            replyDict[reply.parent.com_id] = [reply]
        else :
            replyDict[reply.parent.com_id].append(reply)

    print(replyDict)
    print(post)
    params = {'post':post,'comments':comments,'replyDict':replyDict}
 
    return render(request,'blog/blogpost.html',params)


    
def postcomment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        post_id = request.POST.get('post_id')
        post = Post.objects.get(post_id = post_id)
        parentcom_id = request.POST.get('parentcom_id')
        if parentcom_id == "":
            comment = Blogcomment(comment= comment,user = user,post=post)
            comment.save()
            messages.success(request,"Your comment has been posted successfully")
        else :
            parent = Blogcomment.objects.get(com_id = parentcom_id)
            comment = Blogcomment(comment= comment,user = user,post=post,parent = parent)
     
        
            comment.save()
            messages.success(request,"Your reply has been posted successfully")
        
    return redirect(f'/blog/{post.slug}')

