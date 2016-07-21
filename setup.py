from setuptools import setup, find_packages
import os

with open(os.path.join('version.txt')) as version_file:
    version_from_file = version_file.read().strip()

with open('requirements.txt') as f_required:
    required = f_required.read().splitlines()

with open('test_requirements.txt') as f_tests:
    required_for_tests = f_tests.read().splitlines()

setup(
    name='cloudshell-networking-Huawei',
    url='https://github.com/QualiSystems/cloudshell-networking-Huawei',
    author='QualiSystems',
    author_email='info@qualisystems.com',
    packages=find_packages(),
    install_requires=required,
	tests_require=required_for_tests,
    test_suite='tests',
    version=version_from_file,
    description='QualiSystems Python package',
    include_package_data = True
)
