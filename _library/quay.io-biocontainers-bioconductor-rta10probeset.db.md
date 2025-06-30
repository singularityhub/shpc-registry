---
layout: container
name:  "quay.io/biocontainers/bioconductor-rta10probeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rta10probeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rta10probeset.db/container.yaml"
updated_at: "2025-06-30 05:08:51.304604"
latest: "8.8.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-rta10probeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
 - "8.8.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-rta10probeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rta10probeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rta10probeset.db", "latest": {"8.8.0--r44hdfd78af_5": "sha256:8d1edb56e304085ea2ee9fc87bab7a3ce4aa6bf489aceef0894dfa292a38b91f"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:16f5eb716e7ab6c58c8b1d960a04363511d08447a81afc18d261d39975c02d3a", "8.8.0--r42hdfd78af_2": "sha256:c906d6037036f81c2916e6be33a7617eaa705c43495de22a31061f9f960ec2ec", "8.8.0--r43hdfd78af_3": "sha256:18725f829eac38dfff2cd0cd362af186ce95f18c1f57011b57b94102dcb08c18", "8.8.0--r43hdfd78af_4": "sha256:28f5251977e6aaf109a93697a024428b5bb173f85143870bdd98a7e06773e0f2", "8.8.0--r44hdfd78af_5": "sha256:8d1edb56e304085ea2ee9fc87bab7a3ce4aa6bf489aceef0894dfa292a38b91f"}, "docker": "quay.io/biocontainers/bioconductor-rta10probeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rta10probeset.db.
shpc-registry automated BioContainers addition for bioconductor-rta10probeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rta10probeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rta10probeset.db:8.8.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rta10probeset.db/8.8.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-rta10probeset.db/8.8.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rta10probeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rta10probeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rta10probeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rta10probeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rta10probeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rta10probeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rta10probeset.db

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