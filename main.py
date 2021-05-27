# -*- coding: utf-8 -*-
import sys
import shagekiou
import trace
import algorithms
import json
import utils


#*****************************射撃王御用*****************************
def loadProblem(file = "problem.py", variable = "problem_params"):

    """
    Loads a matrix from a python file, and constructs a PeakProblem from it.
    """

    namespace = dict()
    with open(file) as handle:
        exec(handle.read(), namespace)
    return shagekiou.createProblem(namespace[variable])
#*****************************射撃王御用*****************************

def main():
    #*****************************射撃王御用*****************************
    if len(sys.argv) > 1:
        problem = loadProblem(sys.argv[1])
    else:
        problem = loadProblem(utils.getOpenFilename("problem.py"))

    # run 射撃王 algorithm, gathering the traces and printing out the results as
    # we go
    algorithm = algorithms.algorithm1

    steps = []

    tracer = trace.TraceRecord()

    # What, if any, should be the return value of shagekiou algorithm?
    shagekiou = algorithm(problem, trace = tracer)
    steps.append(tracer.sequence)
    
    # status = "is NOT a peak (INCORRECT!)"
    # if problem.isPeak(peak):
    #     status = "is a peak"

    # print(name + " : " + str(peak) + " => " + status)

    # write the trace out to a file
    with open("trace.jsonp", "w") as traceFile:
        traceFile.write("parse(")

        json.dump({
            "input" : [problem.height, problem.rising_speed],
            "steps" : steps
        }, traceFile)

        traceFile.write(")")
    #*****************************射撃王御用*****************************

if __name__ == "__main__":
    main()
