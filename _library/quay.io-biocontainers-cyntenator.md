---
layout: container
name:  "quay.io/biocontainers/cyntenator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cyntenator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cyntenator/container.yaml"
updated_at: "2023-07-01 03:26:53.393653"
latest: "0.0.r2326--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/cyntenator"
aliases:
 - "cyntenator"
versions:
 - "0.0.r2326--h9f5acd7_1"
 - "0.0.r2326--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for cyntenator"
config: {"url": "https://biocontainers.pro/tools/cyntenator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cyntenator", "latest": {"0.0.r2326--h4ac6f70_3": "sha256:687b7cc1d74d06a7d058dfc02e5c81d39e375e2e0f8bcd0479ab093e69ca2862"}, "tags": {"0.0.r2326--h9f5acd7_1": "sha256:ae28c25e18ba5128d5b1aad96173b186643e81d43fef755f1513f548b7aa5c4c", "0.0.r2326--h4ac6f70_3": "sha256:687b7cc1d74d06a7d058dfc02e5c81d39e375e2e0f8bcd0479ab093e69ca2862"}, "docker": "quay.io/biocontainers/cyntenator", "aliases": {"cyntenator": "/usr/local/bin/cyntenator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cyntenator.
shpc-registry automated BioContainers addition for cyntenator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cyntenator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cyntenator:0.0.r2326--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cyntenator/0.0.r2326--h4ac6f70_3
$ module help quay.io/biocontainers/cyntenator/0.0.r2326--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cyntenator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cyntenator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cyntenator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cyntenator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cyntenator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cyntenator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cyntenator

```bash
$ singularity exec <container> /usr/local/bin/cyntenator
$ podman run --it --rm --entrypoint /usr/local/bin/cyntenator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyntenator   -v ${PWD} -w ${PWD} <container> -c " $@"
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