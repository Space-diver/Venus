
# -*- coding: utf-8 -*-
# These codes are adpated from the following
# https://github.com/cfinch/Shocksolution_Examples/blob/d050f3a1c6cd7b251dd716dd81139949009f3cee/PairCorrelation/paircorrelation.py
# python3.6

def pair_correlation(Arr1, Arr2, p, rmax, dr):
    """
    # This is to calculate the average radial density distribution of particle 2
    # in reference to particle 1.
    # Arguments
    # Arr1, 2-D array of coordinates of particle 1
    # Arr2, 2-D array of coordinates of particle 2
    # p = (x0, y0, w, h)
    # (x0, y0), the origin coordinates of the rectangular area to be analyzed
    # w, h, the width and the height of the area to be analyzed
    # rmax, the outer radius of largest annulus to be calculated
    # dr, radius increment of the annulus
    """

    import numpy as np
    from scipy.spatial import distance
    
    x0, y0, w, h = p
    
    
    # remove particles that are too close (distance < rmax) to the border of the area
    B11 = Arr1[:,0] > x0 + rmax
    B12 = Arr1[:,0] < x0 + w - rmax
    B13 = Arr1[:,1] > y0 + rmax
    B14 = Arr1[:,1] < y0 + h - rmax
    mask1 = np.where(B11 & B12 & B13 & B14)
    A1 = Arr1[mask1]
    
    # remove particles that are too close (distance < rmax) to the border of the area
    B21 = Arr2[:,0] > x0
    B22 = Arr2[:,0] < x0 + w
    B23 = Arr2[:,1] > y0
    B24 = Arr2[:,1] < y0 + h
    mask2 = np.where(B21 & B22 & B23 & B24)
    A2 = Arr2[mask2]

    # the number of particles from 1 and 2
    num_clusters_1 = len(A1)
    num_clusters_2 = len(A2)

    # the analyzed radii from 1
    edge = np.arange(0., rmax + 1.1 * dr, dr)
    num_step = len(edge) - 1

    radius = (edge[:-1] + edge[1:]) / 2

    # the average density of the analyzed particles
    density = num_clusters_2 / (w * h)

    d = distance.cdist(A1, A2, 'euclidean')
    # remove the unneeded values before calculating  histogram
    d = d[(d>0) & (d< rmax + (2*dr))]
    
    hist, bins = np.histogram(d, bins=edge, normed=0)
    g_mean = hist/(np.pi * (edge[1:]**2 - edge[:-1]**2) * density * num_clusters_1)
    
    return g_mean, radius
