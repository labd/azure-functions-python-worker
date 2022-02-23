# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import os


__version__: str = "function_app"

# This module should be shadowed from customer_deps_path/common_module
# ./tests/unittests/resources/customer_func_path/common_module
package_location: str = os.path.dirname(__file__)
