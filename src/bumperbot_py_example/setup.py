from setuptools import find_packages, setup

package_name = 'bumperbot_py_example'

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
    maintainer='naivoder',
    maintainer_email='cameron.redovian@r-dex.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = bumperbot_py_example.simple_publisher:main',
            'simple_subscriber = bumperbot_py_example.simple_subscriber:main'
        ],
    },
)
