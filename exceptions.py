#following function will decompress your array of elements
def decompress(compressed_elements):
    '''
    
    >>>decompress([(1, '1'), (2, 'test'), (3, '2')])
    [1, 2, 2, 2, test, test]
    
    >>>decompress[(2, 'test')]
    [test, test]
    
    >>>decompress[()]
    'Sorry. There is not enough elements in your array'
    '''
    
    decompressed_elements = []
    if len(compressed_elements) > 0:
        for i in range (len(compressed_elements)):
            for j in range(compressed_elements[i][0]):
                decompressed_elements.append(compressed_elements[i][1])
    
        return decompressed_elements
    else:
        raise ValueError("Can't decompress an empty sequence")

print('Hi')
try:
    f = open('my.db', 'r')
    d = eval(f.read())
except FileNotFoundError as e:
    d = {}
print(d)
    
print('Bye')