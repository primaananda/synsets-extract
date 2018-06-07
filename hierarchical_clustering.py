import itertools
from synsets_extraction import synsets_extraction
import numpy as np

x1 = ['ahad', 'esa', 'satu', 'tunggal']
x2 = ['ahad', 'minggu']

def calculate_distance(synset1, synset2):
    similar_word = 0
    sum_word = len(synset1) + len(synset2)
    for word1 in synset1:
        for word2 in synset2:
            if word1 == word2:
                similar_word += 1
                sum_word -= 1
    return similar_word/sum_word

def complete_link(cluster1, cluster2):
    max_distance = None
    for point_a in cluster1:
        for point_b in cluster2:
            dist = calculate_distance(point_a, point_b)
            if max_distance is None:
                max_distance = dist
            else:
                if dist > max_distance:
                    max_distance = dist
    return max_distance

def agglomerative_clustering(dataset):
    current_cluster = dataset
    output_cluster = []
    i = 1
    while len(current_cluster) > 1:
        shortest_distance = None
        shortest_object = None
        #print(current_cluster,'\n')
        best_cluster = None
        for data in itertools.combinations(current_cluster, 2):
            cluster1, cluster2 = data
            if np.array(cluster1).shape == (2,):
                cluster1 = [cluster1]
            if np.array(cluster2).shape == (2,):
                cluster2 = [cluster2]

            dist = complete_link(cluster1, cluster2)

            if shortest_distance is None:
                shortest_distance = dist
                shortest_object = data
                best_cluster = cluster1, cluster2
            else:
                if dist < shortest_distance:
                    shortest_distance = dist
                    shortest_object = data
                    best_cluster = cluster1, cluster2
        current_cluster.remove(shortest_object[0])
        current_cluster.remove(shortest_object[1])
        temp = []
        for point in best_cluster[0]: temp.append(point)
        for point in best_cluster[1]: temp.append(point)
        current_cluster.append(temp)
        print('current cluster : ' + str(current_cluster))
        print("Cluster-{}\n{}\nDistance: {}\n".format(i, list(shortest_object), round(shortest_distance, 2)))
        i += 1
    return output_cluster

file1 = open('datatest/1.json')
synsets = synsets_extraction(file1)
agglomerative_clustering(synsets)
# hasil = calculate_distance(x2,x1)