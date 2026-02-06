---
layout: container
name:  "quay.io/biocontainers/raptor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/raptor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/raptor/container.yaml"
updated_at: "2026-02-06 04:42:00.546682"
latest: "3.0.1--haf24da9_4"
container_url: "https://biocontainers.pro/tools/raptor"
aliases:
 - "raptor"
versions:
 - "2.0.0--h19e8d03_1"
 - "2.0.0--h6dccd9a_3"
 - "3.0.0--h6dccd9a_1"
 - "3.0.1--h6dccd9a_0"
 - "3.0.1--h6dccd9a_2"
 - "3.0.1--haf24da9_3"
 - "3.0.1--haf24da9_4"
description: "shpc-registry automated BioContainers addition for raptor"
config: {"url": "https://biocontainers.pro/tools/raptor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for raptor", "latest": {"3.0.1--haf24da9_4": "sha256:133e567afdbfa9e46e4d9582bd08e48814ad56e6fde33aec3704c2e063008713"}, "tags": {"2.0.0--h19e8d03_1": "sha256:86149b282f2927d0ab258d8b5e4cf82113ed965ec05bb3c5c0af7053dc20cf3b", "2.0.0--h6dccd9a_3": "sha256:dcac76e9ec14c71e01114703a02862ba2d961f12cc9c34627b467d5ba6971497", "3.0.0--h6dccd9a_1": "sha256:493705141705795dd4d104f9809dd92b5156034a61690036ff90aa991a555e8d", "3.0.1--h6dccd9a_0": "sha256:51617c16f91b9716f00ea13d22dd35b4a75640dd0d3c02105f833ef561544100", "3.0.1--h6dccd9a_2": "sha256:5d6e99baee658d82e195fa0b2279af260a282c2f9e0502d52d157a111d3b7a91", "3.0.1--haf24da9_3": "sha256:55d2720de27f7174d32e4dbea5a61795f6309353ac1747d96834ea2839b364dc", "3.0.1--haf24da9_4": "sha256:133e567afdbfa9e46e4d9582bd08e48814ad56e6fde33aec3704c2e063008713"}, "docker": "quay.io/biocontainers/raptor", "aliases": {"raptor": "/usr/local/bin/raptor"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/raptor.
shpc-registry automated BioContainers addition for raptor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/raptor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/raptor:3.0.1--haf24da9_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/raptor/3.0.1--haf24da9_4
$ module help quay.io/biocontainers/raptor/3.0.1--haf24da9_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### raptor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### raptor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### raptor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### raptor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### raptor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### raptor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### raptor

```bash
$ singularity exec <container> /usr/local/bin/raptor
$ podman run --it --rm --entrypoint /usr/local/bin/raptor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raptor   -v ${PWD} -w ${PWD} <container> -c " $@"
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