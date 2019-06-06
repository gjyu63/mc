from interface import implements, Interface
import abstract_classifier, time


class Classifier1 (implements(abstract_classifier.AbstractClassifier)):

    def __init__(self, children):
        self.children = children

    # must be sorted
    def get_children(self):
        return self.children

    def classify(self, image):
        # classify with respect to its direct child
        self.children
        print('classifying...1')
        time.sleep(1)

        res = {}
        for i, child in enumerate(self.children):
            res[child] = 0.8 if i == 0 else 0.2

        self.children = sorted(self.children, key=lambda x: res[x], reverse=True)

        return res


class Classifier2 (implements(abstract_classifier.AbstractClassifier)):

    def __init__(self, children):
        self.children = children

    # must be sorted
    def get_children(self):
        return self.children

    def classify(self, image):
        # classify with respect to its direct child
        self.children
        print('classifying...2')
        time.sleep(1)

        res = {}
        for i, child in enumerate(self.children):
            if i == 0: res[child] = 0.3
            elif i == 2: res[child] = 0.2
            else: res[child] = 0.2
        self.children = sorted(self.children, key=lambda x: res[x])

        return res



class Classifier3 (implements(abstract_classifier.AbstractClassifier)):

    def __init__(self, children):
        self.children = children

    # must be sorted
    def get_children(self):
        return self.children

    def classify(self, image):
        # classify with respect to its direct child
        self.children
        print('classifying...3')
        time.sleep(1)

        res = {}
        for i, child in enumerate(self.children):
            if i == 0: res[child] = 1
        self.children = sorted(self.children, key=lambda x: res[x])

        return res


class Classifier4 (implements(abstract_classifier.AbstractClassifier)):

    def __init__(self, children):
        self.children = children

    # must be sorted
    def get_children(self):
        return self.children

    def classify(self, image):
        # classify with respect to its direct child
        self.children
        print('classifying...4')
        time.sleep(1)

        res = {}
        for i, child in enumerate(self.children):
            if i == 0: res[child] = 1
        self.children = sorted(self.children, key=lambda x: res[x])

        return res


class Classifier5 (implements(abstract_classifier.AbstractClassifier)):

    def __init__(self, children):
        self.children = children

    # must be sorted
    def get_children(self):
        return self.children

    def classify(self, image):
        # classify with respect to its direct child
        self.children
        print('classifying...5')
        time.sleep(1)

        res = {}
        for i, child in enumerate(self.children):
            if i == 0: res[child] = 1
        self.children = sorted(self.children, key=lambda x: res[x])

        return res


class Classifier6 (implements(abstract_classifier.AbstractClassifier)):

    def __init__(self, children):
        self.children = children

    # must be sorted
    def get_children(self):
        return self.children

    def classify(self, image):
        # classify with respect to its direct child
        self.children
        print('classifying...6')
        time.sleep(1)

        res = {}
        for i, child in enumerate(self.children):
            if i == 0: res[child] = 1
        self.children = sorted(self.children, key=lambda x: res[x])

        return res
