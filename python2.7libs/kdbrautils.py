import hou, re



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



def menuFromPointNames(inp=0,grp_mode=True, attrib_name="name", re_mode=False):
    geo = hou.pwd().input(inp).geometry()
    names = geo.pointStringAttribValues(attrib_name)
    tmp = []

    for a in names:
        c = True
        if grp_mode:
            a = "@name="+a
        if re_mode:
            pattern = "[a-zA-Z_]*"
            s = re.search(pattern, a)
            a = s.group(0)
            c = not a in tmp 

        if c:
            tmp.append(str(a))
            tmp.append(str(a))
    tmp.sort()
    return tmp

def menuFromAgentClips(inp="."):
    geo = hou.node(inp).geometry()
    clips = geo.prim(0).intrinsicValue("agentclipcatalog")
    tmp = []

    for a in clips:
        c = True
        
        pattern = "[a-zA-Z_]*"
        s = re.search(pattern, a)
        a = s.group(0) + "*"
        c = not a in tmp 
        if c:
            tmp.append(a)
            tmp.append(a)
    tmp.sort()
    return tmp