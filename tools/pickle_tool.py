import pickle

pickle_folder = "pickle_files"


def save_pickle(data, name):
    full_path = pickle_folder + "/" + name
    outfile = open(full_path, "wb")
    pickle.dump(data, outfile)
    outfile.close()


def get_pickle(name):
    infile = open("pickle_folder" + "/" + name, "rb")
    games = pickle.load(infile)
    infile.close()
    return games
