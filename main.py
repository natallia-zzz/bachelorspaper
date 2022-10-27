# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import meshpy as mp
import json
import sys

def file_analysis(path):
    f = open(path)
    data = json.load(f)
    return data['shapes']


def cell_area(pts):
    sys.path.append('/Users/natalliazzz/Downloads/BSU MMF/2coursepaper')
    import volume
    print(volume.area_of_triangle(pts[0], pts[1], pts[2]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_analysis("Segmented 2/3.json")
    cell_area([[1,2], [3,3],[2,1]])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
