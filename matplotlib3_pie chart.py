from matplotlib import pyplot as plt


def create_the_first_pie_chart():
    plt.style.use('fivethirtyeight')

    slices = [59219, 55466, 47544, 36443, 35917]
    labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
    explode = [0, 0, 0, 0.1, 0]

    plt.pie(slices, labels=labels, explode=explode,
            shadow=True, startangle=0, autopct='%1.1f%%',
            wedgeprops={'edgecolor': 'black'})

    plt.title('My First Pie Chart')
    plt.tight_layout()

    return plt.show()


create_the_first_pie_chart()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
