---
layout: container
name:  "quay.io/biocontainers/kggseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kggseq/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/kggseq/container.yaml"
updated_at: "2022-10-27 00:44:43.209413"
latest: "1.1--0"
container_url: "https://biocontainers.pro/tools/kggseq"
aliases:
 - ".kggseq-post-link.sh"
 - "kggseq"
 - "kggseq1.log"
versions:
 - "1.1--0"
description: "shpc-registry automated BioContainers addition for kggseq"
config: {"url": "https://biocontainers.pro/tools/kggseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kggseq", "latest": {"1.1--0": "sha256:0a3721e17acd293a6268bd24c7e6befb74a63f8602cef1e25013307629c34b42"}, "tags": {"1.1--0": "sha256:0a3721e17acd293a6268bd24c7e6befb74a63f8602cef1e25013307629c34b42"}, "docker": "quay.io/biocontainers/kggseq", "aliases": {".kggseq-post-link.sh": "/usr/local/bin/.kggseq-post-link.sh", "kggseq": "/usr/local/bin/kggseq", "kggseq1.log": "/usr/local/bin/kggseq1.log"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kggseq.
shpc-registry automated BioContainers addition for kggseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kggseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kggseq:1.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kggseq/1.1--0
$ module help quay.io/biocontainers/kggseq/1.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kggseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kggseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kggseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kggseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kggseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kggseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .kggseq-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.kggseq-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.kggseq-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.kggseq-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kggseq

```bash
$ singularity exec <container> /usr/local/bin/kggseq
$ podman run --it --rm --entrypoint /usr/local/bin/kggseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kggseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kggseq1.log

```bash
$ singularity exec <container> /usr/local/bin/kggseq1.log
$ podman run --it --rm --entrypoint /usr/local/bin/kggseq1.log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kggseq1.log   -v ${PWD} -w ${PWD} <container> -c " $@"
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