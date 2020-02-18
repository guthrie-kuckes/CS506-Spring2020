from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    sums = []
    while len(sums) < len(points[0]):
        sums.append(0);
    for point in points:
        for dimension in range(0, len(point)):
            sums[dimension] += point[dimension]
            
    for i in range(0,len(sums)):
        sums[i] /= len(points)
    return sums


#testing
points1 = [[0,0,0], [1,1,1],[2,2,2]]
print(point_avg(points1))

def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    raise NotImplementedError()


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    if len(a) != len(b):
        raise ValueError("poits of different dimensions")

    distance = 0
    for x in range(0, len(a)):
        diff = a[x] - b[x]
        diff = diff**2
        distance += diff
    return distance**(1/2)

#testing
print(distance([0,0,0], [1,1,1]))


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    raise NotImplementedError()


def cost_function(clustering):
    raise NotImplementedError()


def generate_k_pp(dataset, k):
    raise NotImplementedError()


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
