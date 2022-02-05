# INSPIRO
Python + Gnuplot script to draw cycloids where one circle moves on the perimeter of another one.

It's inspired by (Spirograph)[https://en.wikipedia.org/wiki/Spirograph] and it's clone from the former Czechoslovakia called (INSPIRO)[https://www.zatrolene-hry.cz/spolecenska-hra/inspiro-7995/obrazky/]

![Example output](images/9.png)

# Install
It requires Python2 plus libraries numpy and [PyGnuplot](https://pypi.org/project/PyGnuplot/#description).
Drawing is done with [Gnuplot](http://www.gnuplot.info/).

# Configure
 - Radius of the big circle
```
big_radius = 96.0
```
 - Radius of the small circle plus parameters for the drawing
   - Tuple with 
     - radius of the small circle
     - distance of the drawing point from the center of the small circle
     - number of different starting angles
     - string with binary encoding (0==OFF, 1==ON) to choose the variants to draw
       - 1000 => inner circle, real variant (X = ... + cos, Y = .. - sin)
       - 0100 => inner circle, new  variant (X = ... + cos, Y = .. + sin) 
       - 0010 => outer circle, real variant (X = ... + cos, Y = .. + sin)
       - 0001 => outer circle, new  variant (X = ... + cos, Y = .. - sin)
```
small_radius_draw_point = [ (40.0, 20.0, 1,  '0100'),
                            (40.0, 20.0, 10, '1010'),
                            (40.0, 20.0, 5,  '0110'),
                            (40.0, 20.0, 1,  '0110'),
                            (56.0, 28.0, 10, '1010'), 
                            (56.0, 28.0, 10, '0101'), 
                            (80.0, 20.0, 10, '1001'), 
                            (72.0, 36.0, 7,  '1001'), 
                            (24.0, 20.0, 12, '1111'),
                            (24.0, 20.0, 12, '1010'),
                            (24.0, 20.0, 12, '0101'),
                            (32.0, 28.0, 6,  '1010'),
                            (32.0, 28.0, 6,  '0101'),
                            (64.0, 8.0, 10,  '1001'),
                            (48.0, 4.0, 8,   '1001'),
]
```

# Run it 
`./inspiro.py`

and check the images in `Images` directory. Delete intermediary files in the `Temp` directory.

`rm -rf Temp/*dat`

Enjoy!

