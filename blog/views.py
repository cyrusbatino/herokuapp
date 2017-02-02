from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import Context
from django.template.loader import get_template
from .models import Post_Thoughts, Post_Work, Post_Photos, Post_Videos
from .forms import ContactForm

# Create your views here.
def post_list(request):
	post_t = Post_Thoughts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	post_w = Post_Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	post_p = Post_Photos.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	post_v = Post_Videos.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	form_class = ContactForm

	# new logic!
	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			name = request.POST.get('name', '')
			email = request.POST.get('email', '')
			subject = request.POST.get('subject', '')
			message = request.POST.get('message', '')

			# Email the profile with the 
			# contact information
			template = get_template('blog/contact.txt')
			context = Context({
				'name': name,
				'email': email,
				'subject': subject,
				'message': message,
			})
			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				email,
				['boogness@gmail.com'],
				headers = {'Reply-To': email }
			)
			email.send()
			return redirect('post_list')

	return render(request, 'blog/index.html', {
		'thoughts':post_t,
		'work': post_w,
		'photos':post_p,
		'videos':post_v,
		'form': form_class,
	})


def detail_thoughts(request, slug):
    post = get_object_or_404(Post_Thoughts, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post,'ext':'#blog','head':'thoughts'})

def detail_work(request, slug):
    post = get_object_or_404(Post_Thoughts, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post,'ext':'#work','head':'projects'})

def detail_photos(request, slug):
    post = get_object_or_404(Post_Photos, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post,'ext':'#photo','head':'photography'})

def detail_videos(request, slug):
    post = get_object_or_404(Post_Videos, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post,'ext':'#film','head':'filmography'})
    