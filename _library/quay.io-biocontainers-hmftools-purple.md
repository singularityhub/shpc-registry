---
layout: container
name:  "quay.io/biocontainers/hmftools-purple"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-purple/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-purple/container.yaml"
updated_at: "2022-10-27 01:10:19.296913"
latest: "3.6--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hmftools-purple"
aliases:
 - "PURPLE"
versions:
 - "3.6--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for hmftools-purple"
config: {"url": "https://biocontainers.pro/tools/hmftools-purple", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmftools-purple", "latest": {"3.6--hdfd78af_0": "sha256:677d1b3509a70b16dd502a7cc44302c9e8282de9371f6af07c41ec2f7d7269fb"}, "tags": {"3.6--hdfd78af_0": "sha256:677d1b3509a70b16dd502a7cc44302c9e8282de9371f6af07c41ec2f7d7269fb"}, "docker": "quay.io/biocontainers/hmftools-purple", "aliases": {"PURPLE": "/usr/local/bin/PURPLE"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-purple.
shpc-registry automated BioContainers addition for hmftools-purple
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-purple
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-purple:3.6--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-purple/3.6--hdfd78af_0
$ module help quay.io/biocontainers/hmftools-purple/3.6--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-purple-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-purple-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-purple-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-purple-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-purple-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-purple-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PURPLE

```bash
$ singularity exec <container> /usr/local/bin/PURPLE
$ podman run --it --rm --entrypoint /usr/local/bin/PURPLE   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PURPLE   -v ${PWD} -w ${PWD} <container> -c " $@"
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