---
layout: container
name:  "quay.io/biocontainers/seidr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seidr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seidr/container.yaml"
updated_at: "2024-04-30 02:40:27.249101"
latest: "0.14.2--mpi_mpich_h0475154"
container_url: "https://biocontainers.pro/tools/seidr"
aliases:
 - "anoverence"
 - "correlation"
 - "el-ensemble"
 - "genie3"
 - "llr-ensemble"
 - "mi"
 - "narromi"
 - "pcor"
 - "plsnet"
 - "seidr"
 - "svm-ensemble"
 - "tigress"
 - "tomsimilarity"
 - "clp"
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
 - "0.14.2--mpi_openmpi_h430a956"
 - "0.14.2--mpi_mpich_h0475154"
description: "shpc-registry automated BioContainers addition for seidr"
config: {"url": "https://biocontainers.pro/tools/seidr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seidr", "latest": {"0.14.2--mpi_mpich_h0475154": "sha256:572073dbddd2ed38215a93f16b6bd99f5a18205b5bfc96b58e29cee2a739d2c4"}, "tags": {"0.14.2--mpi_openmpi_h430a956": "sha256:fad286334f630046f070f4c1fc050289723a1fb140a4161873c8105e4efbdefc", "0.14.2--mpi_mpich_h0475154": "sha256:572073dbddd2ed38215a93f16b6bd99f5a18205b5bfc96b58e29cee2a739d2c4"}, "docker": "quay.io/biocontainers/seidr", "aliases": {"anoverence": "/usr/local/bin/anoverence", "correlation": "/usr/local/bin/correlation", "el-ensemble": "/usr/local/bin/el-ensemble", "genie3": "/usr/local/bin/genie3", "llr-ensemble": "/usr/local/bin/llr-ensemble", "mi": "/usr/local/bin/mi", "narromi": "/usr/local/bin/narromi", "pcor": "/usr/local/bin/pcor", "plsnet": "/usr/local/bin/plsnet", "seidr": "/usr/local/bin/seidr", "svm-ensemble": "/usr/local/bin/svm-ensemble", "tigress": "/usr/local/bin/tigress", "tomsimilarity": "/usr/local/bin/tomsimilarity", "clp": "/usr/local/bin/clp", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info", "opal_wrapper": "/usr/local/bin/opal_wrapper", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seidr.
shpc-registry automated BioContainers addition for seidr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seidr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seidr:0.14.2--mpi_mpich_h0475154
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seidr/0.14.2--mpi_mpich_h0475154
$ module help quay.io/biocontainers/seidr/0.14.2--mpi_mpich_h0475154
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seidr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seidr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seidr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seidr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seidr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seidr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### anoverence

```bash
$ singularity exec <container> /usr/local/bin/anoverence
$ podman run --it --rm --entrypoint /usr/local/bin/anoverence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anoverence   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### correlation

```bash
$ singularity exec <container> /usr/local/bin/correlation
$ podman run --it --rm --entrypoint /usr/local/bin/correlation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correlation   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### el-ensemble

```bash
$ singularity exec <container> /usr/local/bin/el-ensemble
$ podman run --it --rm --entrypoint /usr/local/bin/el-ensemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/el-ensemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genie3

```bash
$ singularity exec <container> /usr/local/bin/genie3
$ podman run --it --rm --entrypoint /usr/local/bin/genie3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genie3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### llr-ensemble

```bash
$ singularity exec <container> /usr/local/bin/llr-ensemble
$ podman run --it --rm --entrypoint /usr/local/bin/llr-ensemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/llr-ensemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mi

```bash
$ singularity exec <container> /usr/local/bin/mi
$ podman run --it --rm --entrypoint /usr/local/bin/mi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### narromi

```bash
$ singularity exec <container> /usr/local/bin/narromi
$ podman run --it --rm --entrypoint /usr/local/bin/narromi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/narromi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcor

```bash
$ singularity exec <container> /usr/local/bin/pcor
$ podman run --it --rm --entrypoint /usr/local/bin/pcor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plsnet

```bash
$ singularity exec <container> /usr/local/bin/plsnet
$ podman run --it --rm --entrypoint /usr/local/bin/plsnet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plsnet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seidr

```bash
$ singularity exec <container> /usr/local/bin/seidr
$ podman run --it --rm --entrypoint /usr/local/bin/seidr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seidr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-ensemble

```bash
$ singularity exec <container> /usr/local/bin/svm-ensemble
$ podman run --it --rm --entrypoint /usr/local/bin/svm-ensemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-ensemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tigress

```bash
$ singularity exec <container> /usr/local/bin/tigress
$ podman run --it --rm --entrypoint /usr/local/bin/tigress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tigress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tomsimilarity

```bash
$ singularity exec <container> /usr/local/bin/tomsimilarity
$ podman run --it --rm --entrypoint /usr/local/bin/tomsimilarity   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tomsimilarity   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clp

```bash
$ singularity exec <container> /usr/local/bin/clp
$ podman run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clp   -v ${PWD} -w ${PWD} <container> -c " $@"
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