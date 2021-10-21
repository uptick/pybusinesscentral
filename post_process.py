import re
import glob
from typing import Optional

package_name = 'pybusinesscentral'
model_import = re.compile(rf'^from {package_name}.model.(?P<module>\w+) import (?P<model>\w+)\n$')
bad_import = f'from {package_name}.model.unknownbasetype import UNKNOWNBASETYPE\n'


for filename in glob.glob(f'./{package_name}/api/*_api.py'):
    print(filename)
    model_name: Optional[str] = None
    variable_name: Optional[str] = None
    converted: list[str] = []
    with open(filename) as file:
        for line in file.readlines():
            if line == bad_import:
                # Just skip these lines as we don't need them anymore
                continue

            out = line
            if model_name:
                out = line.replace(
                    'unknown_base_type',
                    variable_name,
                ).replace(
                    'UNKNOWN_BASE_TYPE',
                    model_name,
                )
            elif match:= model_import.search(line):
                module, model = match.groups()
                if not model.startswith('InlineResponse'):
                    model_name = model
                    variable_name = re.sub(r'(?<!^)(?=[A-Z])', '_', model).lower()

            converted.append(out)

    with open(filename, 'w') as file:
        file.writelines(converted)
