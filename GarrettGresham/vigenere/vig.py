import sys


if (len(sys.argv) > 3 or len(sys.argv) == 1):
    print("Usage: 'vig.py -e(encode) <key>' OR 'vig.py -d(dencode) <key>'")
    quit()

charl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
charc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

key = str(sys.argv[2])
MODE = str(sys.argv[1])

while True:
    try:
        work_str = input()
    except EOFError:
        quit()
    
    if MODE not in ["-e","-d"]:
        print("Please enter a valid mode: 'vig.py -e(encode) <key>' OR 'vig.py -d(dencode) <key>'")
        quit()

    keyl = list(key)
    strl = list(work_str)
    temp = []
    dkey = []

    # converting given mesage char list to a number list, 
    capch = [] # <- used to track capitalization
    for char in strl:
        if char in charl:
            temp.append(charl.index(char))
            capch.append(0)
        elif char in charc:
            temp.append(charc.index(char))
            capch.append(1)
        else:
            # symbol/number handling
            temp.append(char)
            capch.append(0)
            
    #print(capch)

    # converting given key char list to a number list,
    for char in keyl:
        if char in charl:
            dkey.append(charl.index(char))
        elif char in charc:
            dkey.append(charc.index(char))
        else:
            # space/symbol handeling for key
            temp.append(None)

    #print(temp)
    #print(dkey)

    # encoding of the message
    space_offset = 0 
    coded = []
    for i in range(0,len(temp)):
        wkey = (i + space_offset)%len(dkey)
        if dkey[wkey] == None:
            # used to ignore key spaces
            continue
        if isinstance(temp[i],int):

            if (MODE == "-e"):
                coded.append((temp[i] + dkey[wkey]) % 26)
            elif (MODE == "-d"):
                coded.append((26 + temp[i] - dkey[wkey]) % 26)
            else:
                print("Please enter a valid mode: 'vig.py -e(encode) <key>' OR 'vig.py -d(dencode) <key>'")
                quit()
            

        else:
            # used to handle message spaces/symbols and apply an offset
            coded.append(temp[i])
            space_offset += 2
    
    #print(coded)

    # conversion of codd mesage to text
    out = []
    for i in range(0,len(coded)):
        if not isinstance(coded[i],int):
            # used to handle message spaces/symbols
            out.append(coded[i])
        elif capch[i] == 0:
            out.append(charl[coded[i]])
        else:
            out.append(charc[coded[i]])
    
    #print(out)
    # actual print out
    print(''.join(out))

    
