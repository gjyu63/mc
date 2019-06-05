from interface import implements, Interface


class AbstractClassifier(Interface):

    """
    @param: image: a numpy 2d image. Should follow the rule of 'concrete classifier
    @return: a map of child-name -> probability
    """
    def classify(self, image):
        pass

    """
    @param: None
    @return: a list of pointers to children
    """
    def get_children(self):
        pass
