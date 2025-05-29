from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(128), nullable=False) 
    role = Column(String(20), default='user', nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"

class TravelSchedule(Base):
    __tablename__ = 'travel_schedules'
    id = Column(Integer, primary_key=True)
    asal = Column(String, nullable=False)
    tujuan = Column(String(100), nullable=False)
    tanggal = Column(Date, nullable=False)
    kapasitas = Column(Integer, nullable=False)
    supir = Column(String, nullable=False)

    def __repr__(self):
        return f"<TravelSchedule(tujuan={self.tujuan}, tanggal={self.tanggal})>"

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    jenis = Column(String(100), nullable=False)
    kapasitas = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Car(jenis={self.jenis})>"

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    tanggal_pesan = Column(Date, nullable=False)
    nama = Column(String, nullable=False)
    jenis = Column(String, nullable=False)
    tujuan = Column(String, nullable=False)
    alamat_jemput = Column(String, nullable=False)
    alamat_tujuan = Column(String, nullable=False)
    tanggal = Column(Date, nullable=False)  

    user = relationship('User', backref='bookings')

    def __repr__(self):
        return f"<Booking(user_id={self.user_id}, tujuan={self.tujuan}, tanggal={self.tanggal})>"
