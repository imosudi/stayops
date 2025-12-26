# stayops/infrastructure/repositories/base.py
class BaseRepository:
    def __init__(self, session):
        self.session = session

    def active(self, model):
        return self.session.query(model).filter_by(is_deleted=False)
