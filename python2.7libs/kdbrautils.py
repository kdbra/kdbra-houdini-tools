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