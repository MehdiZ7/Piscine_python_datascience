def ft_filter(function, iterable):
    '''Return an iterator yielding those items of iterable for which
    function(item) is true.  If function is None, return the items that
    are true.'''
    ret = iter([c for c in iterable if
                (c if function is None else function(c))])
    return ret


def main():
    '''This main is only here for you, dear correcter'''
    print(list(ft_filter(lambda x: x % 2 == 0, range(10))))
    print(list(filter(lambda x: x % 2 == 0, range(10))))
    print(list(ft_filter(None, [0, 1, "", "a", [], [0], None, 3])))
    print(list(filter(None, [0, 1, "", "a", [], [0], None, 3])))


if __name__ == "__main__":
    main()
