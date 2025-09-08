---
layout: container
name:  "quay.io/biocontainers/bioconductor-msbackendmassbank"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msbackendmassbank/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msbackendmassbank/container.yaml"
updated_at: "2025-09-08 03:47:58.557039"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msbackendmassbank"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.1--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msbackendmassbank"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msbackendmassbank", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msbackendmassbank", "latest": {"1.14.0--r44hdfd78af_0": "sha256:3b967b5cef6bd23bac2f8cecbe638036d1285bc89fa48c96988122818ad5d1d7"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:a08b8b8c688399637c028c21334e4d768a4bbf7f2f369775c2ee43e71a8586b7", "1.6.0--r42hdfd78af_0": "sha256:c5c75ac90118d83fa0e9b1e4ee1d48169014033ca6ec4a25273a2daca0d178a4", "1.8.0--r43hdfd78af_0": "sha256:a4e7a8ad5e43c482a46d12221b48cbceca7e9a9e4281ccfa5f66333e7fa24b3e", "1.10.1--r43hdfd78af_0": "sha256:c1b6e9c56c3040fee1200084a07b9847387248f93c7e9657678cff559fc91fca", "1.14.0--r44hdfd78af_0": "sha256:3b967b5cef6bd23bac2f8cecbe638036d1285bc89fa48c96988122818ad5d1d7"}, "docker": "quay.io/biocontainers/bioconductor-msbackendmassbank"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msbackendmassbank.
shpc-registry automated BioContainers addition for bioconductor-msbackendmassbank
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msbackendmassbank
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msbackendmassbank:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msbackendmassbank/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msbackendmassbank/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msbackendmassbank-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msbackendmassbank-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msbackendmassbank-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msbackendmassbank-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msbackendmassbank-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msbackendmassbank-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-msbackendmassbank

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