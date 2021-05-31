from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd


def create_bar_chart():
    plt.style.use('fivethirtyeight')

    ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    x_indeces = np.arange(len(ages_x))
    width = 0.25

    python_dev_y = [38496, 42000, 46752, 49320, 53200,
                    56000, 62316, 64928, 67317, 68748, 73752]
    plt.bar(x_indeces - width, python_dev_y, width=width, color='b', label='Python')

    c_dev_y = [45372, 48876, 53850, 57287, 63016,
               65998, 70003, 70000, 71496, 75370, 83640]
    plt.bar(x_indeces, c_dev_y, width=width, color='#adad3b', label='C')

    javascript_dev_y = [37810, 43515, 46823, 49293, 53437,
                        56373, 62375, 66674, 68745, 68746, 74583]
    plt.bar(x_indeces + width, javascript_dev_y, width=width, color='k', linestyle='--', label='Javascript')

    # Specify axis and add the title for the plot
    plt.xlabel('Ages')
    plt.ylabel('Median Salary(USD)')
    plt.title('Median Salary (USD) by Age')
    # plt.legend(['Javascript', 'Python'])   # alternative way to add legend
    plt.legend()

    plt.xticks(ticks=x_indeces, labels=ages_x)

    plt.tight_layout()  # Adjust the padding between and around subplots.

    return plt.show()

    # format_string = [marker][line][color]

    # ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
    # 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark',
    # 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
    # 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
    # 'seaborn-whitegrid', 'tableau-colorblind10']


# create_bar_chart()


def analyzing_data_from_CSVs_by_csv():
    plt.style.use('fivethirtyeight')

    with open('matplotlib2_data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # ~~ a reader but maps the information in each row
        # to a a dict whose keys are given by the optional fieldnames parameters

        language_counter = Counter()

        for row in csv_reader:
            language_counter.update(row['LanguagesWorkedWith'].split(';'))

    languages = []
    popularity = []

    for item in language_counter.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])
    languages.reverse()
    popularity.reverse()

    plt.barh(languages, popularity)

    # Specify axis and add the title for the plot
    plt.title('Most Popular Languages')
    plt.xlabel('Number of users')
    plt.tight_layout()  # Adjust the padding between and around subplots.

    return plt.show()


# analyzing_data_from_CSVs_by_csv()


def analyzing_data_from_CSVs_by_pandas():
    plt.style.use('fivethirtyeight')

    data = pd.read_csv('matplotlib2_data.csv')  # Return into DataFrame
    ids = data['Responder_id']
    lang_responses = data['LanguagesWorkedWith']

    language_counter = Counter()  # return into a dictionary

    for response in lang_responses:
        language_counter.update(response.split(';'))

    languages = []
    popularity = []

    for item in language_counter.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])
        print(item)
    languages.reverse()
    popularity.reverse()

    plt.barh(languages, popularity)

    plt.title('Most Popular Languages')
    plt.xlabel('Number of users')
    plt.tight_layout()

    return plt.show()


analyzing_data_from_CSVs_by_pandas()
