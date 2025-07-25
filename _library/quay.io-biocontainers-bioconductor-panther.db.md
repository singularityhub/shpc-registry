---
layout: container
name:  "quay.io/biocontainers/bioconductor-panther.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-panther.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-panther.db/container.yaml"
updated_at: "2025-07-25 03:49:20.546206"
latest: "1.0.12--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-panther.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.0.5--r36_0"
 - "1.0.11--r41hdfd78af_2"
 - "1.0.11--r42hdfd78af_3"
 - "1.0.11--r43hdfd78af_4"
 - "1.0.12--r43hdfd78af_0"
 - "1.0.12--r44hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-panther.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-panther.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-panther.db", "latest": {"1.0.12--r44hdfd78af_1": "sha256:9e91a9b431744418bb22a5ffb3d7e63167027581c87f18c9a4852e316885ec22"}, "tags": {"1.0.5--r36_0": "sha256:ed71e31c064fbfb86fcd29b798dda7f106dc6fdd3f8a1aa0cd0b23d94770e79f", "1.0.11--r41hdfd78af_2": "sha256:bea660b93ff92277267d81d21897cff57b876df0ff8ebd7e12024e5df24e478d", "1.0.11--r42hdfd78af_3": "sha256:2d04a2e79a6faba0c8007e74e05945e492e5f5d0dac550ce3bc6768741c4dc1e", "1.0.11--r43hdfd78af_4": "sha256:fcd444a4f81515ed8aded1a47e0a6ca48ace5e8589b014dd3ff5e1567968ece4", "1.0.12--r43hdfd78af_0": "sha256:1ba657c6ae46435ab8e298c5b832db043bcac42cf457195a6519aa804ca90071", "1.0.12--r44hdfd78af_1": "sha256:9e91a9b431744418bb22a5ffb3d7e63167027581c87f18c9a4852e316885ec22"}, "docker": "quay.io/biocontainers/bioconductor-panther.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-panther.db.
shpc-registry automated BioContainers addition for bioconductor-panther.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-panther.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-panther.db:1.0.12--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-panther.db/1.0.12--r44hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-panther.db/1.0.12--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-panther.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panther.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-panther.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-panther.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-panther.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-panther.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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