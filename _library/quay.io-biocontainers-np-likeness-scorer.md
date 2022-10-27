---
layout: container
name:  "quay.io/biocontainers/np-likeness-scorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/np-likeness-scorer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/np-likeness-scorer/container.yaml"
updated_at: "2022-10-27 00:43:00.679092"
latest: "2.1--py35_0"
container_url: "https://biocontainers.pro/tools/np-likeness-scorer"
aliases:
 - "np-likeness"
versions:
 - "2.1--py35_0"
description: "shpc-registry automated BioContainers addition for np-likeness-scorer"
config: {"url": "https://biocontainers.pro/tools/np-likeness-scorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for np-likeness-scorer", "latest": {"2.1--py35_0": "sha256:5f763c7077a033626c390ab3f33efbf6f43c28170bb87e8fc7ab052bb69f8a5d"}, "tags": {"2.1--py35_0": "sha256:5f763c7077a033626c390ab3f33efbf6f43c28170bb87e8fc7ab052bb69f8a5d"}, "docker": "quay.io/biocontainers/np-likeness-scorer", "aliases": {"np-likeness": "/usr/local/bin/np-likeness"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/np-likeness-scorer.
shpc-registry automated BioContainers addition for np-likeness-scorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/np-likeness-scorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/np-likeness-scorer:2.1--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/np-likeness-scorer/2.1--py35_0
$ module help quay.io/biocontainers/np-likeness-scorer/2.1--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### np-likeness-scorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### np-likeness-scorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### np-likeness-scorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### np-likeness-scorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### np-likeness-scorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### np-likeness-scorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### np-likeness

```bash
$ singularity exec <container> /usr/local/bin/np-likeness
$ podman run --it --rm --entrypoint /usr/local/bin/np-likeness   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/np-likeness   -v ${PWD} -w ${PWD} <container> -c " $@"
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