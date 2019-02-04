from flask import render_template
from flask_login import login_required, current_user

from . import home
from ..models import Department, Role, Employee, IdeaTable


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    ideas = IdeaTable.query.all()

    return render_template('home/dashboard.html', ideas=ideas, title="Dashboard")


@home.route('/lounge')
@login_required
def idea_lounge():
    """
    Render the dashboard template on the /dashboard route
    """
    ideas = IdeaTable.query.all()

    return render_template('home/idea_lounge.html', ideas=ideas, title="Idea Lounge")


# add admin dashboard view
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    ideas = IdeaTable.query.all()

    return render_template('home/admin_dashboard.html', ideas=ideas, title="Dashboard")


# add reward dashboard view
@home.route('/rewards')
@login_required
def rewards():
    """
    Render the dashboard template on the /rewards route
    """
    return render_template('home/rewards.html', title="My Rewards")
