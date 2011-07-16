'''
/*
 * Copyright 2011  Matthew Mole <code@gairne.co.uk>
 * 
 * This file is part of pyPortTrigger.
 * 
 * pyPortTrigger is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * ahgdc is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with pyPortTrigger.  If not, see <http://www.gnu.org/licenses/>.
*/
'''

import socket

print "Attempting to bind to local port 7777"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 7777))
print "Complete."
print "Attemping to make an outgoing connection."
s.connect(("www.google.com", 80))
s.send("GET google.co.uk")
s.close()
print "Port triggered: 7777"
