---
layout: container
name:  "quay.io/biocontainers/ericscript"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ericscript/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ericscript/container.yaml"
updated_at: "2022-10-27 00:46:57.472461"
latest: "0.5.5--hdfd78af_5"
container_url: "https://biocontainers.pro/tools/ericscript"
aliases:
 - "ericscript.pl"
versions:
 - "0.5.5--hdfd78af_5"
description: "shpc-registry automated BioContainers addition for ericscript"
config: {"url": "https://biocontainers.pro/tools/ericscript", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ericscript", "latest": {"0.5.5--hdfd78af_5": "sha256:d6c08e44e06a25c5dcca541b33adfd5297ccc3ef657b2b0fd437760865fdd1f5"}, "tags": {"0.5.5--hdfd78af_5": "sha256:d6c08e44e06a25c5dcca541b33adfd5297ccc3ef657b2b0fd437760865fdd1f5"}, "docker": "quay.io/biocontainers/ericscript", "aliases": {"ericscript.pl": "/usr/local/bin/ericscript.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ericscript.
shpc-registry automated BioContainers addition for ericscript
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ericscript
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ericscript:0.5.5--hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ericscript/0.5.5--hdfd78af_5
$ module help quay.io/biocontainers/ericscript/0.5.5--hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ericscript-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ericscript-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ericscript-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ericscript-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ericscript-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ericscript-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ericscript.pl

```bash
$ singularity exec <container> /usr/local/bin/ericscript.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ericscript.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ericscript.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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