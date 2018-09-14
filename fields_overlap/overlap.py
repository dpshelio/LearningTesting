import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def sf(f1, f2):
    def vertices(L,B,R,T):
        verts = [(L,B),(L,T),(R,T),(R,B),(L,B)]
        return verts
    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    p1 = Path(vertices(*f1), codes)
    p2 = Path(vertices(*f2), codes)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    pa1 = patches.PathPatch(p1, facecolor='orange', lw=2)
    pa2 = patches.PathPatch(p2, facecolor='blue', lw=2)
    ax.add_patch(pa1)
    ax.add_patch(pa2)
    ax.set_xlim(0,5)
    ax.set_ylim(0,5)
    fig.show()


def oa(f1, f2):
    L1, B1, T1, R1 = f1
    L2, B2, T2, R2 = f2
    overL = max(L1, L2)
    overB = max(B1, B2)
    overR = min(R1, R2)
    overT = min(T1, T2)
    overH = (overT-overB)
    overW = (overR-overL)
    return overH*overW
