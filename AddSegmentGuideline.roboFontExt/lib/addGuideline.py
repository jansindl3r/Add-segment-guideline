from math import atan2, degrees
from lib.fontObjects.fontPartsWrappers import RGuideline, RGlyph
from typing import Tuple


def angleBetweenTwoPoints(pt1: RGlyph, pt2: RGlyph) -> float:
    x: int
    y: int
    x, y = tuple(i - j for i, j in zip(pt1.position, pt2.position))
    return degrees(atan2(y, x))


def middleBetweenTwoPoints(pt1: RGlyph, pt2: RGlyph) -> Tuple[int, int]:
    sums: tuple = tuple(map(sum, zip(pt1.position, pt2.position)))
    x, y = tuple(i // 2 for i in sums)
    return (x, y)


def addGuideline(glyph: RGlyph) -> None:
    for contour in glyph:
        for i, segment in enumerate(contour):
            if segment.selected:
                if segment.type == "line":
                    ptTo = segment.points[0]
                    ptFrom = contour[i - 1].points[0]
                    angle: float = angleBetweenTwoPoints(ptFrom, ptTo)
                    position: Tuple[int, int] = middleBetweenTwoPoints(ptFrom, ptTo)
                    glyph.appendGuideline(position, angle, color=(.999, .001, 0, .499))
    glyph.update()


if __name__ == "__main__":
    try:
        glyph: RGlyph = CurrentGlyph()
        with glyph.undo(f"Added segment guideline in {glyph.name}"):
            addGuideline(glyph)
    except:
        pass