---
layout: container
name:  "quay.io/biocontainers/bioconductor-consensusclusterplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-consensusclusterplus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-consensusclusterplus/container.yaml"
updated_at: "2024-10-02 02:54:49.958115"
latest: "1.66.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-consensusclusterplus"

versions:
 - "1.58.0--r41hdfd78af_0"
 - "1.62.0--r42hdfd78af_0"
 - "1.64.0--r43hdfd78af_0"
 - "1.66.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-consensusclusterplus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-consensusclusterplus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-consensusclusterplus", "latest": {"1.66.0--r43hdfd78af_0": "sha256:2ad73134f915a1fe59cc002a8d28fdda2e439216df6ede0f1564f2758efc57f6"}, "tags": {"1.58.0--r41hdfd78af_0": "sha256:f161e7d7531d74d1995063c4e36b263731df611e2cada2fcd4fea11d7bf2ca5f", "1.62.0--r42hdfd78af_0": "sha256:acad947a7bbccfdd959d182bfe5c35cdda2d8e2c0f31f94dfd67ac1b28329d58", "1.64.0--r43hdfd78af_0": "sha256:89140f3042cabcc9c133ea97a75a2c01e12ec8debf0dadf6c488f8c68d6fbc3d", "1.66.0--r43hdfd78af_0": "sha256:2ad73134f915a1fe59cc002a8d28fdda2e439216df6ede0f1564f2758efc57f6"}, "docker": "quay.io/biocontainers/bioconductor-consensusclusterplus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-consensusclusterplus.
shpc-registry automated BioContainers addition for bioconductor-consensusclusterplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-consensusclusterplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-consensusclusterplus:1.66.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-consensusclusterplus/1.66.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-consensusclusterplus/1.66.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-consensusclusterplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-consensusclusterplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-consensusclusterplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-consensusclusterplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-consensusclusterplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-consensusclusterplus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-consensusclusterplus

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