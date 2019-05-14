from distutils.core import setup

setup(
    name='pycblosc2',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    install_requires=['setuptools_scm', 'cffi'],
    py_modules=['pycblosc2'],
    )
