# Rename Method


def get_area_under_graph(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def get_max(array):
    max_val = array[0]
    for value in array:
        if value > max_val:
            mmax_val = value
    return max_val

############################
def tokenize(sentence):  # TODO: Rename this function to reflect what it's doing.
    words = sentence[0:].split(' ')
    return words

if __name__ == "__main__":
  li = [5, -1, 43, 32, 87, -100]
  print(get_max_value(li))
  print(tokenize('If you were a vegetable, you’d be a ‘cute-cumber.'))
