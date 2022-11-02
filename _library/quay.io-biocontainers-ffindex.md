---
layout: container
name:  "quay.io/biocontainers/ffindex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ffindex/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ffindex/container.yaml"
updated_at: "2022-11-02 19:04:22.251524"
latest: "0.98--h9f5acd7_2"
container_url: "https://biocontainers.pro/tools/ffindex"

versions:
 - "0.98--h9f5acd7_2"
description: "shpc-registry automated BioContainers addition for ffindex"
config: {"url": "https://biocontainers.pro/tools/ffindex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ffindex", "latest": {"0.98--h9f5acd7_2": "sha256:b3c72a2816aa3af70d8b60844daf0acebff71a8899ff8c591038cf1d3ceb47c4"}, "tags": {"0.98--h9f5acd7_2": "sha256:b3c72a2816aa3af70d8b60844daf0acebff71a8899ff8c591038cf1d3ceb47c4"}, "docker": "quay.io/biocontainers/ffindex"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ffindex.
shpc-registry automated BioContainers addition for ffindex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ffindex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ffindex:0.98--h9f5acd7_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ffindex/0.98--h9f5acd7_2
$ module help quay.io/biocontainers/ffindex/0.98--h9f5acd7_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ffindex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ffindex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ffindex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ffindex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ffindex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ffindex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ffindex

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