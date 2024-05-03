from flask import url_for
from application.database_models.comment import Comment
from application.database_models.thread import Thread
from application.viewmodels.comment_viewmodel import CommentViewmodel
from application.viewmodels.thread_viewmodel import ThreadViewmodel
from application.timestamp import get_date_string

def comment_dbmodel_to_viewmodel(comment: Comment) -> CommentViewmodel:
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
        comment.is_reply,
        ""
    )
    return cvm

def comment_dbmodels_to_viewmodels(comments: list[Comment]) -> list[CommentViewmodel]:
    return [comment_dbmodel_to_viewmodel(c) for c in comments]

def thread_dbmodel_to_viewmodel(thread: Thread) -> ThreadViewmodel:
    last_edit = None
    if thread.last_edited_at != -1:
        last_edit = get_date_string(thread.last_edited_at)
    tvm = ThreadViewmodel(
        thread.title,
        thread.content,
        thread.poster.username,
        get_date_string(thread.created_at),
        last_edit,
        url_for("thread.thread_view", forum_name=thread.forum.url_name, thread_uuid=thread.uuid)
    )
    return tvm

def thread_dbmodels_to_viewmodels(threads: list[Thread]) -> list[ThreadViewmodel]:
    return [thread_dbmodel_to_viewmodel(t) for t in threads]
