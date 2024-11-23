---
layout: container
name:  "quay.io/biocontainers/ccphylo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ccphylo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ccphylo/container.yaml"
updated_at: "2024-11-23 03:16:10.488321"
latest: "0.8.2--he4a0461_2"
container_url: "https://biocontainers.pro/tools/ccphylo"
aliases:
 - "ccphylo"
versions:
 - "0.8.2--h7132678_0"
 - "0.8.2--he4a0461_2"
description: "singularity registry hpc automated addition for ccphylo"
config: {"url": "https://biocontainers.pro/tools/ccphylo", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ccphylo", "latest": {"0.8.2--he4a0461_2": "sha256:5897aa4f51a05e620ac9ac66ff04d696142859dde3ead10f169a7ee620b24811"}, "tags": {"0.8.2--h7132678_0": "sha256:7b1fd511eed14e02f016ee231db7d3e2c8285dee061c0f094d3ff0d2a45eccae", "0.8.2--he4a0461_2": "sha256:5897aa4f51a05e620ac9ac66ff04d696142859dde3ead10f169a7ee620b24811"}, "docker": "quay.io/biocontainers/ccphylo", "aliases": {"ccphylo": "/usr/local/bin/ccphylo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ccphylo.
singularity registry hpc automated addition for ccphylo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ccphylo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ccphylo:0.8.2--he4a0461_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ccphylo/0.8.2--he4a0461_2
$ module help quay.io/biocontainers/ccphylo/0.8.2--he4a0461_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ccphylo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ccphylo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ccphylo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ccphylo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ccphylo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ccphylo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccphylo

```bash
$ singularity exec <container> /usr/local/bin/ccphylo
$ podman run --it --rm --entrypoint /usr/local/bin/ccphylo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccphylo   -v ${PWD} -w ${PWD} <container> -c " $@"
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