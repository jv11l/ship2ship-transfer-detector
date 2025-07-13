import matplotlib.axes
import matplotlib.pyplot as plt
import numpy as np
import rasterio
from rasterio.plot import show



def plot_backscatter_distribution(
    band_data: np.ndarray, 
    clip: bool = False, 
    clip_min: float = -30, 
    clip_max: float = 0, 
    ax: matplotlib.axes.Axes = None
    ) -> matplotlib.axes.Axes:
    """
    Plot the distribution of backscatter values in a raster file.

    Parameters:
    - band_data (np.ndarray): The array of backscatter values.
    - clip (bool): Whether to clip the values or not. Default is False.
    - clip_min (float): The minimum value for clipping. Default is -30.
    - clip_max (float): The maximum value for clipping. Default is 0.
    - ax (matplotlib.axes.Axes): The axes object to plot on. If None, a new axes object will be created.

    Returns:
    - ax (matplotlib.axes.Axes): The axes object containing the histogram plot.
    """
    if clip:
        band_data = np.clip(band_data, clip_min, clip_max)
    else:
        pass
    band_data = band_data.flatten()
    print(band_data.shape)

    if ax == None:
        ax = plt.gca()
        
    ax.hist(band_data, bins=100)
    ax.set_title("Distribution of backscatter (dB)")
    return ax
