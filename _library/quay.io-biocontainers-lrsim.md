---
layout: container
name:  "quay.io/biocontainers/lrsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lrsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lrsim/container.yaml"
updated_at: "2023-12-25 02:40:36.214261"
latest: "1.0--pl5321hbcd995c_0"
container_url: "https://biocontainers.pro/tools/lrsim"
aliases:
 - "lrsim"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0--pl5321hbcd995c_0"
description: "singularity registry hpc automated addition for lrsim"
config: {"url": "https://biocontainers.pro/tools/lrsim", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for lrsim", "latest": {"1.0--pl5321hbcd995c_0": "sha256:c2552d2c9faec07545dfae5e9c7b340d21580250e88119b393e58c261e76ab31"}, "tags": {"1.0--pl5321hbcd995c_0": "sha256:c2552d2c9faec07545dfae5e9c7b340d21580250e88119b393e58c261e76ab31"}, "docker": "quay.io/biocontainers/lrsim", "aliases": {"lrsim": "/usr/local/bin/lrsim", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lrsim.
singularity registry hpc automated addition for lrsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lrsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lrsim:1.0--pl5321hbcd995c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lrsim/1.0--pl5321hbcd995c_0
$ module help quay.io/biocontainers/lrsim/1.0--pl5321hbcd995c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lrsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lrsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lrsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lrsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lrsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lrsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lrsim

```bash
$ singularity exec <container> /usr/local/bin/lrsim
$ podman run --it --rm --entrypoint /usr/local/bin/lrsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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