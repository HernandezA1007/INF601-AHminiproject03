# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Mini Project 3

# Import proper packages
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from to_do_list.auth import login_required
from to_do_list.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')  # Displays the list
def index():
    db = get_db()
    items = db.execute(
        'SELECT p.id, created, author_id, title, item_text, username'
        ' FROM todo_list p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('list/index.html', items=items)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():       # Creates...
    if request.method == 'POST':
        title = request.form['title']
        item_text = request.form['item_text']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO todo_list (title, item_text, author_id)'
                ' VALUES (?, ?, ?)',
                (title, item_text, g.user['id'])
            )
            db.commit()
            return redirect(url_for('list.index'))

    return render_template('create.html')  # list/create


def get_items(id, check_author=True):       # Obtains...
    items = get_db().execute(
        'SELECT p.id, created, author_id, title, item_text, username'
        ' FROM todo_list p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if items is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and items['author_id'] != g.user['id']:
        abort(403)

    return items


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):         # Changes...
    items = get_items(id)

    if request.method == 'POST':
        title = request.form['title']
        item_text = request.form['item_text']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE todo_list SET title = ?, item_text = ?'
                ' WHERE id = ?',
                (title, item_text, id)
            )
            db.commit()
            # return redirect(url_for('blog.index'))
            return redirect(request.referrer)

    return render_template('update.html', items=items)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):     # Removes...
    get_items(id)
    db = get_db()
    db.execute('DELETE FROM todo_list WHERE id = ?', (id,))
    db.commit()
    # return redirect(url_for('blog.index'))
    return redirect(request.referrer)

