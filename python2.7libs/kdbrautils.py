import hou



def menuItems(cls="point"):
    geo = hou.pwd().input(0).geometry()
    if cls == "point":
        attrs = geo.pointAttribs()
    elif cls == "prim":
        attrs = geo.primAttribs()
    elif cls == "vtx":
        attrs = geo.vertexAttribs()

    tmp = []
    for a in attrs:
        tmp.append(a.name())
        tmp.append(a.name())
    return tmp

def menuFromPointNames(inp=0,grp_mode=True):
    geo = hou.pwd().input(inp).geometry()
    names = geo.pointStringAttribValues("name")
    tmp = []

    for a in names:
        if grp_mode:
            a = "@name="+a
        tmp.append(str(a))
        tmp.append(str(a))
    return tmp
