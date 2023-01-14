import numpy as np
import pandas as pd
import json
import os

# -------------------------------

mynumarr = np.random.rand(4)

type(mynumarr)

myseries = pd.Series(mynumarr, index=["First", "Second", "Third", "Fourth"])

myseries["Fourth"]

my2darr = np.random.rand(3, 2)

myframes = pd.DataFrame(my2darr)

myframes.columns = ["First", "Second"]

myframes["Second"]

############################

CSV_PATH = os.path.join(
    "D:\Downloads\Programming\Python\Pandas Fundamental PluralSight\pandas-fundamentals\demos\collection-master",
    "artwork_data.csv")

df = pd.read_csv(CSV_PATH, nrows=5)

df = pd.read_csv(CSV_PATH, nrows=5, index_col='id')

df = pd.read_csv(CSV_PATH, nrows=5, index_col='id', usecols=['id', 'artist'])

COLS_TO_USE = ['id', 'artist', 'title', 'medium', 'year', 'acquisitionYear', 'height', 'width', 'units']

df = pd.read_csv(CSV_PATH, nrows=5, index_col='id', usecols=COLS_TO_USE)

df.to_pickle(os.path.join(
    "D:\Downloads\Programming\Python\Pandas Fundamental PluralSight\pandas-fundamentals\demos\collection-master",
    'data_frame.pickle'))

# create a list to get the of tuples
records = [('Expresso', '5$'), ('Cuppacino', '4$')]
pd.DataFrame.from_records(records)
pd.DataFrame.from_records(records, columns=['Coffee', 'Price'])


# 1. read files one by one into a json object
# 2. from each pick real data and put in a tuple
# 3. one global root, materialise dataframe

KEYS_TO_USE = ['id', 'all_artists', 'title', 'medium', 'acquisitionYear', 'height', 'width']


def get_record_from_file(file_path, keys_to_use):
    """
    :rtype: object
    """
    # process a single json file and return a tuple containing fields queried
    with open(file_path) as artwork_file:
        contents = json.load(artwork_file)

    record = []
    for keys in keys_to_use:
        record.append(contents[keys])

    return tuple(record)


# test the function here
SAMPLE_JSON_FILE_PATH = os.path.join(
    'D:\Downloads\Programming\Python\Pandas Fundamental PluralSight\pandas-fundamentals\demos\collection-master',
    'artworks', 'a', '000', 'a00001-1035.json')

sample_file_content = get_record_from_file(SAMPLE_JSON_FILE_PATH, KEYS_TO_USE)


# multiple files  traversing in the folder
def read_artworks_from_json_dir(keys_to_use):

    json_dir_repo = os.path.join('D:\Downloads\Programming\Python\Pandas Fundamental PluralSight\pandas-fundamentals\demos\collection-master','artworks')
    #loop through subdirs under primary dir
    #once in a subdir, loop through each file by calling :
    artworks = []
    for root, dirs, files in os.walk(json_dir_repo):
        for name in files:
            if (name.endswith("json")):
                records = get_record_from_file(os.path.join(root,name),keys_to_use)
                artworks.append(records)
            break

        ddf = pd.DataFrame.from_records(artworks, columns=keys_to_use, index="id")

    return ddf

df = read_artworks_from_json_dir(KEYS_TO_USE)

df['all_artists']

pd.unique(df['all_artists'])

len(pd.unique(df['all_artists']))

s =df['all_artists'] == 'Robert Blake'
s.value_counts()

artist_counts = df['all_artists'].value_counts()

df.shape










