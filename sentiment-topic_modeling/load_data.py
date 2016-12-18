import os
from urllib.request import urlretrieve


# Assign variable with specific path/file info
url = "https://s3-us-west-2.amazonaws.com/msds-projects/data/"
path = "./reviews_Sports_and_Outdoors_5.json.gz"
filename = "reviews_Sports_and_Outdoors_5.json.gz"


def retrieve_data(filename, url, path):
    if not os.path.exists(path):
        filename, _ = urlretrieve(url+filename, filename)
        print("Data Succesfully Retrieved!")
    else:
        print("Your data already exists in the directory. Enjoy.")


if __name__ == "__main__":
    retrieve_data(filename, url, path)
