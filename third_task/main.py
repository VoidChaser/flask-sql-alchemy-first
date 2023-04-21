from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/spaceship.db")
    # add_colounists(db_session)
    add_deploying_job(db_session)
    app.run()


def add_deploying_job(db_ses):
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False

    db_sess = db_ses.create_session()
    db_sess.add(job)
    db_sess.commit()


def add_colounists(db_ses):
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = "scott_chief@mars.org"

    user1 = User()
    user1.surname = 'Mickey'
    user1.name = 'Mouse'
    user1.age = 22
    user1.position = 'employer'
    user1.speciality = 'cleaner'
    user1.address = 'module_2'
    user1.email = "mickey@mars.org"

    user2 = User()
    user2.surname = 'Onion'
    user2.name = 'Skycryer'
    user2.age = 19
    user2.position = 'junior spec.'
    user2.speciality = 'pilot'
    user2.address = 'module_3'
    user2.email = "onion_skycryer@mars.org"

    db_sess = db_ses.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)

    db_sess.commit()




if __name__ == '__main__':
    main()

