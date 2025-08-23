---
layout: container
name:  "quay.io/biocontainers/cgat-scripts"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgat-scripts/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cgat-scripts/container.yaml"
updated_at: "2025-08-23 03:52:39.813464"
latest: "0.3.2--py36h355e19c_2"
container_url: "https://biocontainers.pro/tools/cgat-scripts"

versions:
 - "0.3.2--py36h355e19c_2"
 - "0.3.2--py35h355e19c_2"
description: "shpc-registry automated BioContainers addition for cgat-scripts"
config: {"url": "https://biocontainers.pro/tools/cgat-scripts", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgat-scripts", "latest": {"0.3.2--py36h355e19c_2": "sha256:49101ceb5e3c0f7a8e4cf575bc8b8d76a7a03cdb8838085d2a480eb50e3327c7"}, "tags": {"0.3.2--py36h355e19c_2": "sha256:49101ceb5e3c0f7a8e4cf575bc8b8d76a7a03cdb8838085d2a480eb50e3327c7", "0.3.2--py35h355e19c_2": "sha256:020c1c4b268755809e52998dee93d6db69787f7ef9857e5f21ccd310e409960c"}, "docker": "quay.io/biocontainers/cgat-scripts"}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgat-scripts.
shpc-registry automated BioContainers addition for cgat-scripts
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgat-scripts
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgat-scripts:0.3.2--py36h355e19c_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgat-scripts/0.3.2--py36h355e19c_2
$ module help quay.io/biocontainers/cgat-scripts/0.3.2--py36h355e19c_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cgat-scripts-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cgat-scripts-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cgat-scripts-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cgat-scripts-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cgat-scripts-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cgat-scripts-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### cgat-scripts

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