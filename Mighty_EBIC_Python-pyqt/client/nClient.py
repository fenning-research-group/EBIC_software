#! /usr/bin/env python

#Mighty Ebic - Network Client

#Based loosely on the OSI Model
# Physical Layer - IEEE 802.3
# Data Link Layer - IEEE 802.3
# Network Layer - IPv4
# Transport Layer - TCP
# Application Layer - ? 

# ALGORITHM:
# SET NETWORK IDENTIFIERS
# CREATE TCP/IP SOCKET
# BIND SOCKETS (TEST)
# LISTEN (TEST, FOREVER LOOP)
# PRINT TO STDOUT

# TODO 
#  Connect to SQLITE DB to store data

import sys,os,socket;

class nModel():

	def __init__(self):
		self.EBIC_DEVICE_IP = '127.0.0.1';
		self.EBIC_DEVICE_PORT = 1025;

	def main(self):
		try:
			tSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
			print "Socket created."
		except socket.error, msg:
			print "Could not CREATE socket, ",msg;

		try:
			tSocket.bind((self.EBIC_DEVICE_IP,self.EBIC_DEVICE_PORT));
			print "Socket bound to",self.EBIC_DEVICE_IP,":",self.EBIC_DEVICE_PORT;
		except socket.error, msg:
			print "Could not BIND socket, ",msg;

		tSocket.listen(1);		# Argument specifies number of concurrent connections

n = nModel();
n.main();



