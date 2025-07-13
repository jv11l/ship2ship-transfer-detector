import ee
import math


def to_backscatter(image):
    """Convert dB from S1_GRD collection to backscatter units.

    Also multiply result by 1e5.
    Angle is between the pixel (line-of-sight) and the satellite's nadir.
    """
    angle_corrected = image.select(
        'VH'  # "V.|H."
    ).subtract(  # this should just be 'VH'
        image.select("angle")
        .multiply(math.pi / 180.0)
        .cos()
        .pow(2)
        .log10()
        .multiply(10.0)
    )
    backscatter = (
        ee.Image(10.0)
        .pow(angle_corrected.divide(10.0))
        .multiply(10000)
        # .select("VH")
    )
    return backscatter


def to_natural(img):
    return ee.Image(10.0).pow(img.select(0).divide(10.0))