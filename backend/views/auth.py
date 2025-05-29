from pyramid.view import view_config
from pyramid.httpexceptions import HTTPBadRequest, HTTPUnauthorized, HTTPServerError
from pyramid.response import Response
from sqlalchemy.exc import IntegrityError
from models import DBSession, User
from auth import hash_pw, verify_pw, generate_token
from transaction import commit
import json

@view_config(route_name='register', renderer='json', request_method='POST')
def register(request):
    try:
        data = request.json_body
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not name or not email or not password:
            raise HTTPBadRequest(json_body={'error': 'Nama, email, dan password harus diisi'})

        if DBSession.query(User).filter_by(email=email).first():
            raise HTTPBadRequest(json_body={'error': 'Email sudah digunakan'})

        hashed_password = hash_pw(password)
        user = User(name=name, email=email, password=hashed_password, role='user')
        DBSession.add(user)
        commit()  # ✅ simpan ke database
        print(f' Registrasi sukses: {email}')
        return {'message': 'registered'}

    except IntegrityError:
        DBSession.rollback()
        raise HTTPServerError(json_body={'error': 'Gagal menyimpan data. Coba lagi nanti.'})

    except Exception as e:
        DBSession.rollback()
        raise HTTPServerError(json_body={'error': str(e)})

@view_config(route_name='login', renderer='json', request_method='POST')
def login(request):
    try:
        data = request.json_body
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise HTTPBadRequest(json_body={'error': 'Email dan password harus diisi'})

        user = DBSession.query(User).filter_by(email=email).first()
        if not user or not verify_pw(password, user.password):
            raise HTTPUnauthorized(json_body={'error': 'Email atau password salah'})

        # ⛔ Tetapkan role admin hanya untuk email tertentu
        if email == 'travelease@admin.com':
            user.role = 'admin'
        else:
            user.role = 'user'

        token = generate_token(user.id, user.role)
        return {'token': token, 'role': user.role}
    except Exception as e:
        raise HTTPServerError(json_body={'error': str(e)})
