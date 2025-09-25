---
layout: container
name:  "quay.io/biocontainers/paf2chain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/paf2chain/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/paf2chain/container.yaml"
updated_at: "2025-09-25 07:27:44.201934"
latest: "0.1.1--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/paf2chain"
aliases:
 - "paf2chain"
versions:
 - "0.1.1--h3ab6199_0"
description: "singularity registry hpc automated addition for paf2chain"
config: {"url": "https://biocontainers.pro/tools/paf2chain", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for paf2chain", "latest": {"0.1.1--h3ab6199_0": "sha256:8a39e2681677f6992f09bb875a21fe4e6c2fa20cbdbcc8d177cef193f0153a35"}, "tags": {"0.1.1--h3ab6199_0": "sha256:8a39e2681677f6992f09bb875a21fe4e6c2fa20cbdbcc8d177cef193f0153a35"}, "docker": "quay.io/biocontainers/paf2chain", "aliases": {"paf2chain": "/usr/local/bin/paf2chain"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/paf2chain.
singularity registry hpc automated addition for paf2chain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/paf2chain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/paf2chain:0.1.1--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/paf2chain/0.1.1--h3ab6199_0
$ module help quay.io/biocontainers/paf2chain/0.1.1--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### paf2chain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### paf2chain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### paf2chain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### paf2chain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### paf2chain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### paf2chain-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### paf2chain

```bash
$ singularity exec <container> /usr/local/bin/paf2chain
$ podman run --it --rm --entrypoint /usr/local/bin/paf2chain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paf2chain   -v ${PWD} -w ${PWD} <container> -c " $@"
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