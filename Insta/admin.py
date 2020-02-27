from django.contrib import admin

from Insta.models import Comment, Post, InstaUser, Like, UserConnection
# Register your models here.

# admin.site.register(Post)
# admin.site.register(InstaUser)
# admin.site.register(Like)
# admin.site.register(UserConnection)


class CommentInline(admin.StackedInline):
    model = Comment


class LikeInline(admin.StackedInline):
    model = Like


class FollowingInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'creator'


class FollowerInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'following'


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        LikeInline,
    ]


class UserAdmin(admin.ModelAdmin):
    inlines = [
        FollowerInline,
        FollowingInline,
    ]


# admin.site.register(Post)
admin.site.register(Post, PostAdmin)
admin.site.register(InstaUser, UserAdmin)
admin.site.register(UserConnection)
admin.site.register(Comment)
admin.site.register(Like)
