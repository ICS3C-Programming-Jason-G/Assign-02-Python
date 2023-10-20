#!/usr/bin/env python3

# Created by: Jason Grace
# Created on: October 20th, 2023
# This program asks the user for the radius of
# a hemisphere in millimeters (mm). It then calculates and
# displays the volume and surface area of the hemisphere in centimeters.

import math


def main():
    # input
    radius = int(input("Enter the radius of the hemisphere (mm): "))

    # process
    volume_mm = 2 / 3 * math.pi * radius**3
    surface_area_mm = 3 * math.pi * radius**2

    volume_cm = volume_mm / 10
    surface_area_cm = surface_area_mm / 10

    # output
    print("")
    print("Volume = {:.1f} cm^3".format(volume_cm))
    print("Surface Area = {:.1f} cm^2".format(surface_area_cm))


if __name__ == "__main__":
    main()
