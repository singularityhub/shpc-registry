---
layout: container
name:  "quay.io/biocontainers/plink2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/plink2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/plink2/container.yaml"
updated_at: "2024-06-27 03:21:04.188281"
latest: "2.00a5.10--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/plink2"
aliases:
 - "plink2"
versions:
 - "2.00a3.3--hb2a7ceb_0"
 - "2.00a3.7--h9f5acd7_2"
 - "2.00a3.7--h4ac6f70_4"
 - "2.00a5--h4ac6f70_0"
 - "2.00a5.10--h4ac6f70_0"
description: "shpc-registry automated BioContainers addition for plink2"
config: {"url": "https://biocontainers.pro/tools/plink2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for plink2", "latest": {"2.00a5.10--h4ac6f70_0": "sha256:1f18b260c8f43ff7b057cdda2ead9e4063facf10242bf3daf73a0d4cc9f3ce0c"}, "tags": {"2.00a3.3--hb2a7ceb_0": "sha256:dfa04a7b5b5ec23ca8e2e3af6aebd322428ca7c6898546b6e10b9ad841413dd5", "2.00a3.7--h9f5acd7_2": "sha256:2944b344c7086659f455bc129eafadf33488e6d9ec1b3ec4e1b58e62ce6f34ee", "2.00a3.7--h4ac6f70_4": "sha256:ad1ddb113bc0b13ae6ac9853a0100d61f7e8264591053abbcb386e2668e7c76d", "2.00a5--h4ac6f70_0": "sha256:ca289a4c97a153ae60c6702f1a0583f6351d94bb2b60548412ed7043d16d8bb9", "2.00a5.10--h4ac6f70_0": "sha256:1f18b260c8f43ff7b057cdda2ead9e4063facf10242bf3daf73a0d4cc9f3ce0c"}, "docker": "quay.io/biocontainers/plink2", "aliases": {"plink2": "/usr/local/bin/plink2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/plink2.
shpc-registry automated BioContainers addition for plink2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/plink2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/plink2:2.00a5.10--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/plink2/2.00a5.10--h4ac6f70_0
$ module help quay.io/biocontainers/plink2/2.00a5.10--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### plink2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### plink2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### plink2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### plink2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### plink2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### plink2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### plink2

```bash
$ singularity exec <container> /usr/local/bin/plink2
$ podman run --it --rm --entrypoint /usr/local/bin/plink2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plink2   -v ${PWD} -w ${PWD} <container> -c " $@"
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