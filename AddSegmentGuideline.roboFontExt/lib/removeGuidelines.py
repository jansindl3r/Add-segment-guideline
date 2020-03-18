from typing import Tuple
from lib.fontObjects.fontPartsWrappers import RGlyph

colorToRemove: Tuple[float, ...] = (.999, .001, 0.0, .499)
glyph: RGlyph = CurrentGlyph()
for guideline in glyph.guidelines:
    if guideline.color == colorToRemove:
        glyph.removeGuideline(guideline)