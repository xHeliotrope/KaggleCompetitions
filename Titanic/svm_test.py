"""gonna test some SVM stuff

steps:
    1. function that adds labelled data to a plot
    2. function that tests linear seperability and then decides to keep/remove last dot added
    3. show plot
    4. calculate a hyperplane
    5. calculate the margin
    6. do some brute forcing
"""
import math
from random import randint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

get_int = lambda: randint(0, 100)


def euclidean_distance(pt_one, pt_two):
    squared_difference = pow(pt_one[0] - pt_two[0], 2) + pow(pt_one[1] - pt_two[1], 2)
    return math.sqrt(squared_difference)

def get_hyperplane(pt_one, pt_two):
    """ y = mx + b
    """
    z_vector = {
        'x': pt_one[0] - pt_two[0],
        'y': pt_one[1] - pt_two[1],
    }
    hyperplane = ()



def is_separable(data):
    """check if the data is linearly separable
    """
    is_separable = False
    set_1 = [x for x in data if not x['label']] 
    set_2 = [x for x in data if x['label']]

    for pt_one in set_1:
        for pt_two in set_2_pt:
            hyper_plane = get_hyperplane(pt_one, pt_two)



def generate_separable_plot(num_pts):
    """given a number of points, generate a linearly separable plot
    with 2 labels
    """
    current_label = True
    points = []
    for index in range(num_pts):
        points.append({'x': get_int(), 'y': get_int(), 'label': current_label})
        # alternate the labels
        current_label = not current_label
        if index > 3:
            if not is_separable(points):
                points.pop(-1)

    return points

def make_plt(data):

    x1s = [dat['x1'] for dat in data]
    x2s = [dat['x2'] for dat in data]
    c = [dat['x2'] for dat in data]

    fig, ax = plt.subplots()
    ax.scatter(x1s, x2s, c=c)

    ax.set_xlabel('Shrim (lbs)', fontsize=15)
    ax.set_ylabel('Plumbis Length(m)', fontsize=15)
    ax.set_title('FUCKING DOTS')

    ax.grid(True)
    fig.tight_layout()
    return plt


# get the minimum distance between all the pointies
def points_min():
    # get a default minimum using the first points in each sets
    pt_one = set_1[0]
    pt_two = set_2[0]
    min_pts = (pt_one, pt_two)
    min_distance = euclidean_distance(pt_one, pt_two)

    for temp_pt_1 in set_1:
        for temp_pt_2 in set_2:
            temp_dist = euclidean_distance(temp_pt_1, temp_pt_2)
            if temp_dist < min_distance:
                min_distance = temp_distance
                min_pts = (pt_one, pt_two)


