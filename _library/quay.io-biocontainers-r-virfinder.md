---
layout: container
name:  "quay.io/biocontainers/r-virfinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-virfinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-virfinder/container.yaml"
updated_at: "2023-07-03 03:39:54.888445"
latest: "1.1--r42hdbdd923_6"
container_url: "https://biocontainers.pro/tools/r-virfinder"

versions:
 - "1.1--r41h87f3376_4"
 - "1.1--r42h87f3376_5"
 - "1.1--r42hdbdd923_6"
description: "shpc-registry automated BioContainers addition for r-virfinder"
config: {"url": "https://biocontainers.pro/tools/r-virfinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-virfinder", "latest": {"1.1--r42hdbdd923_6": "sha256:ffcccf5641832dfa2deedea9b62b893fb708eb44fa851cae8bef7a958b2a53f6"}, "tags": {"1.1--r41h87f3376_4": "sha256:f4001729c61fa7b1cff0308840c0dce7dc77a9ab9aea93a5b21f88d57f1b2412", "1.1--r42h87f3376_5": "sha256:d0d294ccca7a84028de4e06df204b61459c6ff6dfea76fb07e6f87b35443e3df", "1.1--r42hdbdd923_6": "sha256:ffcccf5641832dfa2deedea9b62b893fb708eb44fa851cae8bef7a958b2a53f6"}, "docker": "quay.io/biocontainers/r-virfinder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-virfinder.
shpc-registry automated BioContainers addition for r-virfinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-virfinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-virfinder:1.1--r42hdbdd923_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-virfinder/1.1--r42hdbdd923_6
$ module help quay.io/biocontainers/r-virfinder/1.1--r42hdbdd923_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-virfinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-virfinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-virfinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-virfinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-virfinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-virfinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-virfinder

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