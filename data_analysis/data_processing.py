import pandas as pd
from IPython.core.display_functions import display


def load_dataset():
    file = '../dataset/suicide_rates_socioeconomic_factors.csv'
    data = pd.read_csv(file,
                       usecols=['RegionName', 'CountryName', 'Year', 'Sex',
                                'SuicideCount',
                                'Population', 'GDPPerCapita', 'InflationRate', 'EmploymentPopulationRatio'])

    data = data.dropna()  # Drop rows with null or NaN values
    data = data.reset_index(drop=True)
    data_filtered = data[(data['Year'] >= 2010) & (data['Year'] <= 2022)]

    df = pd.DataFrame({'Year': data_filtered['Year'],
                       'RegionName': data_filtered['RegionName'],
                       'CountryName': data_filtered['CountryName'],
                       'Sex': data_filtered['Sex'],
                       'SuicideCount': data_filtered['SuicideCount'],
                       'Population': data_filtered['Population'],
                       'GDPPerCapita': data_filtered['GDPPerCapita'],
                       'EmploymentPopulationRatio': data_filtered['EmploymentPopulationRatio'],
                       'InflationRate': data_filtered['InflationRate']})

    df = df.sort_values(by='Year')
    df = df.reset_index(drop=True)

    display(df)

    return df


def change_columns(df):
    one_hot_regions = pd.get_dummies(df['RegionName'], prefix='Region')  # Add 6 more columns to the df with the one hot encoding
    df = df.join(one_hot_regions)

    df['Sex'] = df['Sex'].apply(lambda x: 1 if x == 'Male' else 0)

    numeric_features = ['Year', 'SuicideCount', 'Population', 'GDPPerCapita', 'EmploymentPopulationRatio', 'Sex'] + list(one_hot_regions.columns)  # Take those columns for PCA, because it takes only numeric features

    return numeric_features
