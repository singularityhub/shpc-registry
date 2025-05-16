---
layout: container
name:  "quay.io/biocontainers/bioconductor-h10kcod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-h10kcod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-h10kcod.db/container.yaml"
updated_at: "2025-05-16 03:30:06.520665"
latest: "3.4.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-h10kcod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
 - "3.4.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-h10kcod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-h10kcod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-h10kcod.db", "latest": {"3.4.0--r44hdfd78af_13": "sha256:9a74f4d93382d1fe8750c7fd74aa6afc2b99403491b52c930c78901a74688dd6"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:0cba5e59ed71c99dacf727da82f898548f06c1799c8b2d8eb79e793301ad1892", "3.4.0--r42hdfd78af_10": "sha256:066b8281eff584eec6136bc962771a4a66d82d66f9c3a98bf4c6ef8a4c5ee09a", "3.4.0--r43hdfd78af_11": "sha256:a86efbab0266a05462724d159de64ec378677ca4110b336ca697061b8dbbbf4a", "3.4.0--r43hdfd78af_12": "sha256:3c003540f623b75c2885a555392f0ba102829b10ebc518ebd8fa4eb95c951cd4", "3.4.0--r44hdfd78af_13": "sha256:9a74f4d93382d1fe8750c7fd74aa6afc2b99403491b52c930c78901a74688dd6"}, "docker": "quay.io/biocontainers/bioconductor-h10kcod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-h10kcod.db.
shpc-registry automated BioContainers addition for bioconductor-h10kcod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-h10kcod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-h10kcod.db:3.4.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-h10kcod.db/3.4.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-h10kcod.db/3.4.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-h10kcod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-h10kcod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-h10kcod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-h10kcod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-h10kcod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-h10kcod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-h10kcod.db

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