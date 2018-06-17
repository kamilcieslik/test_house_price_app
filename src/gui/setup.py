import setuptools

converter = setuptools.Extension('converter', sources=['converter.c'])

if __name__ == '__main__':
    setuptools.setup(
        name='converter',
        version='1.0',
        ext_modules=[converter]
    )
