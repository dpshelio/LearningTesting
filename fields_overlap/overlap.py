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
    ax.set_xlim(0, max(*field1, *field2) + 1)
    ax.set_ylim(0, max(*field1, *field2) + 1)
    fig.show()


def overlap_area(field1, field2):
    '''
    Calculates the area of overlapping fields from the coordinates
    of their corners.

    parameters
    ----------
    field1: (tuple | list) of (int | float)
        Coordinates of the first field. Order should be: (left, bottom, right, top)

    field2: (tuple | list) of (int | float)
        Coordinates of the second field. Order should be: (left, bottom, right, top)

    Returns
    -------
    int or float
        Area in the coordinates entered unit.

    Example
    -------
    >>> from overlap import overlap_area
    >>> field_a = (1, 1, 4, 4) # position in kms as (x_0, y_0, x_1, y_1)
    >>> field_b = (2, 2, 3, 3) # smaller field inside field_a
    >>> overlap_area(field_a, field_b)
    1

    '''

    left1, bottom1, right1, top1 = field1
    left2, bottom2, right2, top2 = field2

    if (left1 > right1 or bottom1 > top1 or
        left2 > right2 or bottom2 > top2):
        raise ValueError(" Coordinates need to be entered (left, bottom, right, top)")

    overlap_left = max(left1, left2)
    overlap_bottom = max(bottom1, bottom2)
    overlap_right = min(right1, right2)
    overlap_top = min(top1, top2)
    overlap_height = max(0, overlap_top - overlap_bottom)
    overlap_width = max(0, overlap_right - overlap_left)
    return overlap_height * overlap_width
