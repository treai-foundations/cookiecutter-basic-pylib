from distutils.core import setup

setup(
    name="cookiecutter_basic_pylib",
    packages=[],
    use_scm_version={
        "write_to": "_version.py",
        "write_to_template": '__version__ = "{version}"\n',
    },
    description="Cookiecutter template for a base library python package",
    author="Roberto Ciatti",
    author_email="roberto.ciatti@tre-altamira.com",
    url="https://github.com/treai-foundations/cookiecutter-basic-pylib",
    license="MIT",
    keywords=[
        "cookiecutter",
        "template",
        "package",
    ],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
)
