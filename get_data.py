import os
import wget

# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the zipped dataset
# url = 'https://storage.cloud.google.com/staging-eu-ml-pipelines-g98e/dvc_test_data/'
# zip_name = "data_raw.csv"
# wget.download(url, zip_name)

# Unzip it and standardize the .csv filename
# import zipfile
# with zipfile.ZipFile(zip_name,"r") as zip_ref:
#     zip_ref.filelist[0].filename = 'data_raw.csv'
#     zip_ref.extract(zip_ref.filelist[0])

# os.remove(zip_name)

from google.cloud import storage

# Initialise a client
storage_client = storage.Client("analytics-staging-e1b8")
# Create a bucket object for our bucket
bucket = storage_client.get_bucket("staging-eu-ml-pipelines-g98e")
# Create a blob object from the filepath
blob = bucket.blob("dvc_test_data/rawdata_new.csv")
# Download the file to a destination
blob.download_to_filename("data_raw.csv")

#change for experiment 2