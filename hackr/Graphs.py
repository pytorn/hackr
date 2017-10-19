import matplotlib.pyplot as plt
# Matplotlib module has been used for plotting
# Class plot1 has been made to plot given coordinates in different graph styles
# For each graph style a function has been defined
# For saving the figure a function has been defined , You have to provide the full path
# For example in Ubuntu , /home/username/filename.png
# The program is totally user Interactive


class plot1():
    formatdic = {'-', '.', 'o', '+', 'd'}
    colordic = {'Blue': 'b', 'Green': 'g', 'Red': 'r', 'Cyan': 'c', 'Yellow': 'y'}

    def scatterplot(self, xcord, ycord, col, path):
        '''
        :param xcord:It is a list of x coordinates
        :param ycord: It is a list of y coordinates
        :param col: Enter color name ,for example Green ,Red , Cyan etc.
        '''
        plt.scatter(xcord, ycord, color=col, label='Change')
        plt.title('Scatter Plot')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        self.savefig(self, path)
        plt.show()
        # self.savefig()

    def barplot(self, xcord, ycord, col, path):
        '''
        :param xcord:It is a list of x coordinates
        :param ycord: It is a list of y coordinates
        :param col: Enter color name ,for example Green ,Red , Cyan etc.
        '''
        plt.bar(xcord, ycord, color=col, label='Change')
        plt.title('Bar Plot')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        self.savefig(self, path)
        plt.show()

    def histplot(self, bin1, values, col, path):
        '''
        :param xcord:It is a list of x coordinates
        :param ycord: It is a list of y coordinates
        :param col: Enter color name ,for example Green ,Red , Cyan etc.
        '''

        plt.hist(values, bin1, color=col, label='Change')
        plt.title('Histogram')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        self.savefig(self, path)
        plt.show()

    def lineplot(self, xcord, ycord, col, format1, path):
        '''
        :param xcord: It is a list of x coordinates
        :param ycord:  It is a list of y coordinates
        :param col: Enter color name ,for example Green ,Red , Cyan etc.
        :param format1: Enter format style for points ,for example 'd' for diamond ,'+' for plus sign , 'o' for circle
        '''

        plt.plot(xcord, ycord, color=col, label='Change', marker=format1)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        self.savefig(self, path)
        plt.show()

    def savefig(self, path):
        '''
        :param path: It is the full path describing where you want to store fig
        '''
        plt.savefig(path)

# Test Case
# if __name__ == '__main__':
#     plot1.scatterplot(plot1,[1,2,3],[4,5,6],'g','/home/shubhi/c1.png')
