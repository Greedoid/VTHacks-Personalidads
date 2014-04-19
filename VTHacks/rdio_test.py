from rdio import Rdio
from config import CONSUMER_KEY, CONSUMER_SECRET


RDIO_CONSUMER_KEY = CONSUMER_KEY
RDIO_CONSUMER_SECRET = CONSUMER_SECRET

rdio = Rdio((RDIO_CONSUMER_KEY, RDIO_CONSUMER_SECRET))

ian = rdio.call("findUser", {"vanityName": "ian"})

print ian
