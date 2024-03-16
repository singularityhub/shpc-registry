---
layout: container
name:  "quay.io/biocontainers/nanoblaster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanoblaster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanoblaster/container.yaml"
updated_at: "2024-03-16 02:55:21.056612"
latest: "0.16--h4ac6f70_6"
container_url: "https://biocontainers.pro/tools/nanoblaster"
aliases:
 - "nanoblaster"
versions:
 - "0.16--h9f5acd7_4"
 - "0.16--h4ac6f70_6"
description: "shpc-registry automated BioContainers addition for nanoblaster"
config: {"url": "https://biocontainers.pro/tools/nanoblaster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanoblaster", "latest": {"0.16--h4ac6f70_6": "sha256:6632cc7f9598e16fbf6710b39cc564d7fbdeb7d24d825f0631f81f4054386610"}, "tags": {"0.16--h9f5acd7_4": "sha256:73ee53ad59067f97d64f82bcca43fa0906f68e57342a695e4d7b708bdef99424", "0.16--h4ac6f70_6": "sha256:6632cc7f9598e16fbf6710b39cc564d7fbdeb7d24d825f0631f81f4054386610"}, "docker": "quay.io/biocontainers/nanoblaster", "aliases": {"nanoblaster": "/usr/local/bin/nanoblaster"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanoblaster.
shpc-registry automated BioContainers addition for nanoblaster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanoblaster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanoblaster:0.16--h4ac6f70_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanoblaster/0.16--h4ac6f70_6
$ module help quay.io/biocontainers/nanoblaster/0.16--h4ac6f70_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanoblaster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanoblaster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanoblaster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanoblaster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanoblaster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanoblaster-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nanoblaster

```bash
$ singularity exec <container> /usr/local/bin/nanoblaster
$ podman run --it --rm --entrypoint /usr/local/bin/nanoblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanoblaster   -v ${PWD} -w ${PWD} <container> -c " $@"
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