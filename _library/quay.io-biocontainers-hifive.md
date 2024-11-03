---
layout: container
name:  "quay.io/biocontainers/hifive"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hifive/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hifive/container.yaml"
updated_at: "2024-11-03 03:05:11.169633"
latest: "1.5.7--py27h20e14e4_4"
container_url: "https://biocontainers.pro/tools/hifive"
aliases:
 - "fetch_mrh_data"
 - "hifive"
 - "unit2"
 - "aggregate_profile.pl"
 - "profile2mat.pl"
 - "mpiCC"
 - "ompi-clean"
 - "ompi-server"
 - "ompi_info"
 - "opal_wrapper"
 - "orte-clean"
 - "orte-info"
versions:
 - "1.5.7--py27h20e14e4_4"
description: "shpc-registry automated BioContainers addition for hifive"
config: {"url": "https://biocontainers.pro/tools/hifive", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hifive", "latest": {"1.5.7--py27h20e14e4_4": "sha256:82318eb1c9364828ce4e187f2f442edbfeaa7e2d8e6ca9a4eef94208094ad0e4"}, "tags": {"1.5.7--py27h20e14e4_4": "sha256:82318eb1c9364828ce4e187f2f442edbfeaa7e2d8e6ca9a4eef94208094ad0e4"}, "docker": "quay.io/biocontainers/hifive", "aliases": {"fetch_mrh_data": "/usr/local/bin/fetch_mrh_data", "hifive": "/usr/local/bin/hifive", "unit2": "/usr/local/bin/unit2", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info", "opal_wrapper": "/usr/local/bin/opal_wrapper", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hifive.
shpc-registry automated BioContainers addition for hifive
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hifive
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hifive:1.5.7--py27h20e14e4_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hifive/1.5.7--py27h20e14e4_4
$ module help quay.io/biocontainers/hifive/1.5.7--py27h20e14e4_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hifive-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hifive-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hifive-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hifive-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hifive-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hifive-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fetch_mrh_data

```bash
$ singularity exec <container> /usr/local/bin/fetch_mrh_data
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_mrh_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_mrh_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hifive

```bash
$ singularity exec <container> /usr/local/bin/hifive
$ podman run --it --rm --entrypoint /usr/local/bin/hifive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hifive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unit2

```bash
$ singularity exec <container> /usr/local/bin/unit2
$ podman run --it --rm --entrypoint /usr/local/bin/unit2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unit2   -v ${PWD} -w ${PWD} <container> -c " $@"
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