#Liam Robb, lr2hb, Python3; Collaborator: Patrick Burke
import math

def median_func(sorted_x):
    m = 0
    if len(sorted_x) == 0:
        return 0
    if len(sorted_x) % 2 == 0:
        m = (sorted_x[len(sorted_x) // 2][0] + sorted_x[(len(sorted_x) // 2) - 1][0]) / 2
    else:
        m = sorted_x[len(sorted_x) // 2][0]
    return m

def distance(pair):
    return math.sqrt((pair[1][0] - pair[0][0])*(pair[1][0] - pair[0][0]) + (pair[1][1] - pair[0][1])*(pair[1][1] - pair[0][1]))

def merge(list1, list2):
    both = []
    index_1 = 0
    index_2 = 0
    while len(list1) > index_1 and len(list2) > index_2:
        if list1[index_1][1] < list2[index_2][1]:
            both.append(list1[index_1])
            index_1 += 1
        else:
            both.append(list2[index_2])
            index_2 += 1
    #add the list that ended early, but we don't know which one it was
    both += list1[index_1:]
    both += list2[index_2:]
    return both


def tom_runway_value(pts):

    if len(pts) == 2:
        #sorting small base cases
        if (pts[0][1] <= pts[1][1]):
            return [distance(pts), pts]
        else:
            return [distance(pts), [pts[1], pts[0]]]
    elif len(pts) == 3: #gutting
        pts.sort(key=lambda x: x[1]) # created my own sorting function, but that seemed to be the problem
        helper_min = min(distance([pts[0],pts[1]]), distance([pts[0],pts[2]]), distance([pts[1],pts[2]]))
        return [helper_min, pts]
    else:

        left = tom_runway_value(pts[0:len(pts)//2])
        right = tom_runway_value(pts[len(pts)//2:])    #took out len(pts)

        y_merge = merge(left[1],right[1])

        md = median_func(y_merge)

        cur_min = min(left[0],right[0])

        y_merge = remove_far(md,cur_min,y_merge)

        val = the_runway_boys(cur_min, y_merge)

        return [val, y_merge]


def remove_far(median, delta, list):
    close_by_y = []
    for i in list:
        if distance([i, [median,i[1]]]) <= delta:
            close_by_y.append(i)
    return close_by_y

def the_runway_boys(best_value_from_left_and_right, list):
    beat_this_value = best_value_from_left_and_right
    iter_run = 0
    while len(list) > iter_run:

        for i in range(1,15):
            if len(list) <= iter_run + i:
                break
            if distance([list[iter_run],list[iter_run+i]]) < beat_this_value:
                beat_this_value = distance([list[iter_run],list[iter_run+i]])

        iter_run += 1
    return beat_this_value

fromfile = open("garden.txt", 'r')

num_tomatoes = int(fromfile.readline())

points = fromfile.readlines()

listXY = []

for i in range(0,num_tomatoes):
    a = points[i].split(" ")
    listXY.append((float(a[0]),(float(a[1]))))

listXY.sort()

print(tom_runway_value(listXY)[0])
