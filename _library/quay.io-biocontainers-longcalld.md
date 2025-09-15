---
layout: container
name:  "quay.io/biocontainers/longcalld"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/longcalld/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/longcalld/container.yaml"
updated_at: "2025-09-15 03:21:32.976550"
latest: "0.0.5--h7d57edc_0"
container_url: "https://biocontainers.pro/tools/longcalld"
aliases:
 - "longcallD"
versions:
 - "0.0.4--h7d57edc_0"
 - "0.0.4--h7d57edc_1"
 - "0.0.5--h7d57edc_0"
description: "singularity registry hpc automated addition for longcalld"
config: {"url": "https://biocontainers.pro/tools/longcalld", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for longcalld", "latest": {"0.0.5--h7d57edc_0": "sha256:d0e9c50119a43b3ef5d17142d0794da44991aab06bf86f2eded5c91af4d730c9"}, "tags": {"0.0.4--h7d57edc_0": "sha256:2faac568a800c57b996353c203c1c4bce9a50b498ee1ce40a7c8ecc4fa261455", "0.0.4--h7d57edc_1": "sha256:623c78e058a4ee356c05b7bee3d4b48646deac99108301f89540fc6509041283", "0.0.5--h7d57edc_0": "sha256:d0e9c50119a43b3ef5d17142d0794da44991aab06bf86f2eded5c91af4d730c9"}, "docker": "quay.io/biocontainers/longcalld", "aliases": {"longcallD": "/usr/local/bin/longcallD"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/longcalld.
singularity registry hpc automated addition for longcalld
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/longcalld
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/longcalld:0.0.5--h7d57edc_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/longcalld/0.0.5--h7d57edc_0
$ module help quay.io/biocontainers/longcalld/0.0.5--h7d57edc_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### longcalld-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### longcalld-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### longcalld-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### longcalld-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### longcalld-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### longcalld-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### longcallD

```bash
$ singularity exec <container> /usr/local/bin/longcallD
$ podman run --it --rm --entrypoint /usr/local/bin/longcallD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longcallD   -v ${PWD} -w ${PWD} <container> -c " $@"
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