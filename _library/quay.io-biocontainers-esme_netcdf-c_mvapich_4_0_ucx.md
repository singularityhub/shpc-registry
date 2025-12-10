---
layout: container
name:  "quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx/container.yaml"
updated_at: "2025-12-10 04:02:18.279856"
latest: "4.9.3--hdf4d085_0"
container_url: "https://biocontainers.pro/tools/esme_netcdf-c_mvapich_4_0_ucx"
aliases:
 - "nc4print"
 - "ocprint"
 - "nc-config"
 - "nccopy"
 - "ncdump"
 - "ncgen"
 - "ncgen3"
versions:
 - "4.9.3--hdf4d085_0"
description: "singularity registry hpc automated addition for esme_netcdf-c_mvapich_4_0_ucx"
config: {"url": "https://biocontainers.pro/tools/esme_netcdf-c_mvapich_4_0_ucx", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_netcdf-c_mvapich_4_0_ucx", "latest": {"4.9.3--hdf4d085_0": "sha256:cf3f446e9a4963ede92e422a44db1ed01d73539be99c28bf6a44056ca3ed02ef"}, "tags": {"4.9.3--hdf4d085_0": "sha256:cf3f446e9a4963ede92e422a44db1ed01d73539be99c28bf6a44056ca3ed02ef"}, "docker": "quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx", "aliases": {"nc4print": "/usr/local/bin/nc4print", "ocprint": "/usr/local/bin/ocprint", "nc-config": "/usr/local/bin/nc-config", "nccopy": "/usr/local/bin/nccopy", "ncdump": "/usr/local/bin/ncdump", "ncgen": "/usr/local/bin/ncgen", "ncgen3": "/usr/local/bin/ncgen3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx.
singularity registry hpc automated addition for esme_netcdf-c_mvapich_4_0_ucx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx:4.9.3--hdf4d085_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx/4.9.3--hdf4d085_0
$ module help quay.io/biocontainers/esme_netcdf-c_mvapich_4_0_ucx/4.9.3--hdf4d085_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_netcdf-c_mvapich_4_0_ucx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_netcdf-c_mvapich_4_0_ucx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_netcdf-c_mvapich_4_0_ucx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_netcdf-c_mvapich_4_0_ucx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_netcdf-c_mvapich_4_0_ucx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_netcdf-c_mvapich_4_0_ucx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nc4print

```bash
$ singularity exec <container> /usr/local/bin/nc4print
$ podman run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocprint

```bash
$ singularity exec <container> /usr/local/bin/ocprint
$ podman run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc-config

```bash
$ singularity exec <container> /usr/local/bin/nc-config
$ podman run --it --rm --entrypoint /usr/local/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nccopy

```bash
$ singularity exec <container> /usr/local/bin/nccopy
$ podman run --it --rm --entrypoint /usr/local/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncdump

```bash
$ singularity exec <container> /usr/local/bin/ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen

```bash
$ singularity exec <container> /usr/local/bin/ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen3

```bash
$ singularity exec <container> /usr/local/bin/ncgen3
$ podman run --it --rm --entrypoint /usr/local/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
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