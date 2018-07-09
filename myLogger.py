# import logging
import os
import sys
import imp


def main_is_frozen():
    return (hasattr(sys, "frozen") or  # new py2exe
            hasattr(sys, "importers")  # old py2exe
            or imp.is_frozen("__main__"))  # tools/freeze


def get_main_dir():
    if main_is_frozen():
        return os.path.dirname(os.path.dirname(sys.executable))
    return os.path.abspath(os.path.dirname(sys.argv[0]))


# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                     datefmt='%m-%d %H:%M',
#                     handlers=[logging.FileHandler(os.path.join(get_main_dir(), 'logger.log'), 'w', 'utf-8')])
# logger = logging.getLogger('MainLogs')
# # logger.setLevel(logging.INFO)
# # fh = logging.FileHandler('logger.log', encoding='utf-8')
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)
# logger.addHandler(ch)
