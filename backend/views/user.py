from pyramid.view import view_config
from models import DBSession, TravelSchedule, Booking, User
from auth import decode_token
from pyramid.httpexceptions import HTTPUnauthorized, HTTPBadRequest, HTTPNotFound, HTTPServerError
from pyramid.response import Response
from datetime import datetime
import json

def get_user_id(request):
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    if not token:
        raise HTTPUnauthorized(json_body={'error': 'Token tidak ditemukan'})
    try:
        payload = decode_token(token)
        return payload['user_id']
    except Exception as e:
        raise HTTPUnauthorized(json_body={'error': str(e)})

@view_config(route_name='travel_list', renderer='json', request_method='GET')
def travel_list(request):
    jadwal = DBSession.query(TravelSchedule).all()
    return [
        {
            'id': j.id,
            'asal': j.asal,
            'tujuan': j.tujuan,
            'tanggal': j.tanggal.strftime('%Y-%m-%d'),
            'kapasitas': j.kapasitas,
            'supir': j.supir
        }
        for j in jadwal
    ]

import transaction

@view_config(route_name='user_booking', renderer='json', request_method='POST')
def user_booking(request):
    try:
        user_id = get_user_id(request)
        data = request.json_body

        if not all(k in data for k in ( 'tanggal_pesan', 'nama', 'jenis', 'tujuan', 'tanggal', 'alamat_jemput', 'alamat_tujuan')):
            raise HTTPBadRequest(json_body={'error': 'Data tidak lengkap'})

        tanggal_str = data['tanggal']
        tanggal_obj = datetime.strptime(tanggal_str, '%Y-%m-%d').date()
        tanggal_pesan_str = data['tanggal_pesan']
        tanggal_pesan_obj = datetime.strptime(tanggal_pesan_str, '%Y-%m-%d').date()
        
        b = Booking(
            user_id=user_id,
            tanggal_pesan=tanggal_pesan_obj,
            nama=data['nama'],
            jenis=data['jenis'],
            tujuan=data['tujuan'],
            tanggal=tanggal_obj,
            alamat_jemput=data['alamat_jemput'],
            alamat_tujuan=data['alamat_tujuan']
        )
        DBSession.add(b)
        transaction.commit()  
        request.response.status = 201
        return {'message': 'booked'}

    except Exception as e:
        raise HTTPServerError(json_body={'error': str(e)}) 


@view_config(route_name='user_history', renderer='json', request_method='GET')
def booking_history(request):
    try:
        user_id = get_user_id(request)
        bookings = DBSession.query(Booking).filter_by(user_id=user_id).all()
        return [
            {
                'tanggal_pesan': str(b.tanggal_pesan),
                'jenis': b.jenis,
                'tujuan': b.tujuan,
                'tanggal': str(b.tanggal),
                'alamat_jemput': b.alamat_jemput,
                'alamat_tujuan': b.alamat_tujuan
            }
            for b in bookings
        ]
    except Exception as e:
        raise HTTPServerError(json_body={'error': str(e)})

def includeme(config):
    config.add_route('travel_list', '/api/user/travel')
    config.add_route('user_booking', '/api/user/booking')
    config.add_route('user_history', '/api/user/history')
    config.add_route('user_profile', '/api/user/profile')
    config.scan(__name__)
