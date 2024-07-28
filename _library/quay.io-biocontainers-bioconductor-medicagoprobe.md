---
layout: container
name:  "quay.io/biocontainers/bioconductor-medicagoprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-medicagoprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-medicagoprobe/container.yaml"
updated_at: "2024-07-28 03:23:44.958678"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-medicagoprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-medicagoprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-medicagoprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-medicagoprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:ae495d10709da925ab24d22c656fadccc53d38093d417856b6333ca393589620"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:d6e144fa9e68d28161f45e181d73547dfe863c340983b8906b9322d36e844078", "2.18.0--r42hdfd78af_10": "sha256:24be6aa5f312fc8473be65e0d8d9586824a17b36759290e95f1c49a5ef583bdd", "2.18.0--r43hdfd78af_11": "sha256:0a6230d52d138bac61f5c39cb18f016fd3e64960eeca3a6dd9d880b8e1799a84", "2.18.0--r43hdfd78af_12": "sha256:ae495d10709da925ab24d22c656fadccc53d38093d417856b6333ca393589620"}, "docker": "quay.io/biocontainers/bioconductor-medicagoprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-medicagoprobe.
shpc-registry automated BioContainers addition for bioconductor-medicagoprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-medicagoprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-medicagoprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-medicagoprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-medicagoprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-medicagoprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-medicagoprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-medicagoprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-medicagoprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-medicagoprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-medicagoprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-medicagoprobe

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