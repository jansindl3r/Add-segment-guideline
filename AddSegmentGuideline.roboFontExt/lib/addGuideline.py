from math import atan2, degrees
from lib.fontObjects.fontPartsWrappers import RGuideline, RGlyph
from typing import Tuple, Union


def angleBetweenTwoPoints(pt1: RGlyph, pt2: RGlyph) -> float:
    x: int
    y: int
    x, y = tuple(i - j for i, j in zip(pt1.position, pt2.position))
    return degrees(atan2(y, x))


def middleBetweenTwoPoints(pt1: RGlyph, pt2: RGlyph) -> Tuple[int, int]:
    sums: Tuple[int, int] = tuple(map(sum, zip(pt1.position, pt2.position)))
    return tuple(map(lambda x:x//2, sums))



def addGuideline(glyph: RGlyph) -> None:
    for contour in glyph:
        for i, segment in enumerate(contour):
            if segment.selected:
                if segment.type == "line":
                    ptTo = segment.points[-1]
                    ptFrom = contour[i - 1].points[-1]
                    angle: float = angleBetweenTwoPoints(ptFrom, ptTo)
                    position: Tuple[int, int] = middleBetweenTwoPoints(ptFrom, ptTo)
                    glyph.appendGuideline(
                        position, angle, color=(0.999, 0.001, 0, 0.499)
                    )
    glyph.update()


if __name__ == "__main__":
    try:
        glyph: RGlyph = CurrentGlyph()
        with glyph.undo(f"Added segment guideline in {glyph.name}"):
            addGuideline(glyph)
    except:
        pass
