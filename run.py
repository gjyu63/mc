import classifers, abstract_classifier


def run(root):

    images = []
    image = None # for image in images: ...
    stack = [root]
    while stack:
        classifier = stack[-1]
        # visit node
        prob_map = classifier.classify(image)

        # the leaf
        # by convention a leaf category contains a map with one key. the probability of that key is whatever
        if len(prob_map.keys()) == 1:
            return prob_map

        # check if that classifier is confused or not
        # find the highest probability,
        max_k, max_v = None, 0
        for k, v in list(prob_map.items()):
            if v > max_v:
                max_k, max_v = k, v

        if max_v < 0.4:
            # backtrack to its parent
            stack.pop()
            second_highest = stack[-1].get_children()[1]
            stack.append(second_highest)
        else:
            stack.append(max_k)

    return None  # shouldn't


if __name__ == '__main__':

    cf4, cf5, cf6, cf3 = classifers.Classifier4([]), classifers.Classifier5([]), classifers.Classifier6([]), classifers.Classifier3([])
    cf2 = classifers.Classifier2([cf4, cf5, cf6])
    root_classifier = classifers.Classifier1([cf2, cf3])

    run(root_classifier)