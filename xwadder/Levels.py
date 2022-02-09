#!/usr/bin/env python3
"""
Levels - a module for working with Boom map lumps
Copyright 2022 Eric Duhamel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os
import sys

def main():
    filename = sys.argv[-1]
    if os.path.isfile(filename):
        res = 64
        width, height, origin = scale(res)
        file = open(filename, 'rb')
        for arg in sys.argv:
            if arg[0:13] == "--resolution=":
                res = int(arg[13:])
                width, height, origin = scale(res)
        bits, intmap = load_maps(filename, res)
        save_bitmap(bits, width, height, "vertexes")
        save_graymap(intmap, width, height, "vertexes")

def load_maps(filename, left, top, right, bottom):
    width, height = right - left + 1, bottom - top + 1
    bitstring = "1" * width * height
    intmap = [0 for x in range(width * height)]
    file = open(filename, 'rb')
    i = 1
    while not file.closed:
        bx = file.read(2)
        by = file.read(2)
        x = int.from_bytes(bx, byteorder='little', signed=True)
        y = int.from_bytes(by, byteorder='little', signed=True)
        if bx == b'' or by == b'':
            file.close()
        else:
            px, py = x - left, y - top
            pos = px + (width * py)
            bitstring = bitstring[0:pos] + "0" + bitstring[pos+1:]
            intmap[pos] = i % 256
        i = i + 1
    return bitstring, intmap

def read_things(bytemap):
    pairs = []
    left, top, right, bottom = 0, 0, 0, 0
    for i in range(0, len(bytemap), 2):
        x = int.from_bytes(bytemap[i: i + 2], byteorder='little', signed=True)
        y = int.from_bytes(bytemap[i + 2: i + 4], byteorder='little', signed=True)
        angle = bytemap[i + 4: i + 6]
        type = bytemap[i + 6: i + 8]
        flags = bytemap[i + 8: i + 10]
        pairs.append((x, y))
        if x < left: left = x
        if x > right: right = x
        if y < top: top = y
        if y > bottom: bottom = y
    return pairs

def read_vertices(bytemap):
    pairs = []
    left, top, right, bottom = 0, 0, 0, 0
    for i in range(0, len(bytemap), 4):
        bx = bytemap[i:i+2]
        by = bytemap[i+2:i+4]
        x = int.from_bytes(bx, byteorder='little', signed=True)
        y = int.from_bytes(by, byteorder='little', signed=True)
        pairs.append((x, y))
        if x < left: left = x
        if x > right: right = x
        if y < top: top = y
        if y > bottom: bottom = y
    return pairs, (left, top, right, bottom)

def scale(div):
    width, height = int(65536 / div), int(65536 / div)
    origin = int(65536 / div / 2)
    return width, height, origin

def save_bitmap(bitmap, width, height, name):
    with open(name + ".pbm", 'wb') as file:
        file.write(b"P4 ")
        file.write(bytes(str(width) + " ", 'utf_8'))
        file.write(bytes(str(height) + " ", 'utf_8'))
        bytemap = bytearray()
        for i in range(0, len(bitmap), 8):
            bytemap.append(int(bitmap[i:i+8], 2))
        file.write(bytemap)

def save_graymap(bitmap, width, height, name):
    with open(name + ".pgm", 'wb') as file:
        file.write(b"P5 ")
        file.write(bytes(str(width) + " ", 'utf_8'))
        file.write(bytes(str(height) + " ", 'utf_8'))
        file.write(b"255 ")
        for b in bitmap:
            file.write(b.to_bytes(1, 'little'))

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print("Keyboard Interrupt (Control-C)...")
    sys.exit()
