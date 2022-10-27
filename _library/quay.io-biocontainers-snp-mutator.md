---
layout: container
name:  "quay.io/biocontainers/snp-mutator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snp-mutator/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/snp-mutator/container.yaml"
updated_at: "2022-10-27 01:15:38.345490"
latest: "1.2.0--pyh24bf2e0_0"
container_url: "https://biocontainers.pro/tools/snp-mutator"
aliases:
 - "snpmutator"
versions:
 - "1.2.0--pyh24bf2e0_0"
description: "shpc-registry automated BioContainers addition for snp-mutator"
config: {"url": "https://biocontainers.pro/tools/snp-mutator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snp-mutator", "latest": {"1.2.0--pyh24bf2e0_0": "sha256:feb43598e794c1723b3869f1719070bc6b8fc23df44574772123eaba8e7849cd"}, "tags": {"1.2.0--pyh24bf2e0_0": "sha256:feb43598e794c1723b3869f1719070bc6b8fc23df44574772123eaba8e7849cd"}, "docker": "quay.io/biocontainers/snp-mutator", "aliases": {"snpmutator": "/usr/local/bin/snpmutator"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snp-mutator.
shpc-registry automated BioContainers addition for snp-mutator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snp-mutator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snp-mutator:1.2.0--pyh24bf2e0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snp-mutator/1.2.0--pyh24bf2e0_0
$ module help quay.io/biocontainers/snp-mutator/1.2.0--pyh24bf2e0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snp-mutator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snp-mutator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snp-mutator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snp-mutator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snp-mutator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snp-mutator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### snpmutator

```bash
$ singularity exec <container> /usr/local/bin/snpmutator
$ podman run --it --rm --entrypoint /usr/local/bin/snpmutator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snpmutator   -v ${PWD} -w ${PWD} <container> -c " $@"
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