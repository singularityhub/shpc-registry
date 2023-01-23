---
layout: container
name:  "quay.io/biocontainers/dreamtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dreamtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dreamtools/container.yaml"
updated_at: "2023-01-23 03:41:07.520259"
latest: "1.3.0--py36_0"
container_url: "https://biocontainers.pro/tools/dreamtools"
aliases:
 - "dreamtools"
 - "dreamtools-layout"
 - "dreamtools-scoring"
 - "synapse"
 - "easydev_buildPackage"
 - "ibrowse"
 - "multigit"
 - "browse"
 - "runxlrd.py"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "pybabel"
versions:
 - "1.3.0--py36_0"
description: "shpc-registry automated BioContainers addition for dreamtools"
config: {"url": "https://biocontainers.pro/tools/dreamtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dreamtools", "latest": {"1.3.0--py36_0": "sha256:ec181ed37ad7cc688c6695c228ce3443635d30d17877d2bee4183819224fbeba"}, "tags": {"1.3.0--py36_0": "sha256:ec181ed37ad7cc688c6695c228ce3443635d30d17877d2bee4183819224fbeba"}, "docker": "quay.io/biocontainers/dreamtools", "aliases": {"dreamtools": "/usr/local/bin/dreamtools", "dreamtools-layout": "/usr/local/bin/dreamtools-layout", "dreamtools-scoring": "/usr/local/bin/dreamtools-scoring", "synapse": "/usr/local/bin/synapse", "easydev_buildPackage": "/usr/local/bin/easydev_buildPackage", "ibrowse": "/usr/local/bin/ibrowse", "multigit": "/usr/local/bin/multigit", "browse": "/usr/local/bin/browse", "runxlrd.py": "/usr/local/bin/runxlrd.py", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "pybabel": "/usr/local/bin/pybabel"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dreamtools.
shpc-registry automated BioContainers addition for dreamtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dreamtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dreamtools:1.3.0--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dreamtools/1.3.0--py36_0
$ module help quay.io/biocontainers/dreamtools/1.3.0--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dreamtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dreamtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dreamtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dreamtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dreamtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dreamtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dreamtools

```bash
$ singularity exec <container> /usr/local/bin/dreamtools
$ podman run --it --rm --entrypoint /usr/local/bin/dreamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreamtools-layout

```bash
$ singularity exec <container> /usr/local/bin/dreamtools-layout
$ podman run --it --rm --entrypoint /usr/local/bin/dreamtools-layout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreamtools-layout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dreamtools-scoring

```bash
$ singularity exec <container> /usr/local/bin/dreamtools-scoring
$ podman run --it --rm --entrypoint /usr/local/bin/dreamtools-scoring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dreamtools-scoring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### synapse

```bash
$ singularity exec <container> /usr/local/bin/synapse
$ podman run --it --rm --entrypoint /usr/local/bin/synapse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/synapse   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### runxlrd.py

```bash
$ singularity exec <container> /usr/local/bin/runxlrd.py
$ podman run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runxlrd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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