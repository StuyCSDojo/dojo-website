@public_views.route('/forum/')
def forum_root():
    return flask.render_template('forum_root.html',
                                 is_logged_in=session.get('username'),
                                 topics=db_manager.get_topics())

@public_views.route('/forum/<topic_id>/')
def forum_topic(topic_id):
    topic = db_manager.get_topic_by_id(topic_id)
    posts = db_manager.get_posts_by_topic(topic_id)

    print 'Topic: '
    print topic

    return render_template('forum_topic.html', topic = topic, posts = posts)

@public_views.route('/forum/<topic_id>/<post_id>/')
def forum_post(topic_id, post_id):
    topic = db_manager.get_topic_by_id(topic_id)
    post = db_manager.get_post_by_id(post_id)
    comments = db_manager.get_comments_from_post(post_id)

    return render_template('forum_post.html',
                           topic = topic, post = post, comments = comments)
