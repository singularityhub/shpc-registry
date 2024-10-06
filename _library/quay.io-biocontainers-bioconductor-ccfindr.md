---
layout: container
name:  "quay.io/biocontainers/bioconductor-ccfindr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ccfindr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ccfindr/container.yaml"
updated_at: "2024-10-06 03:20:45.157160"
latest: "1.22.0--r43h7c4fd5e_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ccfindr"
aliases:
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
 - "1.8.0--r40h5f743cb_0"
 - "1.18.0--r42hc247a5b_0"
 - "1.14.0--r41hc247a5b_2"
 - "1.12.0--r41h399db7b_0"
 - "1.10.0--r40h399db7b_1"
 - "1.18.0--r42hf17093f_1"
 - "1.20.0--r43hf17093f_0"
 - "1.22.0--r43h7c4fd5e_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ccfindr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ccfindr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ccfindr", "latest": {"1.22.0--r43h7c4fd5e_0": "sha256:9eee3d9d7abf77bb104b8f21ce5286a0d15626dbced621d451e864000184421f"}, "tags": {"1.8.0--r40h5f743cb_0": "sha256:d073f895818d84225ac8b44392d728ebc910d066a9baf22d57f5faef239a8035", "1.18.0--r42hc247a5b_0": "sha256:e79d0fa05cfb5f68d00a5e3ca6834c42216a3154950711b7296dafd9e242ee15", "1.14.0--r41hc247a5b_2": "sha256:8a478898376fee90422a4ac418d4cd961f23ba96f7cdd8c0e0bed5c761bf029e", "1.12.0--r41h399db7b_0": "sha256:9cc38add8058259b1dbe16f3ca6c698b0c80d8f59ab5672e174f0b102a46accb", "1.10.0--r40h399db7b_1": "sha256:1652d6feb16b40c2e7ed1de27c25b8c3702b7c76cc2366f557306670ea526edc", "1.18.0--r42hf17093f_1": "sha256:df85c7d81b4a82777abd6a1ed33dc65632414f6b60cabe3c6d579432a51147f3", "1.20.0--r43hf17093f_0": "sha256:dc22d8e2bd5a762204017e22aaa4b89c2dd7e10878d85dfd7cc4c37cbaf3e322", "1.22.0--r43h7c4fd5e_0": "sha256:9eee3d9d7abf77bb104b8f21ce5286a0d15626dbced621d451e864000184421f"}, "docker": "quay.io/biocontainers/bioconductor-ccfindr", "aliases": {"aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info", "opal_wrapper": "/usr/local/bin/opal_wrapper", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info", "orte-server": "/usr/local/bin/orte-server"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ccfindr.
shpc-registry automated BioContainers addition for bioconductor-ccfindr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ccfindr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ccfindr:1.22.0--r43h7c4fd5e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ccfindr/1.22.0--r43h7c4fd5e_0
$ module help quay.io/biocontainers/bioconductor-ccfindr/1.22.0--r43h7c4fd5e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ccfindr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccfindr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccfindr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ccfindr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ccfindr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ccfindr-inspect-deffile:

```bash
$ singularity inspect -d <container>
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