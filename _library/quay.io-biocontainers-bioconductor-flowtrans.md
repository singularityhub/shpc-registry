---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowtrans"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowtrans/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowtrans/container.yaml"
updated_at: "2025-03-25 03:45:30.395794"
latest: "1.58.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowtrans"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.58.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowtrans"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowtrans", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowtrans", "latest": {"1.58.0--r44hdfd78af_0": "sha256:72a005e84211589377b02fa66caacccc547dfe147f140e0625f26f5c7a0baff0"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:e3e7bfda0a64510477fefbcb45b8ad64d5391f15965a13c3063b17233aaa67f3", "1.50.0--r42hdfd78af_0": "sha256:ae5962cdcb39add6014f716b37b115679504d0049e84bab2643a64351ff70589", "1.52.0--r43hdfd78af_0": "sha256:74b31edc30f03434088eefe9edd693e866519d070411334fc903af358c0c4712", "1.54.0--r43hdfd78af_0": "sha256:864212626a322249f628fa90db13ff1b393190ae77463ce7780545345b7a906c", "1.58.0--r44hdfd78af_0": "sha256:72a005e84211589377b02fa66caacccc547dfe147f140e0625f26f5c7a0baff0"}, "docker": "quay.io/biocontainers/bioconductor-flowtrans"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowtrans.
shpc-registry automated BioContainers addition for bioconductor-flowtrans
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowtrans
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowtrans:1.58.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowtrans/1.58.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowtrans/1.58.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowtrans-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowtrans-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowtrans-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowtrans-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowtrans-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowtrans-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowtrans

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