---
layout: container
name:  "quay.io/biocontainers/kractor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kractor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kractor/container.yaml"
updated_at: "2025-09-08 03:32:27.722188"
latest: "2.0.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/kractor"
aliases:
 - "kractor"
versions:
 - "1.0.0--h4349ce8_0"
 - "1.0.1--h4349ce8_0"
 - "2.0.0--h4349ce8_0"
description: "singularity registry hpc automated addition for kractor"
config: {"url": "https://biocontainers.pro/tools/kractor", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kractor", "latest": {"2.0.0--h4349ce8_0": "sha256:6c68c3089085440655dc70b22250265f5fbce25f4ab1c389d358ed65c3e3b564"}, "tags": {"1.0.0--h4349ce8_0": "sha256:7596b534ec304f43aedf897766f976a86307bbca13604dc8b1e67fbfe35a6801", "1.0.1--h4349ce8_0": "sha256:1a9a715084dae52e436c7a291d0585ae68674ecd1a28163124c41d8a17e301bf", "2.0.0--h4349ce8_0": "sha256:6c68c3089085440655dc70b22250265f5fbce25f4ab1c389d358ed65c3e3b564"}, "docker": "quay.io/biocontainers/kractor", "aliases": {"kractor": "/usr/local/bin/kractor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kractor.
singularity registry hpc automated addition for kractor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kractor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kractor:2.0.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kractor/2.0.0--h4349ce8_0
$ module help quay.io/biocontainers/kractor/2.0.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kractor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kractor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kractor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kractor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kractor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kractor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kractor

```bash
$ singularity exec <container> /usr/local/bin/kractor
$ podman run --it --rm --entrypoint /usr/local/bin/kractor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kractor   -v ${PWD} -w ${PWD} <container> -c " $@"
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