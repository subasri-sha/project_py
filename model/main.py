import pandas as pd

def get_clean_data():  # Reads data from data.csv
    data = pd.read_csv("C:\\pynotes.a\\data.csv")  # make sure file name is correct
    print(data.head())
    return data

def main():
    get_clean_data()

if __name__ == '__main__':
    main()
