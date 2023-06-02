class Mutable:
    """
    Small little class that lets us transport data into functions and things as a reference instead of value
    """

    def __init__(self, data: any = None):
        """Init method

        :param data: The data to hold in the class 
        :type data: any
        """
        self.data = data

    def set(self, data: any) -> None:
        """
        This sets the internal data

        :param data: The data to set to
        :type data: any
        """
        
        self.data = data
    
    def get(self) -> any:
        """
        Gets the data stored

        :return: The data stored in this class
        :rtype: any
        """

        return self.data