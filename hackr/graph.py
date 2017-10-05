import matplotlib.pyplot as plt

class graph():
    """
    Safe your grap first before you use show it!
    """
    figure = None
    coordinates = {} # a dict with the coordinates or label and coordinate pair for bar graphs
    # x is the key and y is the value
    figures = [] # list of figures you can switch between

    xlabel = "x"
    ylabel = "y"
    def __init__(self, xlabel="x", ylabel="y"):
        """
        Initialize
        :param coordinates: the coordinates for the graph
        :param xlabel: label for the x axis
        :param ylabel: label for the y axis
        """
        self.figure = None
        self.xlabel = xlabel
        self.ylabel = ylabel

    def save(self, file_path, extension="png"):
        """
        Saves the figure of it exists to the png format
        :param file_path: Where to save the figure
        :param name: optional parameter if you want to create a specific name
        :param extension: optional parameter for the file type
        :return:
        """
        if self.figure is None:
            print ("You did not create a plot. Please create a plot before")
        else:
            try:
                self.figure.savefig(file_path + "." + extension)
            except IOError as e:
                print e.filename + " " + e.strerror
                print "Please specify a valid save_path"
                print "The path should end with /"

    def show(self):
        """
        Show the figure if one exists
        :return:
        """
        figure = self.figure
        if self.figure is not None:
            plt.show()
        else:
            print("You did not create a figure. Please create a figure first")

    def create_figure(self):
        """
        Creates a figure on that the graphes will be drawn. Could take size as input for example
        :return:
        """
        self.figure = plt.figure()

    def choose_figure(self, index):
        """
        Choose a figure if you created more than one so you can switch between figures
        :param index: the index of he figure you want
        :return:
        """
        try:
            self.figure = self.figures[index]
        except IndexError as e:
            print ("Index does not exist")

    def create_bar_graph(self, coordinates):
        """
        Creates a bar graph with the arguments provided.
        The dictionary contains as key the labels and then y coordinate as value
        :return: The index number of the figure if you want to show it
        """
        sp = self.figure.add_subplot(111)
        sp.bar(range(len(coordinates)), coordinates.values(), align="center")
        plt.xticks(range(len(coordinates)), coordinates.keys())
        self.figures.append(self.figure)
        self.create_figure()
        return len(self.figures) - 1


    def create_scatter_graph(self, coordinates):
        """
        Create a scatter graph,
        :param coordinates A dictionary keys are labels and the values are the x and y coodinates per label
        :return:
        """
        xs, ys = zip(*coordinates.values())
        labels = coordinates.keys()
        plt.scatter(xs, ys)
        #  TODO Decide if you want to use labels
        for label, x, y in zip(labels, xs, ys):
            plt.annotate(label, xy=(x, y))
        self.figures.append(self.figure)
        self.create_figure()
        return len(self.figures) - 1

    def create_line_graph(self, coordinates):
        """
        Create a normal line graph
        :param coordinates A dictionary keys are x coordinates and values are the y coordinates
        :return: The index of the figure that was created
        """
        x = []
        y = []

        for key, value in coordinates.iteritems():
            x.append(key)
            y.append(value)
        plt.plot(x,y)
        self.figures.append(self.figure)
        self.create_figure()
        return len(self.figures) - 1

"""
# For testing purposes
if __name__ == "__main__":
    D = {u'Label1': 26, u'Label2': 17, u'Label3': 30}
    graph1 = graph(2)
    test = {1092268: [81, 90], 524292: [80, 80], 892456: [88, 88]}
    test2 = {10: 20, 30: 40}
    # First create a figure
    graph1.create_figure()
    scatter_graph = graph1.create_scatter_graph(test)
    line_graph = graph1.create_line_graph(test2)
    bar_graph = graph1.create_bar_graph(D)
    graph1.choose_figure(scatter_graph)
    graph1.save("/home/xaver/graphs/scatter")
    #graph1.show()
    print("Fuck you Xaver")

    graph1.choose_figure(line_graph)
    graph1.save("/home/xaver/graphs/line")
    #graph1.show()

    graph1.choose_figure(bar_graph)
    graph1.save("/home/xaver/graphs/bar")
    #graph1.show()
"""