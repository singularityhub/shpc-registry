---
layout: container
name:  "quay.io/biocontainers/ncfp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncfp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncfp/container.yaml"
updated_at: "2025-01-04 03:22:05.328678"
latest: "0.2.0--py_0"
container_url: "https://biocontainers.pro/tools/ncfp"
aliases:
 - "ncfp"
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
 - "0.2.0--py_0"
description: "shpc-registry automated BioContainers addition for ncfp"
config: {"url": "https://biocontainers.pro/tools/ncfp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncfp", "latest": {"0.2.0--py_0": "sha256:ca86d4cce41a9555ac7a11c1eb663424e2784b34a02482842dbec24db895b886"}, "tags": {"0.2.0--py_0": "sha256:ca86d4cce41a9555ac7a11c1eb663424e2784b34a02482842dbec24db895b886"}, "docker": "quay.io/biocontainers/ncfp", "aliases": {"ncfp": "/usr/local/bin/ncfp", "easydev_buildPackage": "/usr/local/bin/easydev_buildPackage", "ibrowse": "/usr/local/bin/ibrowse", "multigit": "/usr/local/bin/multigit", "browse": "/usr/local/bin/browse", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "pybabel": "/usr/local/bin/pybabel", "rst2html4.py": "/usr/local/bin/rst2html4.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncfp.
shpc-registry automated BioContainers addition for ncfp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncfp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncfp:0.2.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncfp/0.2.0--py_0
$ module help quay.io/biocontainers/ncfp/0.2.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncfp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncfp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncfp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncfp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncfp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncfp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ncfp

```bash
$ singularity exec <container> /usr/local/bin/ncfp
$ podman run --it --rm --entrypoint /usr/local/bin/ncfp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncfp   -v ${PWD} -w ${PWD} <container> -c " $@"
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