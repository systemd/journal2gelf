from distutils.core import setup

setup(
    name='journal2gelf',
    version='0.0.1',
    author='Joe Miller',
    author_email='joeym@joeym.net',
    scripts=['journal2gelf'],
    url='https://github.com/systemd/journal2gelf',
    license='LICENSE',
    description="Send logs from systemd's journald to a GELF server like Graylog2",
    long_description=open('README.md').read(),
    install_requires=["graypy"],
)
