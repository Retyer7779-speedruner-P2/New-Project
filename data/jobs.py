from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, orm, Boolean

from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = "jobs   "

    id = Column(Integer, primary_key=True)
    team_leader = Column(Integer, ForeignKey("users.id"))
    user = orm.relationship("User")
    job = Column(String)
    work_size = Column(String)
    collaborators = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_finished = Column(Boolean)