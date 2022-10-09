import sys
from functools import reduce


print(sys.version)

print('This programme collects your name followed by age , school house and reaction times')

# sample data set to test
stuDataSet = {'Martin': [12, 'mars', 4], 'Simon': [12, 'saturn', 3], 'Gab': [11, 'saturn', 6], 'Nat': [11, 'saturn', 2]}


def stuInfo(stuName: object, stuAge: object, stuHouse: object, stuReactTime: object, stuDict: object) -> object:
    """
    :param stuName:
    :param stuAge:
    :param stuHouse:
    :param stuReactTime:
    :param stuDict:
    :return:

    """
    stuDict[stuName] = [stuAge, stuHouse, stuReactTime]
    return stuDict


def sortByReactionTimeByHouse(stuStore: dict) -> object:
    """
    :return:
    :type stuStore: object
    """
    lst = list()
    tup = tuple()

    for stuName, stuData in stuStore.items():
        tup = (stuData[2], stuData[1], stuData[0], stuName)
        lst.append(tup)

    lst = sorted(lst)
    # if required reverse the list
    # revlst = list()
    # revlst = sorted(lst, reverse=True)
    # print(revlst)

    print(f"shortest reaction time is: {min(lst)[0]} seconds for student: {min(lst)[3]} \nWell done {min(lst)[3]}!")
    print(f"longest reaction time is: {max(lst)[0]} seconds for student: {max(lst)[3]} \nNever give up {max(lst)[3]}!")

    return


def OutputAvgReactionTime(stuStore: dict) -> object:
    """
    :rtype: object
    :param stuStore:
    :return:
    """
    sumReactTime: int = 0

    for stuName, stuData in stuStore.items():
        sumReactTime = sumReactTime + stuData[2]

    print('Average reaction time of students is {}'.format( sumReactTime / len(stuStore)), 'seconds for a group of {} students'.format(len(stuStore)))

    return


def GroupByHouse(stuStore: dict)  -> object:
    """

    :param stuStore:
    :return:
    """
    avgReacTimeMars: int = 0
    avgReacTimeSat: int = 0
    stuCntMars: int = 0
    stuCntSat: int = 0


    lst = list()
    tup = tuple()



    for stuName, stuHouse in stuStore.items():
        tup = (stuHouse[1], stuHouse[2])
        lst.append(tup)

        # method 1
        if stuHouse[1] == 'mars':
            avgReacTimeMars = avgReacTimeMars + stuHouse[2]
            stuCntMars = stuCntMars+1
        elif stuHouse[1] == 'saturn' :
            avgReacTimeSat = avgReacTimeSat + stuHouse[2]
            stuCntSat = stuCntSat + 1

    print(lst)


    """
    method 2
        @docstring
         1. convert the view returned from filter operation  to list 
         2. use that list to extract second element from the new filtered list into a single element list
         3. can use item index search within [] 
         4. can use zip to unzip using *
         5. can use itemgetter with map function   
        
    """
    lst_mars = list(filter(lambda hname: hname[0] == 'mars'.casefold(), lst))

    lst_sat = list(filter(lambda hname: hname[0] == 'saturn'.casefold(), lst))

    print(lst_mars)
    print(lst_sat)

    mtime = list([it[1] for it in lst_mars])
    print(mtime)
    a, b = list(zip(*lst_mars))
    # print (zip(*list(lst_mars))[1])
    # print(list(map(itemgetter(1), list(lst_sat))))

    stime = [it[1] for it in lst_sat]
    print(stime)
    # print(zip(*lst_sat)[1])

    avgMars = reduce(lambda rtime1, rtime2: rtime1 + rtime2, mtime)
    # avgMars = reduce(operator.add, mtime)

    avgSat = reduce(lambda rtime1, rtime2: rtime1 + rtime2, stime)
    # avgSat = reduce(operator.add, stime)


    print(f'Average reaction times for Mars:{avgReacTimeMars/stuCntMars} and for Saturn: {avgReacTimeSat/stuCntSat}' )
    print(f'Average reaction times Using complex method for Mars:{avgMars/len(lst_mars)} and for Saturn: {avgSat/len(lst_sat)}')

    return


def RunProg() -> object:
    """
    :rtype: object
    :return:
    """
    stuStore = dict()

    yn = input('use existing dataset or create from scratch y/n?:')

    if yn == 'n' :
        n = int(input('Provide number of student dataset to be created:'))

        for i in range(0, n):
            stuName = input('Enter your first name:')
            print(stuName)

            stuAge = int(input('Enter your age:'))
            print(stuAge)

            stuHouse = input('Enter your House:')
            print(stuHouse)

            stuReaction = int(input('Enter your reaction times in seconds:'))
            print(stuReaction)

            print(stuInfo(stuName, stuAge, stuHouse, stuReaction, stuStore))

            print('sorting by reaction time and print score and house ')
    else:
        stuStore = stuDataSet

    sortByReactionTimeByHouse(stuStore)

    OutputAvgReactionTime(stuStore)

    GroupByHouse(stuStore)

    return


if __name__ == "__RunProg__":
    RunProg()

RunProg()

