try:
    count = int(input("How many numbers you to want to capture? "))
    numList = []
    for i in range(count):
        msg = 'Enter number #' + str(i) + ' '
        num = int(input(msg))
        numList.append(num)
    print('The lowest number in the list', min(numList))
    print('The highest number in the list', max(numList))
    print('The total of the numbers in the list', sum(numList))
    print('The average of the numbers in the list', sum(numList)/len(numList))
except ValueError:
    print('Error with the numbers')
except ZeroDivisionError:
    print('Zero division error')
except:
    print('unknown error')
else:
    if len(numList) > 0:
        print('The item in the List: ')
        for i in range(len(numList)):
            print(numList[i])
finally:
    print('End')
