---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgug4131a.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgug4131a.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgug4131a.db/container.yaml"
updated_at: "2026-01-07 04:19:48.858769"
latest: "3.2.3--r44hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-rgug4131a.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r43hdfd78af_13"
 - "3.2.3--r44hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-rgug4131a.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgug4131a.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgug4131a.db", "latest": {"3.2.3--r44hdfd78af_14": "sha256:21d7486ef7d934aa89a17ed636518537513ac30e8e37365a098e40de74187980"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:ea63902d6168f87f412ff10818bcb4adeb00e7c0a5a39c4cee94506f06db7873", "3.2.3--r42hdfd78af_11": "sha256:8015d2ed37e09de3288ac120c8ce34a9d64dae7cc1976c23ed7ebb2521401457", "3.2.3--r43hdfd78af_12": "sha256:1adb8ec79e91f3ab5e44ce7edb695623504c552684b461e752b430136085f52b", "3.2.3--r43hdfd78af_13": "sha256:85f83b0cb79ff9b87d8723788826c800952297862d12b56e94e608c52d1fbe97", "3.2.3--r44hdfd78af_14": "sha256:21d7486ef7d934aa89a17ed636518537513ac30e8e37365a098e40de74187980"}, "docker": "quay.io/biocontainers/bioconductor-rgug4131a.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgug4131a.db.
shpc-registry automated BioContainers addition for bioconductor-rgug4131a.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgug4131a.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgug4131a.db:3.2.3--r44hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgug4131a.db/3.2.3--r44hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-rgug4131a.db/3.2.3--r44hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgug4131a.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgug4131a.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgug4131a.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgug4131a.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgug4131a.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgug4131a.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgug4131a.db

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