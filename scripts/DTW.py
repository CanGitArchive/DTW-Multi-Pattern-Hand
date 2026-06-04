import numpy as np

def dtw_distance(series1, series2):
    # Step 1: Define the distance function (Euclidean distance)
    def distance(x, y):
        return np.sqrt((x - y) ** 2)
    
    # Step 2: Create a matrix to store accumulated distances
    n, m = len(series1), len(series2)
    dtw_matrix = np.zeros((n+1, m+1))
    dtw_matrix[0, 1:] = np.inf
    dtw_matrix[1:, 0] = np.inf
    
    # Step 3: Initialize the matrix with large values
    
    # Step 4: Set the starting point to 0
    dtw_matrix[0, 0] = 0
    
    # Step 5: Calculate accumulated distances
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = distance(series1[i-1], series2[j-1])
            dtw_matrix[i, j] = cost + min(dtw_matrix[i-1, j],    # Insertion
                                           dtw_matrix[i, j-1],    # Deletion
                                           dtw_matrix[i-1, j-1]) # Match
            
    # Step 6: DTW distance is the value in the bottom-right cell
    return dtw_matrix[n, m]

# Define your arrays
array1 = np.array([1.58, 1.53, 1.44, 0.15, 1.51, 2.22, 2.45, 2.57, 1.98, 1.63])
array2 = np.array([1.52, 1.57, 0.93, 1.06, 1.52, 2.00, 1.91, 1.74, 1.69, 1.71])

# Calculate the DTW distance
dtw_similarity = 1 / (1 + dtw_distance(array1, array2))

print("Dynamic Time Warping Similarity:", dtw_similarity)
