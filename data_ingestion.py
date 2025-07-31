import os
import sys
from dataclasses import dataclass
import kagglehub
from root.exception import CustomException
from root.logger import logging
import pandas as pd



# DATA INGESTION OF THE SAMPLE DATASETS
@dataclass
class DataIngestionConfig:
    dataset_path_1: str= os.path.join('sample_datasets','indian-kids-screentime-2025.csv')
    dataset_path_2: str = os.path.join('sample_datasets', 'social_media_engagements.csv')
    dataset_path_3: str = os.path.join('sample_datasets', 'electronic_product_detials.csv')


class DataIngestion:
    def __init__(self):
        self.ingestionconfig = DataIngestionConfig()


    def load_sample_datasets(self):
        logging.info("starting to download sample datasets")
        try:
            # loading sample datasets
            data_1 = pd.read_csv("Indian_Kids_Screen_Time.csv")
            logging.info("sample data 1 read successfully")

            os.makedirs(os.path.dirname(self.ingestionconfig.dataset_path_1), exist_ok=True)
            data_1.to_csv(self.ingestionconfig.dataset_path_1, index=False, header=True)
            
            logging.info("sample data 1 downloaded")

            # loading sample datasets
            data_2 = pd.read_csv("social_media_engagement1.csv")
            logging.info("sample data 2 read successfully")

            os.makedirs(os.path.dirname(self.ingestionconfig.dataset_path_2), exist_ok=True)
            data_2.to_csv(self.ingestionconfig.dataset_path_2, index=False, header=True)
            
            logging.info("sample data 2 downloaded")

            # loading sample datasets
            data_3 = pd.read_csv("Electronic_product_details.csv")
            logging.info("sample data 3 read successfully")

            os.makedirs(os.path.dirname(self.ingestionconfig.dataset_path_3), exist_ok=True)
            data_3.to_csv(self.ingestionconfig.dataset_path_3, index=False, header=True)
            
            logging.info("sample data 3 downloaded")
            return (
                self.ingestionconfig.dataset_path_1,
                self.ingestionconfig.dataset_path_2,
                self.ingestionconfig.dataset_path_3
            )

        except Exception as e:
            raise CustomException(e,sys)
if __name__ == "__main__":
    obj = DataIngestion()
    obj.load_sample_datasets()
