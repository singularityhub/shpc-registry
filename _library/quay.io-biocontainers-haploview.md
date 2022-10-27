---
layout: container
name:  "quay.io/biocontainers/haploview"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haploview/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/haploview/container.yaml"
updated_at: "2022-10-27 00:20:43.659878"
latest: "4.2--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/haploview"
aliases:
 - "haploview"
versions:
 - "4.2--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for haploview"
config: {"url": "https://biocontainers.pro/tools/haploview", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haploview", "latest": {"4.2--hdfd78af_1": "sha256:d81696bf7d9b67a034f25b4a053d8b963a1727bb66874f8c66ca91851f65cb68"}, "tags": {"4.2--hdfd78af_1": "sha256:d81696bf7d9b67a034f25b4a053d8b963a1727bb66874f8c66ca91851f65cb68"}, "docker": "quay.io/biocontainers/haploview", "aliases": {"haploview": "/usr/local/bin/haploview"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haploview.
shpc-registry automated BioContainers addition for haploview
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haploview
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haploview:4.2--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haploview/4.2--hdfd78af_1
$ module help quay.io/biocontainers/haploview/4.2--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haploview-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haploview-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haploview-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haploview-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haploview-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haploview-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### haploview

```bash
$ singularity exec <container> /usr/local/bin/haploview
$ podman run --it --rm --entrypoint /usr/local/bin/haploview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haploview   -v ${PWD} -w ${PWD} <container> -c " $@"
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