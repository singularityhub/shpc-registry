---
layout: container
name:  "quay.io/biocontainers/flashlfq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/flashlfq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/flashlfq/container.yaml"
updated_at: "2023-10-23 02:59:36.760518"
latest: "1.2.4--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/flashlfq"
aliases:
 - "FlashLFQ"
 - "lttng-gen-tp"
versions:
 - "1.2.4--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for flashlfq"
config: {"url": "https://biocontainers.pro/tools/flashlfq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for flashlfq", "latest": {"1.2.4--hdfd78af_0": "sha256:d1654b13f30566096da690a28eae8e8e4f36394bb4b3cca4578c49adc4bad714"}, "tags": {"1.2.4--hdfd78af_0": "sha256:d1654b13f30566096da690a28eae8e8e4f36394bb4b3cca4578c49adc4bad714"}, "docker": "quay.io/biocontainers/flashlfq", "aliases": {"FlashLFQ": "/usr/local/bin/FlashLFQ", "lttng-gen-tp": "/usr/local/bin/lttng-gen-tp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/flashlfq.
shpc-registry automated BioContainers addition for flashlfq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/flashlfq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/flashlfq:1.2.4--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/flashlfq/1.2.4--hdfd78af_0
$ module help quay.io/biocontainers/flashlfq/1.2.4--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flashlfq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flashlfq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flashlfq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flashlfq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flashlfq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flashlfq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FlashLFQ

```bash
$ singularity exec <container> /usr/local/bin/FlashLFQ
$ podman run --it --rm --entrypoint /usr/local/bin/FlashLFQ   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FlashLFQ   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
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