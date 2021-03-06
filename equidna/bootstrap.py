# -*- coding: utf-8 -*-
#
# Copyright (C) 2014  Geographica (Geografía Aplicada SL)
# Author: Alberto Asuero

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from equidna import Equidna

metadata = {
	"bounds" : "-180,-85,180,85",
	#"bounds": "-16.875,32.5468,8.4375,47.5172",
	"center" : "0,0,1",
	"minzoom" : 0,
	"maxzoom" : 10,
	"name" : "Test",
	"description" : "",
	"attribution" : "",
	"template" : "",
	"version" : "1.0.0",
	"format"  : "png"
}

eq = Equidna(mapnikxml = "mapnik.xml", metadata = metadata,ncores=None)

eq.build(output="test.mbtiles",format="mbtiles")