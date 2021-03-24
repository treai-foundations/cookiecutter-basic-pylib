from setuptools import setup, find_packages

MINIMAL_REQUIREMENTS = []

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="{{ cookiecutter.project_name_kebab }}",
    use_scm_version={
        "write_to": "{{ cookiecutter.project_name_snake }}/_version.py",
        "write_to_template": '__version__ = "{version}"\n',
    },
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme,
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    license="{{ cookiecutter.license }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_kebab }}",
    packages=find_packages(exclude=["tests", "tests.*"]),
    data_files=[("", ["LICENSE"])],
    install_requires=MINIMAL_REQUIREMENTS,
    zip_safe=False,
    keywords=[
        "{{ cookiecutter.project_name_snake }}",
    ],
)
