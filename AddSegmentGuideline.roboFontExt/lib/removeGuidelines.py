from typing import Tuple
from lib.fontObjects.fontPartsWrappers import RGlyph


def removeGuidelines(glyph: RGlyph):
    colorToRemove: Tuple[float, ...] = (0.999, 0.001, 0.0, 0.499)
    for guideline in glyph.guidelines:
        if guideline.color == colorToRemove:
            glyph.removeGuideline(guideline)


if __name__ == "__main__":
    try:
        glyph: RGlyph = CurrentGlyph()
        with glyph.undo(f"removed segment guideliens in {glyph.name}"):
            removeGuidelines(glyph)
    except:
        pass
