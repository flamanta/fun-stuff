import numpy as np
from math import sqrt


def cartToSph(x, y, z):
    """Computes and returns spherical coordinates (r, az, el)
     as NumPy arrays. Input is Cartesian coordinates (x, y, z)."""

    # Initialize empty lists
    r = []
    az = []
    el = []

    for idx in range(len(x)):

        # Calculate radius, azimuth and elevation
        radius = np.round(sqrt(x[idx] ** 2 + y[idx] ** 2 + z[idx] ** 2), 5)
        azimuth = np.round(np.arctan2(y[idx], x[idx]), 5)
        elevation = np.round(np.arccos(z[idx] / radius), 5)

        # Append to the master list
        r.append(radius)
        az.append(azimuth)
        el.append(elevation)

    # Change list to NumPy arrays
    r = np.array(r)
    az = np.array(az)
    el = np.array(el)

    return r, az, el


def sphToCart(r, az, el):
    """Computes and returns Cartesian coordinates (x, y, z)
     as NumPy arrays. Input is spherical coordinates (r, az, el)."""

    # Initialize empty lists
    x = []
    y = []
    z = []

    for idx in range(len(r)):

        # Calculate x, y and z
        ptX = np.round(r[idx] * np.sin(el[idx]) * np.cos(az[idx]), 5)
        ptY = np.round(r[idx] * np.sin(el[idx]) * np.sin(az[idx]), 5)
        ptZ = np.round(r[idx] * np.cos(el[idx]), 5)

        # Append to the master list
        x.append(ptX)
        y.append(ptY)
        z.append(ptZ)

    # Change list to NumPy arrays
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)

    return x, y, z
