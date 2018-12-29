#!/usr/bin/env python

# Create images motivated by INSPIRO (http://starehracky.cz/katalog_detail.php?kategorie=OSTATNI&hracka=570)
# Small circle rolls inside or outside of the big circle. 
# The drawing point (pencil) is at distance of p from the center of the small circle

# Copyright 2018 Jirka Hladky (hladky DOT jiri AT gmail DOT com)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import PyGnuplot as gp
# https://pypi.org/project/PyGnuplot/#description
import numpy as np
from fractions import gcd

def graph_setup():
    gp.c('set terminal qt')
    gp.c('set size ratio -1')    
    #gp.c('set grid')
    gp.c('set key off')
    #gp.c('set xrange[-100:-80]')    
    #gp.c('set yrange[-100:-80]')   
    gp.c('unset border')
    gp.c('unset xtics')
    gp.c('unset ytics')
    

# Radius of the big circle
big_radius = 96.0
# Tuple with 
# - radius of the small circle
# - distance of the drawing point from the center of the small circle
# - number of different starting angles
# - string with binary encoding (0==OFF, 1==ON) to choose the variants to draw
#       - 1000 => inner circle, real variant (X = ... + cos, Y = .. - sin)
#       - 0100 => inner circle, new  variant (X = ... + cos, Y = .. + sin) 
#       - 0010 => outer circle, real variant (X = ... + cos, Y = .. + sin)
#       - 0001 => outer circle, new  variant (X = ... + cos, Y = .. - sin)
# This can be easily enhanced so that the string is using base 36 encoding which allows
#    turn off the variant (0)
#    number of different starting angles from 1 (1) to 35 (letter Z)
#    code: int("A", 36)
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

for idx, (r,p,num_angles,types) in enumerate(small_radius_draw_point):
        graph_setup()
        first = True
        command='plot'
        full_revolutions = r / gcd (big_radius,r)
        for (idx_angle,starting_angle) in enumerate(np.linspace (0,360, num=num_angles, endpoint=False)):
            starting_angle_rad = starting_angle / (2.0 * np.pi) * full_revolutions
            T = np.linspace(0.0, 2*np.pi*full_revolutions, num=400*full_revolutions, endpoint=True)
            for (variant,(radius,sign_x,sign_y)) in enumerate([(big_radius - r, 1, -1), (big_radius - r, 1, 1), (big_radius + r,1,1), (big_radius + r,1,-1)]):
                if types[variant]=='1':
                    X = radius * np.cos(T+starting_angle_rad) + sign_x * p *  np.cos(big_radius/r * T)
                    Y = radius * np.sin(T+starting_angle_rad) + sign_y * p *  np.sin(big_radius/r * T)
                    name = 'Temp/INSPIRO_' + str(idx) + '_' + str(starting_angle) + '_' + str(variant)
                    print name + '.dat'
                    gp.s([X,Y],name + '.dat')
                    gp.c(command + ' "' + name + '.dat" u 1:2 w lines ls ' + str(1))
                    if first:
                        first=False
                        command='replot'
        #raw_input("Press Enter to continue...")
        # This is needed as PNG terminal type does not support replot
        # As the WA, we need to plot the whole graph first and then switch to PNG            
        gp.c('set term pngcairo size 800,800 enhanced')
        gp.c('set output "Images/' + str(idx) + '.png"')
        gp.c('replot')
        gp.figure()
    
