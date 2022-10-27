---
layout: container
name:  "quay.io/biocontainers/dammet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dammet/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dammet/container.yaml"
updated_at: "2022-10-27 01:11:50.043715"
latest: "1.0.1a--h5e47628_6"
container_url: "https://biocontainers.pro/tools/dammet"
aliases:
 - "DamMet"
versions:
 - "1.0.1a--h5e47628_6"
description: "shpc-registry automated BioContainers addition for dammet"
config: {"url": "https://biocontainers.pro/tools/dammet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dammet", "latest": {"1.0.1a--h5e47628_6": "sha256:0c78d978ef090757f7a7a017f0e31bf886308c6c930e86d10501a086d8096131"}, "tags": {"1.0.1a--h5e47628_6": "sha256:0c78d978ef090757f7a7a017f0e31bf886308c6c930e86d10501a086d8096131"}, "docker": "quay.io/biocontainers/dammet", "aliases": {"DamMet": "/usr/local/bin/DamMet"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dammet.
shpc-registry automated BioContainers addition for dammet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dammet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dammet:1.0.1a--h5e47628_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dammet/1.0.1a--h5e47628_6
$ module help quay.io/biocontainers/dammet/1.0.1a--h5e47628_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dammet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dammet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dammet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dammet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dammet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dammet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DamMet

```bash
$ singularity exec <container> /usr/local/bin/DamMet
$ podman run --it --rm --entrypoint /usr/local/bin/DamMet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DamMet   -v ${PWD} -w ${PWD} <container> -c " $@"
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