---
layout: container
name:  "quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1/container.yaml"
updated_at: "2025-11-01 04:00:01.357334"
latest: "4.6.2--hb2a3317_0"
container_url: "https://biocontainers.pro/tools/esme_netcdf-fortran_psmpi_5_12_1"
aliases:
 - "nf-config"
versions:
 - "4.6.2--hb2a3317_0"
description: "singularity registry hpc automated addition for esme_netcdf-fortran_psmpi_5_12_1"
config: {"url": "https://biocontainers.pro/tools/esme_netcdf-fortran_psmpi_5_12_1", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_netcdf-fortran_psmpi_5_12_1", "latest": {"4.6.2--hb2a3317_0": "sha256:142fd17166f0e587f6c7b74d6b234cace4a3edad5f5c044b1bbaee91a3d1a409"}, "tags": {"4.6.2--hb2a3317_0": "sha256:142fd17166f0e587f6c7b74d6b234cace4a3edad5f5c044b1bbaee91a3d1a409"}, "docker": "quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1", "aliases": {"nf-config": "/usr/local/bin/nf-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1.
singularity registry hpc automated addition for esme_netcdf-fortran_psmpi_5_12_1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1:4.6.2--hb2a3317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1/4.6.2--hb2a3317_0
$ module help quay.io/biocontainers/esme_netcdf-fortran_psmpi_5_12_1/4.6.2--hb2a3317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_netcdf-fortran_psmpi_5_12_1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_netcdf-fortran_psmpi_5_12_1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_netcdf-fortran_psmpi_5_12_1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_netcdf-fortran_psmpi_5_12_1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_netcdf-fortran_psmpi_5_12_1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_netcdf-fortran_psmpi_5_12_1-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nf-config

```bash
$ singularity exec <container> /usr/local/bin/nf-config
$ podman run --it --rm --entrypoint /usr/local/bin/nf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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