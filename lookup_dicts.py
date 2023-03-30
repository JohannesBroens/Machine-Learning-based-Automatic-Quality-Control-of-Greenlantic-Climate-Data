
PATH_DATA = {
    'train': {
        'X': 'data/train/X_train.pt',
        'y': 'data/train/y_train_true.pt',
        'preds': 'data/train/preds/'
    },
    'val': {
        'X': 'data/val/X_val.pt',
        'y': 'data/val/y_val_true.pt',
        'preds': 'data/train/preds/'
    },
    'test': {
        'X': 'data/test/X_test.pt',
        'y': 'data/test/y_test_true.pt',
        'preds': 'data/train/preds/'
    }
}
ELEM_DICT = {
    # Below table is from KLIPROD-54462274-051222-1145-124
    # from https://confluence.dmi.dk/pages/viewpage.action?pageId=54462274
    # Only DMI users can access this page. However some of the information is also available in the open source database info from the DMI website.
    # 1-hundred series: Temperature
    101: 'Average Temperature',
    112: 'Maximal Temperature',
    113: 'Maximal Temperature for the last 12 hours (112)',
    122: 'Minimal Temperature',
    123: 'Minimal Temperature for the last 12 hours (122)',
    # 2-hundred series: Humidity
    201: 'Average relative humidity (%)',
    # 3-hundred series: Wind
    301: 'Average wind speed (m/s, 10 minute average)',
    305: 'Highest 3-secound windspeed (m/s)',
    365: 'Average wind direction over 10 minutes (°, grader)',
    371: 'Average wind direction (°, grader)',
    # 4-hundred series: Air pressure
    401: 'Average pressure (hPa)',
    # 5-hundred series: Radiation from the sun
    504: 'Accumulated sunshine (minutes)',
    550: 'Average global radiation (W/m^2)',
    # 6-hundred series: Precipitation
    601: 'Accumulated precipitation (mm)',
    603: 'Accumulated precipitation for the last 12 hours (mm) (601)',
    609: 'Accumulated precipitation for the last 24 hours (mm) (601)',
    # 7-hundred series: Hourly data for 2014 and forward
    731: 'Average visibility (m)',
    741: 'Weather in the moment of observation (code number, see Appendix 2: Om skydække og vejrlig)',
    744: 'Weather for the last 3 hours (code number, 741)',
    745: 'Weather for the last 6 hours (code number, 741)',
    # 8-hundred series: Cloud cover
    801: 'Cloud cover (%)',
}
INDEX_TO_FEATURE = {
    0: 'Element Value',
    1: 'Element Number',
    2: 'Station ID',
    3: 'Year',
    4: 'Month',
    5: 'Day',
    6: 'Hour'
}
