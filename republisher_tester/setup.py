from setuptools import find_packages, setup

package_name = 'republisher_tester'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hluo',
    maintainer_email='hluo@clearpathrobotics.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'delay_tester = republisher_tester.delay_tester:main',
            'cmd_vel_repub = republisher_tester.cmd_vel_repub:main'
        ],
    },
)
