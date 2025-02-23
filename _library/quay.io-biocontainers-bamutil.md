---
layout: container
name:  "quay.io/biocontainers/bamutil"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamutil/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamutil/container.yaml"
updated_at: "2025-02-23 03:18:55.021119"
latest: "1.0.15--h5ca1c30_6"
container_url: "https://biocontainers.pro/tools/bamutil"
aliases:
 - "bam"
versions:
 - "1.0.15--h5b5514e_2"
 - "1.0.15--h43eeafb_4"
 - "1.0.15--h43eeafb_5"
 - "1.0.15--h5ca1c30_6"
description: "shpc-registry automated BioContainers addition for bamutil"
config: {"url": "https://biocontainers.pro/tools/bamutil", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamutil", "latest": {"1.0.15--h5ca1c30_6": "sha256:a530d1b7769cf5e9d7cc0f4414f010caed7c1ab865469bc30db11163a9090de0"}, "tags": {"1.0.15--h5b5514e_2": "sha256:5a41de1d668490033b07716ddb6bab9ec52656587985ca2f42df9c206f552d0c", "1.0.15--h43eeafb_4": "sha256:1656a1b8d4a1d43dc815c4c2fac94137bfbaec850819c0992bb2f91360c622e9", "1.0.15--h43eeafb_5": "sha256:8ad26abab598d0823e478bc21fba2f3438484f968782a6c54132989654a85ec4", "1.0.15--h5ca1c30_6": "sha256:a530d1b7769cf5e9d7cc0f4414f010caed7c1ab865469bc30db11163a9090de0"}, "docker": "quay.io/biocontainers/bamutil", "aliases": {"bam": "/usr/local/bin/bam"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamutil.
shpc-registry automated BioContainers addition for bamutil
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamutil
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamutil:1.0.15--h5ca1c30_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamutil/1.0.15--h5ca1c30_6
$ module help quay.io/biocontainers/bamutil/1.0.15--h5ca1c30_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamutil-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamutil-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamutil-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamutil-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamutil-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamutil-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bam

```bash
$ singularity exec <container> /usr/local/bin/bam
$ podman run --it --rm --entrypoint /usr/local/bin/bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam   -v ${PWD} -w ${PWD} <container> -c " $@"
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