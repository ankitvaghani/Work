def flatten(dictionary):
    # your code here
    #print (dictionary)
    for key,value in dictionary.items():
        print("key:",key)
        print("value:",value)
        
        if type(value) == dict:
            
            k = value.keys()
            v = value.values()
            print('key inside:',k)
            print('val inside:',v)
            
    return dictionary


if __name__ == '__main__':
    #test_input = {"key": {"deeper": {"more": {"enough": "value"}}}, "abx" : "123"}
    #print('Input: {}'.format(test_input))
    #print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}, "abx" : "123"}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
