from setuptools import setup

setup(name='autograder',
        version='0.1',
        description='Autograder for programming projects',
        url='http://github.com/rhomeister/autograder',
        author='Ruben Stranders',
        author_email='r.stranders@gmail.com',
        license='MIT',
        packages=['autograder'],
        install_requires=[
            'gitpython',
            'gitinspector',
            'numpy'
            ],
        entry_points = {
            'console_scripts': [
                'autograde=autograder.cli:main'
                ],
            },
        zip_safe=False
        )
