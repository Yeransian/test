from flask import Blueprint, render_template, request
from innoviuzsite.models import Post
from flask_mail import Message
from innoviuzsite import mail
# from flask_login import login_user, login_required, current_user, logout_user

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def index():
    services_list = services()
    return render_template('index.html', services_list=services_list)


@main.route('/about')
def about():
    services_list = services()
    return render_template('about.html', services_list=services_list)


@main.route('/blog-single')
def singleblog():
    return render_template('blog-single.html')


@main.route('/blog')
def blog():
    return render_template('blog.html')


@main.route('/blog-single') # blog-sing.html ??
def blog_single():
    return render_template('blog-single.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


# @main.route('/main')
# def main():
#     return render_template('main.html')


@main.route('/project')
def project():
    return render_template('project.html')


@main.route('/services')
def services():
    return render_template('services.html')


@main.route('/team')
def team():
    return render_template('team.html')


# @login_required
# @main.route('/test')
# def test():
#     if current_user.is_authenticated:
#         return render_template('test.html')
#     else:
#         return render_template('team.html')

def services():
    services_list = ['Web Development', 'Automation', 'Data Analytics', 'IT Services', 'SEO Optimization',
                'Marketing/Social Media']
    return services_list


@main.route('/consultation', methods=['POST'])
def consultation():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    service = request.form["service"]
    phone_number = request.form["phone_number"]
    message = request.form["message"]
    print(first_name, last_name, service, phone_number, message)
    msg = Message(f'Consultation for {service}',
                  sender='abraham@gmail.com', recipients=['abraham@innoviuz.com'])
    msg.body = f'Name: {first_name} {last_name} Phone:{phone_number} {message}'
    mail.send(msg)
    return first_name


@main.route('/send_contact', methods=['POST'])
def send_contact():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]
    print(name, email, subject, message)
    msg = Message(f'Message from {name}',
                  sender='abraham@gmail.com', recipients=['abraham@innoviuz.com'])
    msg.body = f'Name: {name} {email} Subject: {subject} {message}'
    mail.send(msg)
    return name

# @main.route('/')
# @main.route('/home')
# def home():
#     # posts = Post.query.all()
#     page = request.args.get('page', 1, type=int)
#     posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
#     return render_template('home.html', posts=posts)
#
#
# @main.route('/about')
# def about():
#     return render_template('about.html', title='About')
#
#
# @main.route('/test')
# def test():
#     return render_template('test.html', title='Test')