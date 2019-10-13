import requests


def get_all_data():
    root = "https://raw.githubusercontent.com/patidarparas13/Sentiment-Analyzer-Tool/master/Datasets/"

    data = requests.get(root + "imdb_labelled.txt").text.split("\n")
    data += requests.get(root + "amazon_cells_labelled.txt").text.split("\n")
    data += requests.get(root + "yelp_labelled.txt").text.split("\n")

    return data


data = get_all_data()
