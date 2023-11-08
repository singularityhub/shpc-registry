---
layout: container
name:  "quay.io/biocontainers/libbambamc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libbambamc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libbambamc/container.yaml"
updated_at: "2023-11-08 02:45:24.765545"
latest: "0.0.50--he4a0461_5"
container_url: "https://biocontainers.pro/tools/libbambamc"

versions:
 - "0.0.50--h7132678_3"
 - "0.0.50--he4a0461_5"
description: "shpc-registry automated BioContainers addition for libbambamc"
config: {"url": "https://biocontainers.pro/tools/libbambamc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libbambamc", "latest": {"0.0.50--he4a0461_5": "sha256:0d701fd1caf0ade504ecffeedbb95932d45f7693ca4a77c794f253920a0d3add"}, "tags": {"0.0.50--h7132678_3": "sha256:50404e5571b3e0e69017283966d2b1326673482a20298ad9c0c070ffa84782cb", "0.0.50--he4a0461_5": "sha256:0d701fd1caf0ade504ecffeedbb95932d45f7693ca4a77c794f253920a0d3add"}, "docker": "quay.io/biocontainers/libbambamc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libbambamc.
shpc-registry automated BioContainers addition for libbambamc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libbambamc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libbambamc:0.0.50--he4a0461_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libbambamc/0.0.50--he4a0461_5
$ module help quay.io/biocontainers/libbambamc/0.0.50--he4a0461_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libbambamc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libbambamc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libbambamc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libbambamc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libbambamc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libbambamc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libbambamc

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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