#!/bin/env python3


def add(array1, array2):
    outputarray = []
    for rows in zip(array1, array2):
        row = []
        for line in zip(rows[0], rows[1]):
            row.append(line[0] + line[1])
        outputarray.append(row)

    return outputarray
