import classifers, abstract_classifier


def run(root):

    images = []
    image = None # for image in images: ...

    stack = [root]
    while stack:
        classifier = stack.pop()
        # visit node
        prob_map = classifier.classify(image)
        if len(prob_map.keys()) == 1:
            return prob_map

        # check if that classifier is confused or not
        # find the highest probability,
        max_k, max_v = None, 0
        for k,v in list(prob_map.items()):
            if v > max_v:
                max_k, max_v = k, v

        if max_v < 0.4:
            second_highest = stack.pop().get_children()[1]
            stack.append(second_highest)
        else:
            stack.append(max_k)

    return None  # shouldn't


if __name__ == '__main__':
    root_classifier = None
    run(root_classifier)