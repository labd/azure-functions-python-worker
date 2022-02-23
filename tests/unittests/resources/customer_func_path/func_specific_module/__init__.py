# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import os


__version__: str = "function_app"

# ./tests/unittests/resources/customer_func_path/func_specific_module
package_location: str = os.path.dirname(__file__)
