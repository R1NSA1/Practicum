import pickle


def save_table_pickle(file_name, data):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def load_table_pickle(file_name):
    with open(file_name, 'rb') as f:
        print(pickle.load(f))
