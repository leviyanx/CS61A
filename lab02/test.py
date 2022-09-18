def cake():
    print('beets')

    def pie():
        print('sweets')
        return 'cake'
    return pie


def snake(x, y):
    chocolate = cake()
    more_chocolate, more_cake = chocolate(), cake

    if cake == more_cake:
        return chocolate
    else:
        return x + y
