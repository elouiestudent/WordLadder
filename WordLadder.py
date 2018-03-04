#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

import sys
import time
import collections
def findDifference(vertex,test):
    diff = 0
    for v,t in zip(vertex,test):
        if v != t:
            diff += 1
    if diff == 1:
        return True
    else:
        return False

def makeGraph(fopen,graph):
    for line in fopen:
        word = line.strip()
        graph[word] = set()
        for key in graph:
            if findDifference(key, word):
                graph[key].add(word)
                graph[word].add(key)
    return graph

def findConnectedComponents(graph):
    alreadySeen = set()
    allcomps = list()
    for key in graph:
        if key not in alreadySeen:
            comp = list()
            alreadySeen.add(key)
            parseMe = collections.deque()
            parseMe.appendleft(key)
            comp.append(key)
            while len(parseMe) > 0:
                element = parseMe.popleft()
                newSet = graph[element]
                for thing in newSet:
                    if thing not in alreadySeen:
                        alreadySeen.add(thing)
                        parseMe.appendleft(thing)
                        comp.append(thing)
            # print("comp:",comp)
            # if len(comp) > 1:
            allcomps.append(len(comp))
    return allcomps

startTime = time.clock()
fopen = open("words.txt")
graph = dict()
graph = makeGraph(fopen,graph)
print("Time to Construct:", str(time.clock() - startTime))
mosts = set()
numE = 0
greatNeighbor = 0
for thing in graph.values():
    numE += len(thing)
    if len(thing) > greatNeighbor:
        greatNeighbor = len(thing)
for key in graph:
    if len(graph[key]) == greatNeighbor:
        mosts.add(key)
print("Number of Vertices:",len(graph))
print("Number of Edges:",numE//2)
if len(sys.argv) > 1:
    vertex = sys.argv[1]
    print(vertex + "'s Neighbors:",", ".join(graph[vertex]))
print("Word(s) with Most Neighbors:", ", ".join(mosts) + ", Number of Neighbors:",greatNeighbor)
c = findConnectedComponents(graph)
# print("Connected Components:", c)
print("Number of Connected Components:",len(c))
print("Size of Largest Component:",max(c))
print("Runtime:", str(time.clock() - startTime))