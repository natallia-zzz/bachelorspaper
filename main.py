# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from meshpy.triangle import MeshInfo, build
import json
import sys


def file_analysis(path):
    f = open(path)
    data = json.load(f)
    return data['shapes']


def mesh_partition(pts):
    mesh_info = MeshInfo()
    mesh_info.set_points(pts)
    facets = [[i, i+1] for i in range(len( pts))]+ [[len(pts)-1,0]]
    mesh_info.set_facets(facets)
    mesh = build(mesh_info)
    return mesh


def cell_area(pts):
    sys.path.append('/Users/natalliazzz/Downloads/BSU MMF/2coursepaper')
    import volume
    area = 0;
    for p in pts:
        area += volume.area_of_triangle(p[0], p[1], p[2])
    return area


def mesh_to_points(m):
    pts = []
    for i in range(len(m.elements)):
        pts += [[m.points[m.elements[i][0]],m.points[m.elements[i][1]],m.points[m.elements[i][2]]]]
    return pts


def print_areas(data):
    for i in data:
        mesh = mesh_partition(i['points'])
        pts = mesh_to_points(mesh)
        print(i["label"],cell_area(pts))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = file_analysis("Segmented 2/pepe3 10mcl - Aocul - 20Xspec.json")
    points = data[5]['points']
    mesh = mesh_partition(points)
    meshFile = {'points': [i for i in mesh.points], 'elements': [i for i in mesh.elements]}
    with open('resultpepe3.json', 'w') as fp:
        json.dump(meshFile, fp)
    pts = mesh_to_points(mesh)
    print(cell_area(pts))
    print_areas(data)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
