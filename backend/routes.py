def includeme(config):
    config.add_route('register', '/api/register')
    config.add_route('login', '/api/login')
    config.add_route('user_profile', '/api/user/profile')

    config.add_route('travel_list', '/api/user/travel')
    config.add_route('user_booking', '/api/user/booking')
    config.add_route('user_history', '/api/user/history')

    config.add_route('travel_crud', '/api/admin/travel')
    config.add_route('travel_delete', '/api/admin/travel/{id}')
    config.add_route('car_crud', '/api/admin/cars')
    config.add_route('car_delete', '/api/admin/cars/{id}')
    config.add_route('admin_stat', '/api/admin/statistik')
    config.add_route('admin_booking_list', '/api/admin/bookings')
