---
layout: container
name:  "quay.io/biocontainers/dlcpar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dlcpar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dlcpar/container.yaml"
updated_at: "2025-08-25 03:43:35.986668"
latest: "1.0--py_2"
container_url: "https://biocontainers.pro/tools/dlcpar"
aliases:
 - "dlcoal_to_dlcpar"
 - "dlcpar"
 - "dlcpar_search"
 - "dlcpar_to_dlcoal"
 - "tree-events-dlc"
 - "tree-events-dlcpar"
 - "f2py2"
 - "f2py2.7"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "1.0--py_2"
description: "shpc-registry automated BioContainers addition for dlcpar"
config: {"url": "https://biocontainers.pro/tools/dlcpar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dlcpar", "latest": {"1.0--py_2": "sha256:622eada8e2961e7aca1801b908b93f31c7f78314bdb4394df5d620f5301fcc2b"}, "tags": {"1.0--py_2": "sha256:622eada8e2961e7aca1801b908b93f31c7f78314bdb4394df5d620f5301fcc2b"}, "docker": "quay.io/biocontainers/dlcpar", "aliases": {"dlcoal_to_dlcpar": "/usr/local/bin/dlcoal_to_dlcpar", "dlcpar": "/usr/local/bin/dlcpar", "dlcpar_search": "/usr/local/bin/dlcpar_search", "dlcpar_to_dlcoal": "/usr/local/bin/dlcpar_to_dlcoal", "tree-events-dlc": "/usr/local/bin/tree-events-dlc", "tree-events-dlcpar": "/usr/local/bin/tree-events-dlcpar", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dlcpar.
shpc-registry automated BioContainers addition for dlcpar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dlcpar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dlcpar:1.0--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dlcpar/1.0--py_2
$ module help quay.io/biocontainers/dlcpar/1.0--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dlcpar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dlcpar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dlcpar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dlcpar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dlcpar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dlcpar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dlcoal_to_dlcpar

```bash
$ singularity exec <container> /usr/local/bin/dlcoal_to_dlcpar
$ podman run --it --rm --entrypoint /usr/local/bin/dlcoal_to_dlcpar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dlcoal_to_dlcpar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dlcpar

```bash
$ singularity exec <container> /usr/local/bin/dlcpar
$ podman run --it --rm --entrypoint /usr/local/bin/dlcpar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dlcpar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dlcpar_search

```bash
$ singularity exec <container> /usr/local/bin/dlcpar_search
$ podman run --it --rm --entrypoint /usr/local/bin/dlcpar_search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dlcpar_search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dlcpar_to_dlcoal

```bash
$ singularity exec <container> /usr/local/bin/dlcpar_to_dlcoal
$ podman run --it --rm --entrypoint /usr/local/bin/dlcpar_to_dlcoal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dlcpar_to_dlcoal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tree-events-dlc

```bash
$ singularity exec <container> /usr/local/bin/tree-events-dlc
$ podman run --it --rm --entrypoint /usr/local/bin/tree-events-dlc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tree-events-dlc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tree-events-dlcpar

```bash
$ singularity exec <container> /usr/local/bin/tree-events-dlcpar
$ podman run --it --rm --entrypoint /usr/local/bin/tree-events-dlcpar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tree-events-dlcpar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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