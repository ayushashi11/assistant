import curses, sys
from curses import wrapper
from _curses import window
sys.path.append(".")
from ai_m2 import reply

def main(stdscr: window):# curses._CursesWindow):
    s=''
    stdscr.clear()
    stdscr.refresh()
    while "bye" not in s.lower() and "see ya" not in s.lower():
        stdscr.addstr(20,0, ">>> ")
        curses.echo()
        s=reply(stdscr.getstr(20, 4).decode(), stdscr)
        stdscr.clear()
        stdscr.addstr(0,0,s)
        stdscr.refresh()
    stdscr.getkey()

wrapper(main)

