"""
Start development web server!
"""

import sys
from app import APP

def main(argv):
    """Start development web server."""
    APP.run(host="127.0.0.1", port=5000, threaded=True)

if __name__ == "__main__":
    main(sys.argv)
