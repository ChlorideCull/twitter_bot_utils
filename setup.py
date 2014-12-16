from setuptools import setup

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


setup(
    name='twitter_bot_utils',

    version='0.5',

    description='Python utilities for twitter bots',

    long_description=read_md('readme.md'),

    url='http://github.com/fitnr/twitter_bot_utils',

    author='Neil Freeman',

    author_email='contact@fakeisthenewreal.org',

    license='GPL',

    packages=['twitter_bot_utils'],

    entry_points={
        'console_scripts': [
            'fave_mentions=twitter_bot_utils.tools:cli_fave_mentions',
            'auto_follow=twitter_bot_utils.tools:cli_auto_follow'
        ],
    },

    install_requires=[
        'tweepy>=2.3.0',
        'PyYAML>=3.11',
        'argparse>=1.2.1',
    ],

)
