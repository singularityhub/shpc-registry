---
layout: container
name:  "quay.io/biocontainers/oncofuse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oncofuse/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/oncofuse/container.yaml"
updated_at: "2022-10-27 00:34:17.044966"
latest: "1.1.1--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/oncofuse"
aliases:
 - "oncofuse"
versions:
 - "1.1.1--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for oncofuse"
config: {"url": "https://biocontainers.pro/tools/oncofuse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for oncofuse", "latest": {"1.1.1--hdfd78af_2": "sha256:afe58c4910b875df010a3bc15f72584a724d736f4e3995949fdf442f85b4c5a7"}, "tags": {"1.1.1--hdfd78af_2": "sha256:afe58c4910b875df010a3bc15f72584a724d736f4e3995949fdf442f85b4c5a7"}, "docker": "quay.io/biocontainers/oncofuse", "aliases": {"oncofuse": "/usr/local/bin/oncofuse"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oncofuse.
shpc-registry automated BioContainers addition for oncofuse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oncofuse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oncofuse:1.1.1--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oncofuse/1.1.1--hdfd78af_2
$ module help quay.io/biocontainers/oncofuse/1.1.1--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oncofuse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oncofuse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oncofuse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oncofuse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oncofuse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oncofuse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### oncofuse

```bash
$ singularity exec <container> /usr/local/bin/oncofuse
$ podman run --it --rm --entrypoint /usr/local/bin/oncofuse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oncofuse   -v ${PWD} -w ${PWD} <container> -c " $@"
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