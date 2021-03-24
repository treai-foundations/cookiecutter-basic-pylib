#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{ cookiecutter.github_action_pr_triggered }}" != "y":
        remove_file(".github/workflows/triggered_by_pr.yml")

    if "{{ cookiecutter.github_action_tag_triggered }}" != "y":
        remove_file(".github/workflows/triggered_by_tag.yml")
