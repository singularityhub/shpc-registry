---
layout: container
name:  "quay.io/biocontainers/d4tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/d4tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/d4tools/container.yaml"
updated_at: "2026-01-13 04:22:01.371967"
latest: "0.3.11--ha986137_3"
container_url: "https://biocontainers.pro/tools/d4tools"
aliases:
 - "d4tools"
 - "starcode"
versions:
 - "0.3.8--h87f3376_0"
 - "0.3.8--hdbdd923_1"
 - "0.3.10--h4c94732_1"
 - "0.3.11--h4c94732_0"
 - "0.3.11--h4c94732_1"
 - "0.3.11--h3ab6199_2"
 - "0.3.11--ha986137_3"
description: "singularity registry hpc automated addition for d4tools"
config: {"url": "https://biocontainers.pro/tools/d4tools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for d4tools", "latest": {"0.3.11--ha986137_3": "sha256:ec82fec4e1b68eb80ea25c0c8b278e377c31122824a0ade191445cc2a408e139"}, "tags": {"0.3.8--h87f3376_0": "sha256:cee34924572fe75db1e653d33953b6824701544478f2a38d40abe2cc59132916", "0.3.8--hdbdd923_1": "sha256:3f6e427b4b2dc4860e21fd106924a46569b8590e7597a8748247467d556bd594", "0.3.10--h4c94732_1": "sha256:ceb8c629fe100a6daae990269bd015a7a69210a61e0055f297e0b6e7e9cf6573", "0.3.11--h4c94732_0": "sha256:4f4585cf95073a0ecf701f567d991118fe4c8c44240519547adfc67584a23d33", "0.3.11--h4c94732_1": "sha256:2f5baeb28d6ea84216bd0f68e5691c822862750dedd8f634efab1b8a243d64a8", "0.3.11--h3ab6199_2": "sha256:1d67bd02b3c8df64473065a26789ba88f223b2140bcc0db1025fd97dfbabced2", "0.3.11--ha986137_3": "sha256:ec82fec4e1b68eb80ea25c0c8b278e377c31122824a0ade191445cc2a408e139"}, "docker": "quay.io/biocontainers/d4tools", "aliases": {"d4tools": "/usr/local/bin/d4tools", "starcode": "/usr/local/bin/starcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/d4tools.
singularity registry hpc automated addition for d4tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/d4tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/d4tools:0.3.11--ha986137_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/d4tools/0.3.11--ha986137_3
$ module help quay.io/biocontainers/d4tools/0.3.11--ha986137_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### d4tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### d4tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### d4tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### d4tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### d4tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### d4tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### d4tools

```bash
$ singularity exec <container> /usr/local/bin/d4tools
$ podman run --it --rm --entrypoint /usr/local/bin/d4tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/d4tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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