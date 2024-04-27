---
layout: container
name:  "quay.io/biocontainers/bioservices"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioservices/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioservices/container.yaml"
updated_at: "2024-04-27 02:34:42.776614"
latest: "1.7.11--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/bioservices"
aliases:
 - "easydev_buildPackage"
 - "ibrowse"
 - "multigit"
 - "browse"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "pybabel"
 - "rst2html4.py"
versions:
 - "1.7.9--pyh3252c3a_0"
 - "1.7.11--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for bioservices"
config: {"url": "https://biocontainers.pro/tools/bioservices", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioservices", "latest": {"1.7.11--pyh3252c3a_0": "sha256:cddb4493b53f6d39d854c353adb554f3ba563d2434e63d0728fe921445099ebc"}, "tags": {"1.7.9--pyh3252c3a_0": "sha256:cb4882e07676079e5ed211615d8e3d1ee58e8a52160129de58f67fc70c7d7c58", "1.7.11--pyh3252c3a_0": "sha256:cddb4493b53f6d39d854c353adb554f3ba563d2434e63d0728fe921445099ebc"}, "docker": "quay.io/biocontainers/bioservices", "aliases": {"easydev_buildPackage": "/usr/local/bin/easydev_buildPackage", "ibrowse": "/usr/local/bin/ibrowse", "multigit": "/usr/local/bin/multigit", "browse": "/usr/local/bin/browse", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "pybabel": "/usr/local/bin/pybabel", "rst2html4.py": "/usr/local/bin/rst2html4.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioservices.
shpc-registry automated BioContainers addition for bioservices
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioservices
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioservices:1.7.11--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioservices/1.7.11--pyh3252c3a_0
$ module help quay.io/biocontainers/bioservices/1.7.11--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioservices-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioservices-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioservices-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioservices-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioservices-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioservices-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### easydev_buildPackage

```bash
$ singularity exec <container> /usr/local/bin/easydev_buildPackage
$ podman run --it --rm --entrypoint /usr/local/bin/easydev_buildPackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easydev_buildPackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibrowse

```bash
$ singularity exec <container> /usr/local/bin/ibrowse
$ podman run --it --rm --entrypoint /usr/local/bin/ibrowse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibrowse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multigit

```bash
$ singularity exec <container> /usr/local/bin/multigit
$ podman run --it --rm --entrypoint /usr/local/bin/multigit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multigit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### browse

```bash
$ singularity exec <container> /usr/local/bin/browse
$ podman run --it --rm --entrypoint /usr/local/bin/browse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/browse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-build

```bash
$ singularity exec <container> /usr/local/bin/sphinx-build
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-quickstart

```bash
$ singularity exec <container> /usr/local/bin/sphinx-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4.py

```bash
$ singularity exec <container> /usr/local/bin/rst2html4.py
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)