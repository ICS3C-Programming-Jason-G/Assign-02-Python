#!/usr/bin/env python3

# Created by: Jason Grace
# Created on: October 20th, 2023
# This program asks the user for the radius of
# a hemisphere in centimeters (cm). It then calculates and
# displays the volume and surface area of the hemisphere.

import math


def main():
    # input
    radius = int(input("Enter the radius of the hemisphere (cm): "))

    # process
    volume = 2 / 3 * math.pi * radius**3
    surface_area = 3 * math.pi * radius**2

    # output
    print("")
    print("Volume = {:.1f} cm^3".format(volume))
    print("Surface Area = {:.1f} cm^2".format(surface_area))


if __name__ == "__main__":
    main()
