# -*- coding: utf-8 -*-
import shagekiou

################################################################################
########################### Class for Tracing Execution ########################
################################################################################

class TraceRecord(object):
    """
    A class for storing the trace of an algorithm, to be exported and displayed
    using the HTML visualizer.
    """

    def __init__(self):
        """
        Initialize the trace to empty.

        RUNTIME: O(1)
        """

        self.sequence = []

    def calculatingUpperbound(self,upperbound):
        self.sequence.append(
            {
             "status": "calculatingUpperbound",
             "value": upperbound
            })

    def settingRight(self, right):
        self.sequence.append(
            {
            "status": "settingRight",
             "value": right
            })

    def settingLeft(self, left):
        self.sequence.append(
            {
            "status": "settingLeft",
             "value": left
            })

    def calculatingMid(self, mid):
        self.sequence.append(
            {
            "status": "calculatingMid",
            "value": mid
            })

    def drawMid(self):
        self.sequence.append(
            {
            "status": "drawMid",
            })        

    def isAboveOriginalHeight(self, ok):
        self.sequence.append(
            {
            "status": "isAboveOriginalHeight",
            "value": ok
            })        

    def isKaboomedBelowMid(self, index, isBelow):
        self.sequence.append(
            {
            "status": "isKaboomedBelowMid",
            "value": [index, isBelow]
            })

    def answerFound(self):
        self.sequence.append(
            {
            "status": "answerFound"
            })