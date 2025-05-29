from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.events import NewRequest
from waitress import serve
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from models import DBSession, Base  # DBSession = scoped_session(sessionmaker())
from routes import includeme as include_routes
import zope.sqlalchemy
import transaction

# ✅ Tambahkan CORS headers
def add_cors_headers(event):
    def cors_callback(request, response):
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
            'Access-Control-Allow-Headers': 'Authorization, Content-Type',
        })
    event.request.add_response_callback(cors_callback)

# ✅ Handler khusus untuk OPTIONS
def options_view(request):
    return Response(status=200)

# ✅ Konfigurasi database + session
def setup_database(config):
    settings = config.get_settings()
    engine = engine_from_config(settings, prefix='sqlalchemy.')
    DBSession.configure(bind=engine)
    zope.sqlalchemy.register(DBSession)
    Base.metadata.create_all(engine)

def main():
    settings = {
        'sqlalchemy.url': 'postgresql://postgres:ntr83205%40postgre@localhost:5432/travelease'
    }

    config = Configurator(settings=settings)
    config.add_subscriber(add_cors_headers, NewRequest)

    # Setup DB dan session
    setup_database(config)

    # Routing
    include_routes(config)

    # Tangani semua preflight
    config.add_route('options', '/{catch_all:.*}', request_method='OPTIONS')
    config.add_view(options_view, route_name='options')

    # Scan semua modul views/ (lihat struktur kamu)
    config.scan('views')

    # Start
    app = config.make_wsgi_app()
    print("Server berjalan di http://localhost:6543")
    serve(app, host='0.0.0.0', port=6543)

if __name__ == '__main__':
    main()
