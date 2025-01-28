def add(str):
    delimiter=","
    totalSum =0
    neg_numbers = []
    if len(str) >3 and "//"  ==str[:2]:
        delimiter = str[2]
        str = str[3:]
    for s in str.split(delimiter):
        for  k in s.split("\n"):
            if k and int(k) <0:
                neg_numbers.append(k)
            elif k:
              totalSum = totalSum+int(k)
    print(totalSum)
    if neg_numbers:
       raise "negative numbers not allowed "+",".join(neg_numbers)
    else:
        return totalSum

assert add("")==0,"return not zero"
assert add("1") ==1 ,"return not 1"
assert add( "1,5") ==6 ,"return not 6"
assert add("//;\n1;2") ==3 , "return not 3"



    
    


    
