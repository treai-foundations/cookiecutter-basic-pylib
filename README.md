# Basic python library cookiecutter template

This is very basic cookiecutter template suitable to start
a new python library project with packaging and tests features.

## Requirements

* Python3

## Install cookiecutter

```sh
pip install --user cookiecutter
```

## Upgrading cookiecutter

```sh
pip install --upgrade cookiecutter
```

---

## Generate new project using this cookiecutter

To create a new project using this cookiecutter template use the following

```sh
cookiecutter gh:treai-foundations/cookiecutter-basic-pylib
```

The line above will fetch automatically the template from github using your
local `~/.cookiecutters/` folder.

In case already present, you'll be prompted to re-download the template, this
can be useful to update it with recent modifications.

```sh
> cookiecutter gh:treai-foundations/cookiecutter-basic-pylib
You've downloaded /home/rciatti/.cookiecutters/cookiecutter-basic-pylib before.
Is it okay to delete and re-download it? [yes]: 
```

After the template download, cookiecutter will prompt you wit a serie of qeustions
defined in the template configuration:

```sh
author_name [Author Name]: 
author_email [author@email.com]: 
github_username [github_username]: 
project_name [name-of-the-project]: 
project_name_snake [name_of_the_project]: 
project_name_kebab [name-of-the-project]: 
project_short_description [Short description of the project]: 
github_action_pr_triggered [y]: 
github_action_tag_triggered [y]: 
use_flake8 [y]: 
use_coverage [y]: 
Select license:
1 - Proprietary
2 - MIT license
3 - BSD license
4 - ISC license
5 - Apache Software License 2.0
6 - GNU General Public License v3
Choose from 1, 2, 3, 4, 5, 6 [1]:
```

Each question has a default value.

### About some options

After the `project_name` you'll be prompted with:

* `project_name_snake`: is the `project_name` value converted in snake case
* `project_name_kebab`: is the `project_name` value converted in kebab case

You can leave the default value compliant with python standard names for
package and project name.

**Warning:**
*When `cookiecutter 2.0` will be available the two options above will be
changed to `rendered private variable`.*

* `github_action_pr_triggered`: add the github action workflow to react to PRs
* `github_action_tag_triggered`: add the github action workflow to react to tags
* `use_flake8`: enable flake8 linter (adding also the package to the *requirements_dev.txt*)
* `use_coverage`: enable coverage and web report

## Makefile

The template, after prompting for all the options, will generate a `Makefile`
that can be used to help you with several tasks that can be exploited like below:

```sh
> make help

clean                remove all build, test, coverage and Python artifacts
clean-build          remove build artifacts
clean-pyc            remove Python file artifacts
clean-test           remove test and coverage artifacts
test                 run tests quickly with the default Python
coverage             check code coverage quickly with the default Python
coverage-web         check code coverage and open report in web browser
dist                 builds source and wheel package
```

## Git init

The template automation, as post-hook action, will do a

```sh
git init .
```

inside the newly generated project. This is mandatory because the
`setuptools_scm` is used to fetch tag versions from the Version Control System.

## Your duties

After the project creation, having a `virtualenv` and installing development
dependencies contained in `requirements_dev.txt` depends on you and your way
to work.
