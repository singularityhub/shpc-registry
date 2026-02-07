---
layout: container
name:  "quay.io/biocontainers/bioconductor-nanostringdiff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nanostringdiff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nanostringdiff/container.yaml"
updated_at: "2026-02-07 04:19:50.134112"
latest: "1.36.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nanostringdiff"

versions:
 - "1.24.0--r41hc247a5b_2"
 - "1.28.0--r42hc247a5b_0"
 - "1.28.0--r42hf17093f_1"
 - "1.30.0--r43hf17093f_0"
 - "1.32.0--r43hf17093f_0"
 - "1.36.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nanostringdiff"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nanostringdiff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nanostringdiff", "latest": {"1.36.0--r44he5774e6_0": "sha256:7e40ae26221564b0f8306ac350341ae1b9f6eec8e3ae94ea453ee74c543826e7"}, "tags": {"1.24.0--r41hc247a5b_2": "sha256:f2e04df5ab17a77c962d45b15a4e05ae345857a80cf6ce031a4241a67e3eba07", "1.28.0--r42hc247a5b_0": "sha256:45114bce0d51887391daa34cd9685f2410ca7b11e5f0d170749fb3a7700832ed", "1.28.0--r42hf17093f_1": "sha256:cecb57f449153187d5c28154b7ef53589ee0df9c26edda6d83253deee58f1867", "1.30.0--r43hf17093f_0": "sha256:4aa5d06776d4632e37635e094e4e5b3eee23dbbef24967a20f85b00b3c7d08b7", "1.32.0--r43hf17093f_0": "sha256:e37d608598c027271bbb37a03ed625681ce24dde22e9a5743104dd38c4f873c3", "1.36.0--r44he5774e6_0": "sha256:7e40ae26221564b0f8306ac350341ae1b9f6eec8e3ae94ea453ee74c543826e7"}, "docker": "quay.io/biocontainers/bioconductor-nanostringdiff"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nanostringdiff.
shpc-registry automated BioContainers addition for bioconductor-nanostringdiff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nanostringdiff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nanostringdiff:1.36.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nanostringdiff/1.36.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-nanostringdiff/1.36.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nanostringdiff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanostringdiff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanostringdiff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nanostringdiff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nanostringdiff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nanostringdiff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nanostringdiff

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