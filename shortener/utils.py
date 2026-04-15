from nanoid import generate
from .models import Shorturl

def generate_code() :
    while True:
     code=generate(size=6)
     if not Shorturl.objects.filter(code=code).exists():
         return code