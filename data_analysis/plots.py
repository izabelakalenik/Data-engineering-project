import seaborn as sns
import matplotlib.pyplot as plt

def plot_country_distribution(df):
    country_counts = df['CountryName'].value_counts()
    print(country_counts)

    plt.figure(figsize=(10, 8))
    sns.barplot(x=country_counts.values, y=country_counts.index)
    plt.title('Distribution of Countries in the Dataset')
    plt.xlabel('Counts')
    plt.ylabel('Countries')
    plt.show()

def plot_region_distribution(df):
    region_counts = df['RegionName'].value_counts()
    print(region_counts)
    
    plt.figure(figsize=(10, 8))
    sns.barplot(x=region_counts.values, y=region_counts.index)
    plt.title('Distribution of Regions in the Dataset')
    plt.xlabel('Counts')
    plt.ylabel('Regions')
    plt.show()

def plot_country_region_distribution(df):
    country_region_counts = df.groupby('RegionName')['CountryName'].value_counts().unstack(fill_value=0)
    print(country_region_counts)

    country_region_counts.plot(kind='bar', stacked=True, figsize=(12, 10))
    plt.title('Country Distribution by Region')
    plt.xlabel('Regions')
    plt.ylabel('Counts of Countries')
    plt.legend(title='Country')
    plt.show()

def plot_correlation_matrix(df):
    correlation_matrix = df[['SuicideCount', 'Population', 'GDPPerCapita', 'EmploymentPopulationRatio']].corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.show()

def plot_descriptive_stats(numeric_df):
    descriptive_stats = numeric_df.describe()
    print(descriptive_stats)

def plot_correlation_heatmap(numeric_df):
    correlation_matrix = numeric_df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix of Suicide Rates Dataset')
    plt.show()

def plot_suicide_counts_over_time_by_region_and_gender(df):
    region_sex_time_suicides = df.groupby(['RegionName', 'Sex', 'Year'])['SuicideCount'].sum().reset_index()
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=region_sex_time_suicides, x='Year', y='SuicideCount', hue='RegionName', style='Sex', markers=True, dashes=False)
    plt.title('Suicide Counts Over Time by Region and Gender')
    plt.xlabel('Year')
    plt.ylabel('Total Suicide Count')
    plt.legend(title='Region')
    plt.show()

def plot_total_suicides_over_time_by_region(df):
    region_time_suicides = df.groupby(['RegionName', 'Year'])['SuicideCount'].sum().reset_index()
    plt.figure(figsize=(12, 8))
    sns.lineplot(data=region_time_suicides, x='Year', y='SuicideCount', hue='RegionName', markers=True)
    plt.title('Total Suicides Over Time by Region')
    plt.xlabel('Year')
    plt.ylabel('Total Suicide Count')
    plt.legend(title='Region')
    plt.show()

def plot_suicide_counts_by_gender(df):
    for sex in [1, 0]:  # 1 for Male, 0 for Female
        gender_df = df[df['Sex'] == sex]
        gender_str = 'Men' if sex == 1 else 'Women'
        region_time_suicides_gender = gender_df.groupby(['RegionName', 'Year'])['SuicideCount'].sum().reset_index()
        plt.figure(figsize=(12, 8))
        sns.lineplot(data=region_time_suicides_gender, x='Year', y='SuicideCount', hue='RegionName')
        plt.title(f'Total Suicide Counts Over Time for {gender_str} by Region')
        plt.xlabel('Year')
        plt.ylabel('Total Suicide Count')
        plt.legend(title='Region')
        plt.show()
