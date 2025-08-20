from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelterCRUD(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, passwd):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = username
        PASS = passwd
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30807
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.collection.insert_one(data)
            return True
        else:
            return False

    # Create method to implement the R in CRUD.
    # Reads One document from the collection
    def read_one(self, data):
        if data is not None:
            found = self.collection.find_one(data)
            return list(found)
        else:
            return []

    # Reads all documents based on the given data input
    def read(self, data):
        if data is not None:
            found = self.collection.find(data)
            return list(found)
        else:
            return []

    # Updates all documents based on the given data
    def update(self, data, updatedata):
        if data is not None:
            if updatedata is not None:
                try:
                    count = self.collection.update_many(data,updatedata)
                    return count.modified_count
                except Exception as e:
                    print('Invalid data')
                    return 0
            else:
                return 0
        else:
            return 0

    # Deletes all documents based on the given data
    def delete(self, data):
        if data is not None:
            count = self.collection.delete_many(data)
            return count.deleted_count
        else:
            return 0
