class Phase():

    def __init__(self, flow, cvs, linearVel, time, bufferName, bufferCost, residenceTime) -> None:
        self.flow = flow
        self.cvs = cvs
        self.linearVel = linearVel
        self.time = time
        self.bufferName = bufferName
        self.bufferCost = bufferCost
        self.rt = residenceTime

        return None
