from setuptools import setup, find_packages


setup(
    name = 'ATM-VIRTUAL',
    version = '1.0',
    description = 'Cajero Automatico',
    long_description = read('README.md'),
    long_description_content_type = "text/markdown",
    author = 'danielangelarro',
    author_email = 'danielangelarro@gmail.com',
    url = 'https://github.com/Kehrveiz/ChefBot',
    scripts = ['run.py'],
    packages = find_packages(),
    keywords = 'atm python',
    install_requires = [],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'License :: MIT-LICENSE',
    ]
)