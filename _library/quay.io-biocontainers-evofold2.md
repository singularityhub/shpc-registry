---
layout: container
name:  "quay.io/biocontainers/evofold2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/evofold2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/evofold2/container.yaml"
updated_at: "2023-02-08 03:08:19.712984"
latest: "0.1--h9ee0642_1"
container_url: "https://biocontainers.pro/tools/evofold2"
aliases:
 - "EvoFoldV2"
 - "EvoFoldV2.sh"
 - "dfgEval"
 - "dfgTrain"
 - "grammarTrain"
 - "multinomial"
versions:
 - "0.1--h9ee0642_1"
description: "shpc-registry automated BioContainers addition for evofold2"
config: {"url": "https://biocontainers.pro/tools/evofold2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for evofold2", "latest": {"0.1--h9ee0642_1": "sha256:e26b87878f6d9ba32d93148118a255b3a0a48f43361f875c54f2243f48485d6e"}, "tags": {"0.1--h9ee0642_1": "sha256:e26b87878f6d9ba32d93148118a255b3a0a48f43361f875c54f2243f48485d6e"}, "docker": "quay.io/biocontainers/evofold2", "aliases": {"EvoFoldV2": "/usr/local/bin/EvoFoldV2", "EvoFoldV2.sh": "/usr/local/bin/EvoFoldV2.sh", "dfgEval": "/usr/local/bin/dfgEval", "dfgTrain": "/usr/local/bin/dfgTrain", "grammarTrain": "/usr/local/bin/grammarTrain", "multinomial": "/usr/local/bin/multinomial"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/evofold2.
shpc-registry automated BioContainers addition for evofold2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/evofold2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/evofold2:0.1--h9ee0642_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/evofold2/0.1--h9ee0642_1
$ module help quay.io/biocontainers/evofold2/0.1--h9ee0642_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### evofold2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### evofold2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### evofold2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### evofold2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### evofold2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### evofold2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EvoFoldV2

```bash
$ singularity exec <container> /usr/local/bin/EvoFoldV2
$ podman run --it --rm --entrypoint /usr/local/bin/EvoFoldV2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EvoFoldV2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EvoFoldV2.sh

```bash
$ singularity exec <container> /usr/local/bin/EvoFoldV2.sh
$ podman run --it --rm --entrypoint /usr/local/bin/EvoFoldV2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EvoFoldV2.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dfgEval

```bash
$ singularity exec <container> /usr/local/bin/dfgEval
$ podman run --it --rm --entrypoint /usr/local/bin/dfgEval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfgEval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dfgTrain

```bash
$ singularity exec <container> /usr/local/bin/dfgTrain
$ podman run --it --rm --entrypoint /usr/local/bin/dfgTrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfgTrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grammarTrain

```bash
$ singularity exec <container> /usr/local/bin/grammarTrain
$ podman run --it --rm --entrypoint /usr/local/bin/grammarTrain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grammarTrain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multinomial

```bash
$ singularity exec <container> /usr/local/bin/multinomial
$ podman run --it --rm --entrypoint /usr/local/bin/multinomial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multinomial   -v ${PWD} -w ${PWD} <container> -c " $@"
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