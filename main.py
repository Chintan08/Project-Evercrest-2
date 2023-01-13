import ctypes
import curses
from curses import *
from Engine.print_queue import print_queue
from Windows.opening_window import opening_window
from Engine.constants import constants
from os import system

system("Project: Evercrest 2")
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, 3)

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 16
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, ctypes.c_long(False), ctypes.pointer(font))

def main(stdscr):

    curses.curs_set(False)

    constants.TERMINAL_Y = stdscr.getmaxyx()[0]
    constants.TERMINAL_X = stdscr.getmaxyx()[1]
    constants.CENTER_Y = int(constants.TERMINAL_Y / 2)
    constants.CENTER_X = int(constants.TERMINAL_X / 2)

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    constants.YELLOW = curses.color_pair(1)
    constants.RED = curses.color_pair(2)
    constants.WHITE = curses.color_pair(3)

    print_queue.add_event(opening_window)
    print_queue.start(stdscr)


wrapper(main)
