# helper functions for cleaning up product list

import pandas as pd


def clean_EAN(df):
    # TODO: include logic about checking availability and type of EAN
    if 'EAN' in df.columns:
        df.EAN.fillna(0)
        df.EAN = df.EAN.astype(str)
        df.EAN = df.EAN.str.split('.').str[0]
    return df