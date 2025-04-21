import os
import sys
import pandas as pd
import json
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException

load_dotenv()

uri = os.getenv("MONGO_URL")


class NetworkDataExtract:
    def __init__(self):
        pass

    def cv_to_json_converter(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongoDB(self, records, database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection
            self.mong_client = MongoClient(uri)
            self.database = self.mong_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    DATA_FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE_NAME = "document_india"
    COLLECTION_NAME = "network_security"
    networkDataExtract = NetworkDataExtract()
    records = networkDataExtract.cv_to_json_converter(DATA_FILE_PATH)

    records1 = networkDataExtract.insert_data_to_mongoDB(
        records, DATABASE_NAME, COLLECTION_NAME
    )
    print(records1)
