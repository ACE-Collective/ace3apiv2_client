"""pytest configuration for aceapi-v2-client tests

This conftest adds the project root to sys.path so that the aceapi_v2_client
module can be imported without requiring the package to be installed first.
"""

import sys
from pathlib import Path

# Add the project root (parent of tests directory) to sys.path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
