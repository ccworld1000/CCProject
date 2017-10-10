#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CCProject.py
# 
#  Created by CC on 2017/10/10.
#  Copyright 2017 youhua deng (deng you hua | CC) <ccworld1000@gmail.com>
#  https://github.com/ccworld1000/CCProject 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class CCProjectCell (object) :
	def __init__(self, dirname, shortDescription = "", longDescription = "") :
		self.dirname = dirname
		self.shortDescription = shortDescription
		self.longDescription = longDescription

class CCProject (object) :
	def __init__ (self, prefix = "CC") :
		self.prefix = prefix
		
	def genProject(self, dirs) :
		#print (dirs)

		for cell in dirs :
			c = CCProjectCell(self.prefix + str(cell))
			print (c.dirname)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    
    dirs = [
        'Cache',
        'ThemeColor',
        'Category',
        'Config',
        'Common',
        'CommonWeb',
        'Constants',
        'Entry',
        'AlertView',
        'Animation',
        'Networking',
        'Public',
        'Base',
        'Deprecated',
        'UI',
        'Error',
        'User',
        'Global',
        'Utility',
        'Localized',
        'Protocol',
        'Vendor',
        ]

    p = CCProject()
    p.genProject(dirs)
    
    sys.exit(main(sys.argv))
    
 
