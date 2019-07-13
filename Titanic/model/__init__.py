def get_training_data():
    """get training data from train.csv
    """
    with open('../data/train.csv') as train_file:
        return train_file.read()
