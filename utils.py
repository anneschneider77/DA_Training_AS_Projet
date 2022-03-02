import unicodedata
import numpy as np
import pandas as pd


def normalize(text):
    nfkd_form = unicodedata.normalize('NFKD', text)
    text = nfkd_form.encode('ASCII', 'ignore').decode('ASCII')
    text = text.lower().replace(' ', '_')
    return text


def spherical_dist(pos1, pos2, r=3958.75 * 1.609):
    pos1 = pos1 * np.pi / 180
    pos2 = pos2 * np.pi / 180
    cos_lat1 = np.cos(pos1[..., 0])
    cos_lat2 = np.cos(pos2[..., 0])
    cos_lat_d = np.cos(pos1[..., 0] - pos2[..., 0])
    cos_lon_d = np.cos(pos1[..., 1] - pos2[..., 1])
    return r * np.arccos(cos_lat_d - cos_lat1 * cos_lat2 * (1 - cos_lon_d))

def transform_into_bins(x):
    a = pd.cut(x, bins=x.quantile(q=np.arange(0, 1.1, .1)), duplicates='drop')
    
    return a.replace({v: i for i, v in enumerate(a.unique())})