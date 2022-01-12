# Assumes openapi-generator is installed
import sys
import subprocess
import re
import glob
from typing import Optional

package_name = 'pybusinesscentral'
model_import = re.compile(rf'^from {package_name}.model.(?P<module>\w+) import (?P<model>\w+)\n$')
bad_import = f'from {package_name}.model.unknownbasetype import UNKNOWNBASETYPE\n'

def generate():
    subprocess.run(
        [
            'openapi-generator',
            'generate',
            '-i',
            './bcoas2.0.yaml',
            '-o',
            '.',
            '--package-name',
            package_name,
            '-g',
            'python',
            '--http-user-agent',
            'PostmanRuntime/7.28.4',
        ],
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    )

def fix_apis():
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

def fix_optional_dicts():
    for filename in glob.glob(f'./{package_name}/model/*.py'):
        print(filename)
        with open(filename) as file:
            converted: list[str] = [
                line.replace(': (dict,),', ': (dict, none_type,),')
                for line in file.readlines()
            ]

        with open(filename, 'w') as file:
            file.writelines(converted)

def fix_setup():
    with open('./setup.py') as file:
        converted: list[str] = [
            line
            .replace(
                'VERSION = "1.0.0"', 'VERSION = "2.0.0"',
            )            
            .replace(
                'author="OpenAPI Generator community",', 'author="Uptick",'
            )
            .replace(
                'author_email="team@openapitools.org",', 'author_email="support@uptickhq.com",',
            )
            for line in file.readlines()
        ]        

    with open('./setup.py', 'w') as file:
        file.writelines(converted)


def main():
    generate()
    fix_apis()
    fix_optional_dicts()
    fix_setup()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""build.py <package-version>
This script assumes Assumes openapi-generator is installed

Args:
    package-version: The version python package to be generated (eg '1.0.3')
""")
        sys.exit(-1)
    print(sys.argv)
    main()