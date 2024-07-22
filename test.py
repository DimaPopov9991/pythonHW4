import pickle

with open('file.pkl', 'rb') as f:
    file = pickle.load(f)

    print(file)