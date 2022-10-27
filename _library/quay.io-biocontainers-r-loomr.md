---
layout: container
name:  "quay.io/biocontainers/r-loomr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-loomr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-loomr/container.yaml"
updated_at: "2022-10-27 01:01:33.448336"
latest: "0.2.0_beta--r41hdfd78af_3"
container_url: "https://biocontainers.pro/tools/r-loomr"

versions:
 - "0.2.0_beta--r41hdfd78af_3"
description: "shpc-registry automated BioContainers addition for r-loomr"
config: {"url": "https://biocontainers.pro/tools/r-loomr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-loomr", "latest": {"0.2.0_beta--r41hdfd78af_3": "sha256:23cb619943d10d6831894b77f296983607183e76e3cd17c0ca7d1eb137b296ab"}, "tags": {"0.2.0_beta--r41hdfd78af_3": "sha256:23cb619943d10d6831894b77f296983607183e76e3cd17c0ca7d1eb137b296ab"}, "docker": "quay.io/biocontainers/r-loomr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-loomr.
shpc-registry automated BioContainers addition for r-loomr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-loomr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-loomr:0.2.0_beta--r41hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-loomr/0.2.0_beta--r41hdfd78af_3
$ module help quay.io/biocontainers/r-loomr/0.2.0_beta--r41hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-loomr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-loomr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-loomr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-loomr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-loomr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-loomr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-loomr

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