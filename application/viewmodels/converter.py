from flask import url_for
from flask_login import current_user
from application.database_models.comment import Comment
from application.database_models.thread import Thread
from application.database_models.forum import Forum
from application.viewmodels.comment_viewmodel import CommentViewmodel
from application.viewmodels.thread_viewmodel import ThreadViewmodel
from application.viewmodels.forum_viewmodel import ForumViewModel
from application.timestamp import get_date_string
from application.permissions import check_permissions_comment, check_permissions_forum, check_permissions_thread, ContentAction

def comment_to_viewmodel(comment: Comment) -> CommentViewmodel:
    last_edit = None
    if comment.last_edit_timestamp != -1:
        last_edit = get_date_string(comment.last_edit_timestamp)
    cvm = CommentViewmodel(
        comment.content,
        comment.poster.username,
        get_date_string(comment.creation_timestamp),
        last_edit,
        url_for(
            "comment.comment_view",
            forum_name=comment.thread.forum.url_name,
            thread_uuid=comment.thread.uuid,
            comment_uuid=comment.uuid
        ),
        url_for(
            "comment.comment_edit_view",
            forum_name=comment.thread.forum.url_name,
            thread_uuid=comment.thread.uuid,
            comment_uuid=comment.uuid
        ),
        url_for(
            "comment.comment_delete_view",
            forum_name=comment.thread.forum.url_name,
            thread_uuid=comment.thread.uuid,
            comment_uuid=comment.uuid
        ),
        comment.is_reply,
        "",
        check_permissions_comment(current_user, ContentAction.EDIT, comment),
        check_permissions_comment(current_user, ContentAction.DELETE, comment)
    )
    return cvm

def comments_to_viewmodels(comments: list[Comment]) -> list[CommentViewmodel]:
    return [comment_to_viewmodel(c) for c in comments]

def thread_to_viewmodel(thread: Thread) -> ThreadViewmodel:
    last_edit = None
    if thread.last_edited_at != -1:
        last_edit = get_date_string(thread.last_edited_at)
    tvm = ThreadViewmodel(
        thread.title,
        thread.content,
        thread.poster.username,
        get_date_string(thread.created_at),
        last_edit,
        url_for("thread.thread_view", forum_name=thread.forum.url_name, thread_uuid=thread.uuid),
        url_for("thread.thread_edit_view", forum_name=thread.forum.url_name, thread_uuid=thread.uuid),
        url_for("thread.thread_delete_view", forum_name=thread.forum.url_name, thread_uuid=thread.uuid),
        url_for("forum.forum_view", forum_name=thread.forum.url_name),
        thread.forum.display_name,
        check_permissions_thread(current_user, ContentAction.EDIT, thread),
        check_permissions_thread(current_user, ContentAction.DELETE, thread),
        check_permissions_comment(current_user, ContentAction.CREATE)
    )
    return tvm

def threads_to_viewmodels(threads: list[Thread]) -> list[ThreadViewmodel]:
    return [thread_to_viewmodel(t) for t in threads]

def forum_to_viewmodel(forum: Forum) -> ForumViewModel:
    fvm = ForumViewModel(
        forum.display_name,
        forum.url_name,
        forum.forum_description,
        get_date_string(forum.created_at),
        forum.creator.username,
        forum.is_invite_only,
        url_for("forum.forum_view", forum_name=forum.url_name),
        url_for("forum.forum_edit_view", forum_name=forum.url_name),
        url_for("forum.forum_delete_view", forum_name=forum.url_name),
        url_for("thread.thread_create_view", forum_name=forum.url_name),
        check_permissions_forum(current_user, ContentAction.EDIT, forum),
        check_permissions_forum(current_user, ContentAction.DELETE, forum),
        check_permissions_thread(current_user, ContentAction.CREATE)
    )
    return fvm

def forums_to_viewmodels(forums: list[Forum]) -> list[ForumViewModel]:
    return [forum_to_viewmodel(f) for f in forums]
