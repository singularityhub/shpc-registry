---
layout: container
name:  "quay.io/biocontainers/intermine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/intermine/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/intermine/container.yaml"
updated_at: "2022-10-27 01:14:55.482051"
latest: "1.13.0--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/intermine"

versions:
 - "1.13.0--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for intermine"
config: {"url": "https://biocontainers.pro/tools/intermine", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for intermine", "latest": {"1.13.0--pyh5e36f6f_0": "sha256:dbe2dcbf1dd3dceb285a7b6db13acc7db15dbc2fb88fae0c8a89c5934452d599"}, "tags": {"1.13.0--pyh5e36f6f_0": "sha256:dbe2dcbf1dd3dceb285a7b6db13acc7db15dbc2fb88fae0c8a89c5934452d599"}, "docker": "quay.io/biocontainers/intermine"}
---

This module is a singularity container wrapper for quay.io/biocontainers/intermine.
shpc-registry automated BioContainers addition for intermine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/intermine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/intermine:1.13.0--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/intermine/1.13.0--pyh5e36f6f_0
$ module help quay.io/biocontainers/intermine/1.13.0--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### intermine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### intermine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### intermine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### intermine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### intermine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### intermine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### intermine

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