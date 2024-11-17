---
layout: container
name:  "quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq/container.yaml"
updated_at: "2024-11-17 03:21:05.548724"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-highlyreplicatedrnaseq"

versions:
 - "1.6.0--r41hdfd78af_1"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-highlyreplicatedrnaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-highlyreplicatedrnaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-highlyreplicatedrnaseq", "latest": {"1.14.0--r43hdfd78af_0": "sha256:b9a38093a2cfdf057c5542033d472f3060a51d21b2f8c9330658d40523495342"}, "tags": {"1.6.0--r41hdfd78af_1": "sha256:f03fcb94608134d2ec0df151879bafb60eaa6078418b3265bafb6b2819cbb35b", "1.10.0--r42hdfd78af_0": "sha256:89234c675b7ecd0cc3484a45166912cfa79a3a99b690211c8c0eedbf4971596c", "1.12.0--r43hdfd78af_0": "sha256:651b20f1a57d4b78cff7703f3ace8d02cd971896154c6f1a17d16faabce24218", "1.14.0--r43hdfd78af_0": "sha256:b9a38093a2cfdf057c5542033d472f3060a51d21b2f8c9330658d40523495342"}, "docker": "quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq.
shpc-registry automated BioContainers addition for bioconductor-highlyreplicatedrnaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-highlyreplicatedrnaseq/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-highlyreplicatedrnaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-highlyreplicatedrnaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-highlyreplicatedrnaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-highlyreplicatedrnaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-highlyreplicatedrnaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-highlyreplicatedrnaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-highlyreplicatedrnaseq

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