import pymongo
from urllib.parse import quote_plus
from pymongo import MongoClient

USERNAME = 'raja_interview'
PASSWORD = 'AZDMbHpFOgPaKhDL'
HOST = 'staging-migration.rmjlr.mongodb.net/test?w=majority'

uri = f"mongodb+srv://{quote_plus(USERNAME)}:{quote_plus(PASSWORD)}@{HOST}"
# noinspection PyUnresolvedReferences
parse_uri = pymongo.uri_parser.parse_uri(
    uri,
    default_port=27017,
    validate=True,
    warn=False,
    normalize=True,
    connect_timeout=None
)


client = MongoClient(uri)

db = client.test

ab_test_collection = db.ab_test
