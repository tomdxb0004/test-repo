setup(
    ...
    install_requires=[
        ...
        'click>=7.0'
    ],
	...
    entry_points='''
        [console_scripts]
        analysis=titanic.command_line:_analysis
    '''
)