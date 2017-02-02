from django.contrib import admin
from .models import Post_Thoughts, Post_Work, Post_Photos, Post_Videos

admin.site.register(Post_Thoughts)
admin.site.register(Post_Work)
admin.site.register(Post_Photos)
admin.site.register(Post_Videos)