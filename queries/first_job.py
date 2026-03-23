from data import db_session
from data.jobs import Jobs

db_session.global_init("db/mars_explorer.db")
session = db_session.create_session()

first_job = Jobs(
    job="deployment of residential modules 1 and 2",
    team_leader="1",
    work_size="15",
    collaborators="2, 3",
    is_finished="False"
)

session.add(first_job)
session.commit()