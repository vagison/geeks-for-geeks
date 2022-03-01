# Remove leading zeros from an IP address
# https://practice.geeksforgeeks.org/problems/remove-leading-zeros-from-an-ip-address3530/1

def newIPAdd(s):
    ipIntoArray = s.split('.')
    resultingIp = ""

    for element in range(0, len(ipIntoArray)):
        param = False

        for char in range(0, len(ipIntoArray[element])):
            if ipIntoArray[element][char] == "0" and param != True and char != len(ipIntoArray[element]) - 1:
                pass

            else:
                param = True
                resultingIp = resultingIp + ipIntoArray[element][char]

        resultingIp = resultingIp + "."

    resultingIp = resultingIp[0:(len(resultingIp) - 1)]

    return resultingIp
