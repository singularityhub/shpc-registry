---
layout: container
name:  "quay.io/biocontainers/ibdne"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ibdne/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ibdne/container.yaml"
updated_at: "2022-10-27 00:58:36.677283"
latest: "04Sep15.e78--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/ibdne"
aliases:
 - "ibdne"
versions:
 - "04Sep15.e78--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for ibdne"
config: {"url": "https://biocontainers.pro/tools/ibdne", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ibdne", "latest": {"04Sep15.e78--hdfd78af_3": "sha256:e6e061f0957777272293444a6cf690733b88ec3d694afd87c0ff3b1c032b065a"}, "tags": {"04Sep15.e78--hdfd78af_3": "sha256:e6e061f0957777272293444a6cf690733b88ec3d694afd87c0ff3b1c032b065a"}, "docker": "quay.io/biocontainers/ibdne", "aliases": {"ibdne": "/usr/local/bin/ibdne"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ibdne.
shpc-registry automated BioContainers addition for ibdne
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ibdne
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ibdne:04Sep15.e78--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ibdne/04Sep15.e78--hdfd78af_3
$ module help quay.io/biocontainers/ibdne/04Sep15.e78--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ibdne-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ibdne-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ibdne-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ibdne-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ibdne-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ibdne-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ibdne

```bash
$ singularity exec <container> /usr/local/bin/ibdne
$ podman run --it --rm --entrypoint /usr/local/bin/ibdne   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibdne   -v ${PWD} -w ${PWD} <container> -c " $@"
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