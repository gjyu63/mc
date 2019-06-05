from interface import implements, Interface
import abstract_classifier, time


class Classifier1 (implements(abstract_classifier)):

    def __init__(self):
        self.children = []

    # must be sorted
    def get_children(self):
        return self.children

    def classify(self, image):
        # classify with respect to its direct child
        self.children
        time.sleep(8)

