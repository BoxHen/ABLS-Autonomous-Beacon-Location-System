#!/usr/bin/env python

import serial
import time

ser = serial.Serial('', 19200, timeout = 1)

def forward(speed):
	ser.write(chr(0XCA))
	ser.write(chr(speed))
	ser.write(chr(0xC1))
	ser.write(chr(speed))

def reverse(speed):


def leftTurn(speed):


def rightTurn(speed):

