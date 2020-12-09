#Call two arms equally strong if the heaviest weights they each are able to lift are equal....

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}