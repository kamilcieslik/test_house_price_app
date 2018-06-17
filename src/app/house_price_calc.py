import sys
sys.path.extend(['../..',
                 'z../../app'])

from src.gui.main_gui_controller import MainGuiController


if __name__ == "__main__":
    if sys.platform.startswith('linux'):
        from OpenGL import GL
    main = MainGuiController("AIzaSyBEmx5P3vl4ox4OU6nPgwTbU9k-_0Zm6Lo")
