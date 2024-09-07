---
layout: container
name:  "quay.io/biocontainers/gcta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gcta/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gcta/container.yaml"
updated_at: "2024-09-07 02:48:14.662903"
latest: "1.94.1--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/gcta"
aliases:
 - "gcta64"
versions:
 - "1.93.2beta--h9ee0642_1"
 - "1.94.1--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for gcta"
config: {"url": "https://biocontainers.pro/tools/gcta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gcta", "latest": {"1.94.1--h9ee0642_0": "sha256:14708fd307cb7fc19b9991553f33539502370ecd2b377a8815d830ca9df77967"}, "tags": {"1.93.2beta--h9ee0642_1": "sha256:f0b0a7f6810020ece4400d56832d19316668222a27217731a06d13f51d81fe6b", "1.94.1--h9ee0642_0": "sha256:14708fd307cb7fc19b9991553f33539502370ecd2b377a8815d830ca9df77967"}, "docker": "quay.io/biocontainers/gcta", "aliases": {"gcta64": "/usr/local/bin/gcta64"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gcta.
shpc-registry automated BioContainers addition for gcta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gcta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gcta:1.94.1--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gcta/1.94.1--h9ee0642_0
$ module help quay.io/biocontainers/gcta/1.94.1--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gcta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gcta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gcta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gcta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gcta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gcta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gcta64

```bash
$ singularity exec <container> /usr/local/bin/gcta64
$ podman run --it --rm --entrypoint /usr/local/bin/gcta64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcta64   -v ${PWD} -w ${PWD} <container> -c " $@"
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