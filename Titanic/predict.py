import csv
import model

# make a prediction given the data
predictions = []
with open('./train.csv') as data_file:
    data = data_file.read()
    for row in data:
        predictions.append(model.make_prediction(row))

# write the data to a file to submit
fieldnames ['PassengerId', 'Survived']
with open('predictions.csv', 'w+') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for prediction in predictions:
        writer.writerow(prediction)

