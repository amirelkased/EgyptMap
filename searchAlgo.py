import time

import pandas as pd
import tkintermapview
from geopy.distance import distance

from AdjcencyList import graph

df = pd.read_csv("Photo/All_Data_5.csv")
city = list(df["name"].values)
lat = list(df["lat"].values)
lng = list(df["lng"].values)
G = graph()


def city_location(c):
    return list(df[(df["name"] == c)][["lat", "lng"]].values.ravel())


def find_city(sub_string):
    return [*filter(lambda x: sub_string.upper() in x.upper(), city)]


def heuristic(goal):
    htable = dict()
    for i in city:
        htable[i] = distance(city_location(goal), city_location(i)).kilometers
    return htable


def wigtedGraph(ADJ):
    allAdjDict_2 = dict()
    for x in city:
        b = [*map(lambda x: x[0], list(ADJ[x].values()))]
        n = list(ADJ[x].keys())
        allAdjDict_2[x] = [(n[i], b[i]) for i in range(len(b))]
    return allAdjDict_2


def showTime(sec):
    x = time.gmtime(sec + (2 * 3600) + time.time())

    if x.tm_hour > 12:
        x = time.gmtime(sec + (14 * 3600) + time.time())
        s = str(f"{x.tm_hour}:{x.tm_min}:{x.tm_sec} PM")
    else:
        s = str(f"{x.tm_hour}:{x.tm_min}:{x.tm_sec} AM")

    return s


def unWigtedGraph(ADJ):
    bfsGraph = dict()
    for i in city:
        bfsGraph[i] = list(ADJ[i].keys())
    return bfsGraph


def drawPath(result_path, mapFram):
    map_widget = tkintermapview.TkinterMapView(mapFram, width=850, height=500)
    map_widget.place(x=25, y=175)
    t = []
    dis = []
    allAdjDict = graph()
    map_widget.set_position(city_location(result_path[0])[0], city_location(result_path[0])[1], marker=True,
                            text=result_path[0])
    map_widget.set_zoom(9)

    for i in range(len(result_path) - 1):
        x = allAdjDict[result_path[i]][result_path[i + 1]][1]
        t.append(x)
        d = allAdjDict[result_path[i]][result_path[i + 1]][0]
        dis.append(d)
        map_widget.set_marker(city_location(result_path[i])[0], city_location(result_path[i])[1], text=result_path[i])

    map_widget.set_marker(city_location(result_path[len(result_path) - 1])[0],
                          city_location(result_path[len(result_path) - 1])[1], text=result_path[len(result_path) - 1])
    message1 = f"if you travel from now you will arrive at {showTime(sum(t))}\nThe total distance will be " + (
            "%.3f" % sum(dis)) + " KM"
    map_widget.set_path([*map(city_location, result_path)])
    return message1


def bfs(start, goal, graph=unWigtedGraph(G)):
    visitted = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visitted:
            continue

        visitted.append(node)
        if node == goal:
            return path, visitted
        else:
            adjnodes = graph.get(node, [])
            for i in adjnodes:
                newPath = path.copy()
                newPath.append(i)
                queue.append(newPath)


def dfs(start, goal, graph=unWigtedGraph(G)):
    visitted = []
    stack = [[start]]
    while stack:
        path = stack.pop(-1)
        node = path[-1]
        if node in visitted:
            continue

        visitted.append(node)
        if node == goal:
            return path, visitted
        else:
            adjnodes = graph.get(node, [])
            for i in adjnodes:
                newPath = path.copy()
                newPath.append(i)
                stack.append(newPath)


def pathCost(path):
    totalCost = 0;
    for node, cost in path:
        totalCost += cost
    return totalCost, path[-1][0]


def uCost(start, goal, graph=wigtedGraph(G)):
    visitted = []
    queue = [[(start, 0)]]
    path = [(start, 0)]
    while queue:
        queue.sort(key=pathCost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visitted:
            continue

        visitted.append(node)
        if node == goal:
            return [*map(lambda l: l[0], path)], visitted

        else:
            adjnodes = graph.get(node, [])
            for node2, cost in adjnodes:
                newPath = path.copy()
                newPath.append((node2, cost))
                queue.append(newPath)


def aStar(start, goal, graph=wigtedGraph(G)):
    hTable = heuristic(goal)

    def path_cost(path):
        gCost = 0
        for node, cost in path:
            gCost += cost
        lastNode = path[-1][0]
        fCost = gCost + hTable[lastNode]
        return fCost, lastNode

    visitted = []
    queue = [[(start, 0)]]
    path = [(start, 0)]
    while queue:
        queue.sort(key=path_cost)  # sorting the queue using Fcost and sorting by alphabet if equal Fcost
        path = queue.pop(0)
        node = path[-1][0]
        if node in visitted:
            continue

        visitted.append(node)
        if node == goal:
            return [*map(lambda l: l[0], path)], visitted

        else:
            adjnodes = graph.get(node, [])
            for node2, cost in adjnodes:
                newPath = path.copy()
                newPath.append((node2, cost))
                queue.append(newPath)
