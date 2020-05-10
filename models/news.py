from .db_session import SqlAlchemyBase
from datetime import date
import sqlalchemy as sa


class News(SqlAlchemyBase):
    __tablename__ = 'personal'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    fam = sa.Column(sa.String)
    name = sa.Column(sa.String)
    date = sa.Column(sa.Date, default=date.today())

    def formated_date(self):
        #return self.date.strftime('%d.%m.%Y')
        return self.fam, self.name, self.date.strftime('%d.%m.%Y')


class News2(SqlAlchemyBase):
    __tablename__ = 't2'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    obrazovan = sa.Column(sa.String)
    specialnost = sa.Column(sa.String)
    stazh = sa.Column(sa.Integer)

    def formated_date(self):
        return self.obrazovan, self.specialnost, self.stazh


class News3(SqlAlchemyBase):
    __tablename__ = 't3'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    dolzhnost = sa.Column(sa.String)
    zarplata = sa.Column(sa.Integer)

    def formated_date(self):
        return self.dolzhnost, self.zarplata, self.zarplata