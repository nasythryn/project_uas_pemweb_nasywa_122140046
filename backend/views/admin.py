from pyramid.view import view_config
from models import DBSession, TravelSchedule, Car, Booking, User
from sqlalchemy import func
import transaction

@view_config(route_name='travel_crud', renderer='json', request_method='GET')
def get_travel(request):
    data = DBSession.query(TravelSchedule).all()
    return [{'id': d.id, 'asal': d.asal, 'tujuan': d.tujuan, 'tanggal': str(d.tanggal), 'kapasitas': d.kapasitas, 'supir': d.supir} for d in data]

@view_config(route_name='travel_crud', renderer='json', request_method='POST')
def post_travel(request):
    d = request.json_body
    obj = TravelSchedule(asal=d['asal'], tujuan=d['tujuan'], tanggal=d['tanggal'], kapasitas=d['kapasitas'], supir=d['supir'])
    DBSession.add(obj)
    transaction.commit()
    return {'message': 'added'}

@view_config(route_name='travel_delete', renderer='json', request_method='DELETE')
def delete_travel(request):
    obj = DBSession.query(TravelSchedule).filter_by(id=int(request.matchdict['id'])).first()
    if obj:
        DBSession.delete(obj)
        transaction.commit()
    return {'message': 'deleted'}

@view_config(route_name='car_crud', renderer='json', request_method='GET')
def get_car(request):
    rows = DBSession.query(Car).all()
    return [{'id': c.id, 'jenis': c.jenis, 'kapasitas': c.kapasitas} for c in rows]

@view_config(route_name='car_crud', renderer='json', request_method='POST')
def post_car(request):
    d = request.json_body
    obj = Car(jenis=d['jenis'], kapasitas=d['kapasitas'])
    DBSession.add(obj)
    transaction.commit()
    return {'message': 'added'}

@view_config(route_name='car_delete', renderer='json', request_method='DELETE')
def delete_car(request):
    obj = DBSession.query(Car).filter_by(id=int(request.matchdict['id'])).first()
    if obj:
        DBSession.delete(obj)
        transaction.commit()
    return {'message': 'deleted'}

@view_config(route_name='admin_stat', renderer='json', request_method='GET')
def admin_stat(request):
    users = DBSession.query(func.count(User.id)).scalar()
    bookings = DBSession.query(func.count(Booking.id)).scalar()
    return {'users': users, 'bookings': bookings}

@view_config(route_name='admin_booking_list', renderer='json', request_method='GET')
def get_all_bookings(request):
    bookings = DBSession.query(Booking).all()
    return [
        {
            'tanggal_pesan': str(b.tanggal_pesan),
            'nama': b.nama,
            'jenis': b.jenis,
            'tujuan': b.tujuan,
            'tanggal': str(b.tanggal),
            'alamat_jemput': b.alamat_jemput,
            'alamat_tujuan': b.alamat_tujuan
        }
        for b in bookings
    ]
