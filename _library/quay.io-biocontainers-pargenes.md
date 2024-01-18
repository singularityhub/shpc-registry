---
layout: container
name:  "quay.io/biocontainers/pargenes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pargenes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pargenes/container.yaml"
updated_at: "2024-01-18 02:35:15.742474"
latest: "1.2.0--py27h8374a30_0"
container_url: "https://biocontainers.pro/tools/pargenes"
aliases:
 - "pargenes-hpc-debug.py"
 - "pargenes-hpc.py"
 - "pargenes.py"
 - "aggregate_profile.pl"
 - "profile2mat.pl"
 - "mpiCC"
 - "ompi-clean"
 - "ompi-server"
 - "ompi_info"
 - "opal_wrapper"
 - "orte-clean"
 - "orte-info"
 - "orte-server"
versions:
 - "1.2.0--py27h8374a30_0"
description: "shpc-registry automated BioContainers addition for pargenes"
config: {"url": "https://biocontainers.pro/tools/pargenes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pargenes", "latest": {"1.2.0--py27h8374a30_0": "sha256:95e0089c23d2ebb9235ab1324ac37628ef0da02f2711ea8ebedc0e634a806078"}, "tags": {"1.2.0--py27h8374a30_0": "sha256:95e0089c23d2ebb9235ab1324ac37628ef0da02f2711ea8ebedc0e634a806078"}, "docker": "quay.io/biocontainers/pargenes", "aliases": {"pargenes-hpc-debug.py": "/usr/local/bin/pargenes-hpc-debug.py", "pargenes-hpc.py": "/usr/local/bin/pargenes-hpc.py", "pargenes.py": "/usr/local/bin/pargenes.py", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info", "opal_wrapper": "/usr/local/bin/opal_wrapper", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info", "orte-server": "/usr/local/bin/orte-server"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pargenes.
shpc-registry automated BioContainers addition for pargenes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pargenes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pargenes:1.2.0--py27h8374a30_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pargenes/1.2.0--py27h8374a30_0
$ module help quay.io/biocontainers/pargenes/1.2.0--py27h8374a30_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pargenes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pargenes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pargenes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pargenes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pargenes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pargenes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pargenes-hpc-debug.py

```bash
$ singularity exec <container> /usr/local/bin/pargenes-hpc-debug.py
$ podman run --it --rm --entrypoint /usr/local/bin/pargenes-hpc-debug.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pargenes-hpc-debug.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pargenes-hpc.py

```bash
$ singularity exec <container> /usr/local/bin/pargenes-hpc.py
$ podman run --it --rm --entrypoint /usr/local/bin/pargenes-hpc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pargenes-hpc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pargenes.py

```bash
$ singularity exec <container> /usr/local/bin/pargenes.py
$ podman run --it --rm --entrypoint /usr/local/bin/pargenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pargenes.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_profile.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregate_profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### profile2mat.pl

```bash
$ singularity exec <container> /usr/local/bin/profile2mat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/profile2mat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/profile2mat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiCC

```bash
$ singularity exec <container> /usr/local/bin/mpiCC
$ podman run --it --rm --entrypoint /usr/local/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-clean

```bash
$ singularity exec <container> /usr/local/bin/ompi-clean
$ podman run --it --rm --entrypoint /usr/local/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-server

```bash
$ singularity exec <container> /usr/local/bin/ompi-server
$ podman run --it --rm --entrypoint /usr/local/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi_info

```bash
$ singularity exec <container> /usr/local/bin/ompi_info
$ podman run --it --rm --entrypoint /usr/local/bin/ompi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opal_wrapper

```bash
$ singularity exec <container> /usr/local/bin/opal_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/opal_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-clean

```bash
$ singularity exec <container> /usr/local/bin/orte-clean
$ podman run --it --rm --entrypoint /usr/local/bin/orte-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-info

```bash
$ singularity exec <container> /usr/local/bin/orte-info
$ podman run --it --rm --entrypoint /usr/local/bin/orte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-server

```bash
$ singularity exec <container> /usr/local/bin/orte-server
$ podman run --it --rm --entrypoint /usr/local/bin/orte-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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