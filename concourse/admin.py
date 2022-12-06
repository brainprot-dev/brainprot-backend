from django.contrib import admin
from .models import Post, TeamMember

# Register your Models here:

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name','designation', 'email')

admin.site.register(Post, PostAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)

