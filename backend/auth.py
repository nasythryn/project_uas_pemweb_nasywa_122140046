import bcrypt
import jwt
import datetime

# ============================
# 🔐 Konfigurasi JWT
# ============================

JWT_SECRET = 'secret'  
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION_TIME = 3600  

# ============================
# 🔐 Password Hashing dengan bcrypt
# ============================

def hash_pw(password: str) -> str:
    """Hash password menggunakan bcrypt."""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')  # Simpan sebagai string

def verify_pw(password: str, hashed_password: str) -> bool:
    """Verifikasi password dengan bcrypt hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# ============================
# 🔐 Token JWT Generator & Verifier
# ============================

def generate_token(user_id: int, role: str) -> str:
    """Buat JWT token berisi user_id dan role."""
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXPIRATION_TIME)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_token(token: str) -> dict:
    """Dekode JWT token dan kembalikan payload."""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception('Token kadaluarsa')
    except jwt.InvalidTokenError:
        raise Exception('Token tidak valid')
