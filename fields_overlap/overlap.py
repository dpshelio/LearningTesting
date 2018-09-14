import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def show_fields(field1, field2):
    def vertices(left, bottom, right, top):
        verts = [(left, bottom), (left, top), (right, top), (right, bottom), (left, bottom)]
        return verts

    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY]
    path1 = Path(vertices(*field1), codes)
    path2 = Path(vertices(*field2), codes)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    patch1 = patches.PathPatch(path1, facecolor='orange', lw=2)
    patch2 = patches.PathPatch(path2, facecolor='blue', lw=2)
    ax.add_patch(patch1)
    ax.add_patch(patch2)
    ax.set_xlim(0,5)
    ax.set_ylim(0,5)
    fig.show()


def overlap_area(field1, field2):
    left1, bottom1, right1, top1 = field1
    left2, bottom2, right2, top2 = field2
    overlap_left = max(left1, left2)
    overlap_bottom = max(bottom1, bottom2)
    overlap_right = min(right1, right2)
    overlap_top = min(top1, top2)
    overlap_height = (overlap_top - overlap_bottom)
    overlap_width = (overlap_right - overlap_left)
    return overlap_height * overlap_width
