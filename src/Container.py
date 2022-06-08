
def forceList(n):
    return [n] if type(n) is int else n or [0]

class Container:
    def __init__(self, parent=None, pos=[0,0], size=[0,0], margin=[0,0,0,0], padding=[0,0,0,0]):
        """
        Pos : [x,y] <=> [0,1] | Origin = Top left
        Size : [w,h] <=> [0,1] | Origin = Top left
        Margin, padding : [top,right,bottom,left] <=> [0,1,2,3]
        """
        self.parent = parent
        self.pos = pos
        self.size = size

        # copy margin into self.margin until four elements
        # thanks to CEO#0069 AKA Fatal error: death.py activated
        # also [:4] and not [:] so that extra args get chopped. Not necessary but cool
        self.padding = ((4*forceList(padding))[:4])
        self.padding = ((4*forceList(padding))[:4])

    def position(self, pos): # to compact
        for i in pos:
            if i == "left":
                self.pos[0] = self.parent.pos[0] + self.parent.padding[3]
            if i == "right":
                self.pos[0] = self.parent.size[0] - self.parent.padding[1]
            if i == "top":
                self.pos[1] = self.parent.pos[1] - self.parent.padding[0]
            if i == "bot" or pos == "bottom":
                self.pos[1] = self.parent.size[1] - self.parent.padding[2]

    def getRect(self):
        return self.pos, self.size
