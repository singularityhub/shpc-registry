---
layout: container
name:  "quay.io/biocontainers/r-ipo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ipo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ipo/container.yaml"
updated_at: "2025-03-06 03:49:27.158352"
latest: "1.7.5--r3.3.1_0"
container_url: "https://biocontainers.pro/tools/r-ipo"

versions:
 - "1.7.5--r3.3.1_0"
 - "1.7.5--r3.3.2_0"
 - "1.7.5--r3.2.2_0"
description: "shpc-registry automated BioContainers addition for r-ipo"
config: {"url": "https://biocontainers.pro/tools/r-ipo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ipo", "latest": {"1.7.5--r3.3.1_0": "sha256:711fc97670c5175619c1e3a222bdeac1a749decd9d35757a382fb29b85acfc99"}, "tags": {"1.7.5--r3.3.1_0": "sha256:711fc97670c5175619c1e3a222bdeac1a749decd9d35757a382fb29b85acfc99", "1.7.5--r3.3.2_0": "sha256:c4c1275055791ba36aa71d983bf9f5aa64bc4ea94f143bde20c9f4565e0f6cb8", "1.7.5--r3.2.2_0": "sha256:d049243bb6b6ba9abe72710d4883f7ac25afa089e0f2fa429ec11313920d7dcf"}, "docker": "quay.io/biocontainers/r-ipo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ipo.
shpc-registry automated BioContainers addition for r-ipo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ipo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ipo:1.7.5--r3.3.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ipo/1.7.5--r3.3.1_0
$ module help quay.io/biocontainers/r-ipo/1.7.5--r3.3.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ipo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ipo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ipo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ipo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ipo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ipo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-ipo

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