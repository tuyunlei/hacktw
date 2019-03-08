import errno
import os, pty, subprocess as sp
from pty import (STDIN_FILENO, STDOUT_FILENO, STDERR_FILENO, CHILD)

parent_fd, child_fd = pty.openpty()

if os.fork() == CHILD:
    # Child process
    os.close(parent_fd)

    child_name = os.ttyname(parent_fd)
    try:
        fd = os.open('/dev/tty', os.O_RDWR | os.O_NOCTTY)
        os.close(fd)
    except OSError as err:
        if err.errno != errno.ENXIO:
            raise
    os.setsid()
    try:
        fd = os.open('/dev/tty', os.O_RDWR | os.O_NOCTTY)
        os.close(fd)
        raise PtyProcessError("OSError of errno.ENXIO should be raised.")
    except OSError as err:
        if err.errno != errno.ENXIO:
            raise

    os.dup2(child_fd, STDIN_FILENO)
    os.dup2(child_fd, STDOUT_FILENO)
    os.dup2(child_fd, STDERR_FILENO)
else:
    # Main process
    pass
