from interface import implements, Interface


class AbstractClassifier(Interface):

    def classify(self, image):
        """
        @param: image: a numpy 2d image. Should follow the rule of 'concrete classifier
        @return: a map of child-name -> probability
        """
        pass

    def get_children(self):
        """
        @param: None
        @return: a list of pointers to children
        """
        pass
