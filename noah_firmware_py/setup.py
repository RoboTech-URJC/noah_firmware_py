#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

package_name = 'noah_firmware_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Jonatan Gines',
    author_email='jginesclavero@gmail.com',
    maintainer='Jonatan Gines',
    maintainer_email='jginesclavero@gmail.com',
    keywords=['ROS2', 'noah_firmware_py'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'The noah_firmware_py package'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'noah_firmware_py = noah_firmware_py.noah_firmware_node:main'
        ],
    },
)
