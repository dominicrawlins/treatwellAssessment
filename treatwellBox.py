################################################
####  Dominic Rawlins Treatwell assessment #####
#                                              #
# use command 'python3 treatwellBox.py' with   #
# different arguments to run.                   #
#                                              #
# To test: 'python3 treatwellBox.py test'      #
#                                              #
# To draw box: 'python3 treatwellBox.py w h'   #
# where w and h are the integer width and      #
# height                                       #
################################################



import sys

#w=2 h=2
testString1 = []
#w=2 h=3
testString2 = []
#w=3 h=2
testString3 = []
#w=3 h=3
testString4 = []

#append characters to create strings to test method against
def createTestStrings():
    #w=2 h=2
    testString1.append(u'\u250c' + u'\u2510')
    testString1.append(u'\u2514' + u'\u2518')

    #w=2 h=3
    testString2.append(u'\u250c' + u'\u2510')
    testString2.append('||')
    testString2.append(u'\u2514' + u'\u2518')

    #w=3 h=2
    testString3.append(u'\u250c' + '-' + u'\u2510')
    testString3.append(u'\u2514' + '-' + u'\u2518')

    #w=3 h=3
    testString4.append(u'\u250c' + '-' + u'\u2510')
    testString4.append('| |')
    testString4.append(u'\u2514' + '-' + u'\u2518')

#start testing
def runTests():
    print("testing\n\n")
    #create global strings ready for use
    createTestStrings()
    #create lists so tests can use loop to print and run
    testPrint = ['w=2 h=2', 'w=2 h=3', 'w=3 h=2', 'w=3 h=3']
    testStrings = [testString1, testString2, testString3, testString4]
    #weights for each test in 2s e.g. at index 0 and 1 are for test 1, 2 and 3 are for test 2 etc.
    testWeights = [2, 2, 2, 3, 3, 2, 3, 3]
    testsPassed = 0
    for i in range(4):
        print("testing:", testPrint[i])
        w = testWeights[i * 2]
        h = testWeights[(i*2) + 1]
        #test if method is correct by comparing to right answer
        testedBox = createBox(w, h)
        if(testedBox == testStrings[i]):
            print("test passed\n")
            testsPassed += 1
        else:
            print("test failed")
    print("number of tests passed:", testsPassed, "/ 4")


def createBox(w, h):
    #indices used for edge characters
    edgeW = [0, w-1]
    edgeH = [0, h-1]
    #create character dictionary
    charDict = {}
    #input edge cases
    charDict[(w*(h-1)) + (w-1)] = u'\u2518'
    charDict[w-1] = u'\u2510'
    charDict[0] = u'\u250c'
    charDict[w*(h-1)] = u'\u2514'
    #add sides of box
    for col in edgeW:
        for row in range(1, h-1):
            charDict[(row*(w)) + col] = '|'
    #add top and bottom of box
    for col in range(1, w-1):
        for row in edgeH:
            key = (row*(w)) + col
            charDict[key] = '-'

    #turn box to list of strings
    boxStrings = []
    for row in range(h):
        rowString = ""
        for col in range(w):
            key = (w*row) + col
            if(key in charDict):
                rowString += charDict[key]
            else:
                rowString += " "
        boxStrings.append(rowString)


    return boxStrings

#print box out
def drawBox(boxStrings):
    for row in boxStrings:
        print(row)

if __name__ == "__main__":
    #if argument is test then test
    if(len(sys.argv) == 2 and sys.argv[1] == 'test'):
        runTests()
    #if 2 arguments present then run draw box
    elif(len(sys.argv) == 3):
        w = int(sys.argv[1])
        h = int(sys.argv[2])

        boxStrings = createBox(w, h)
        drawBox(boxStrings)
