#  Copyright (c) LinkedIn Corporation.
#  All rights reserved.
#
#  This source code is licensed under the license found in the
#  LICENSE file in the root directory of this source tree.

import sys
def generate_permanent_internal_memory_usage_html():
    html = "<h2>Permanent Internal Memory Usage</h2>"
    html += f"<table><tr><th>Memory Usage of Base Branch</th><th>Memory Usage of Head Branch</th><th>Difference in Permanent Internal Memory Usage</th></tr>"

    html += f"<tr><td>{base_memory_usage} MB</td><td>{head_memory_usage} MB</td><td>{int(head_memory_usage) - int(base_memory_usage)} MB</td></tr>"

    html += "</table>"

    print(html)

base_memory_usage = sys.argv[1]
head_memory_usage = sys.argv[2]

generate_permanent_internal_memory_usage_html()
