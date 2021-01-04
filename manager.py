from pymongo import MongoClient
import os

ROOT = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(ROOT, "media") 
ICON_PATH = os.path.join(MEDIA_ROOT, "icons") 
CLIENT = MongoClient('localhost', 27017)
DB = CLIENT['9_0_2_36949']
STATICDB = CLIENT['WoWDB']