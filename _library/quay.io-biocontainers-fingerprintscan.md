---
layout: container
name:  "quay.io/biocontainers/fingerprintscan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fingerprintscan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fingerprintscan/container.yaml"
updated_at: "2024-03-17 03:02:16.883933"
latest: "3_597--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/fingerprintscan"
aliases:
 - "fingerPRINTScan"
versions:
 - "3_597--h9f5acd7_2"
 - "3_597--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for fingerprintscan"
config: {"url": "https://biocontainers.pro/tools/fingerprintscan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fingerprintscan", "latest": {"3_597--h4ac6f70_4": "sha256:08ff97edd50f6999dfee28104efa39ea9c443c2c3175eb9fdf1dedfa6d2f1d40"}, "tags": {"3_597--h9f5acd7_2": "sha256:556c6fbb16e97eaf3bf157c69b599feb7489d52e21e80d17187bc4e413a2e604", "3_597--h4ac6f70_4": "sha256:08ff97edd50f6999dfee28104efa39ea9c443c2c3175eb9fdf1dedfa6d2f1d40"}, "docker": "quay.io/biocontainers/fingerprintscan", "aliases": {"fingerPRINTScan": "/usr/local/bin/fingerPRINTScan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fingerprintscan.
shpc-registry automated BioContainers addition for fingerprintscan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fingerprintscan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fingerprintscan:3_597--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fingerprintscan/3_597--h4ac6f70_4
$ module help quay.io/biocontainers/fingerprintscan/3_597--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fingerprintscan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fingerprintscan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fingerprintscan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fingerprintscan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fingerprintscan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fingerprintscan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fingerPRINTScan

```bash
$ singularity exec <container> /usr/local/bin/fingerPRINTScan
$ podman run --it --rm --entrypoint /usr/local/bin/fingerPRINTScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fingerPRINTScan   -v ${PWD} -w ${PWD} <container> -c " $@"
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