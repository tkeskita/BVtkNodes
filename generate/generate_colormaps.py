import matplotlib
import matplotlib.pyplot as plt
import json
import numpy as np


class NDArrayEncoder(json.JSONEncoder):
    #float_str = "{.5f}"
    #@override
    def default(self, obj):
        #print("NDArrayEncoder called with " + obj)
        if isinstance(obj, np.ndarray):
            return np.array_str(obj, precision=6) #self.float_str.format(obj)
        return super(NDArrayEncoder, self).default(obj)

#https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

cmaps = {}

cmaps['perc_sequential'] = [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']

cmaps['sequential'] = [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

cmaps['diverging'] = [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
cmaps['cyclic'] = ['twilight', 'twilight_shifted', 'hsv']
cmaps['qualitative'] = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                        'Dark2', 'Set1', 'Set2', 'Set3',
                        'tab10', 'tab20', 'tab20b', 'tab20c']
cmaps['misc'] = [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']

cmaps_keys = list(cmaps.keys())
cmap_rgb_filename = "colormaps/colormaps_rgb.json"
cmap_hsv_filename = "colormaps/colormaps_hsv.json"

if __name__ == "__main__":

    all_cmaps_rgb = {}
    all_cmaps_hsv = {}

    #We remove the initial classification between the different colormaps and save them in a flat format
    for key, val in cmaps.items():
        for single_map in val:
            cmap = plt.cm.get_cmap(single_map)

            colors = cmap(np.linspace(0, 1, num=64))
            assert(np.allclose(colors[..., -1], 1.)) #Check that alpha channel is 1 and remove it
            colors = colors[..., :-1]
            all_cmaps_rgb[single_map] = colors.tolist()
            all_cmaps_hsv[single_map] = matplotlib.colors.rgb_to_hsv(colors).tolist()

            #all_cmaps[val] = 

    for cmap_filename, all_cmaps in zip([cmap_rgb_filename, cmap_hsv_filename], [all_cmaps_rgb, all_cmaps_hsv]):
        json_str = json.dumps(all_cmaps, indent=2) #, cls=NDArrayEncoder)
        with open(cmap_filename, 'w') as f:
            f.write(json_str)