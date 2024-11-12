---
layout: container
name:  "quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db/container.yaml"
updated_at: "2024-11-12 03:24:55.014017"
latest: "8.8.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-clariomdhumanprobeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-clariomdhumanprobeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clariomdhumanprobeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clariomdhumanprobeset.db", "latest": {"8.8.0--r43hdfd78af_4": "sha256:b2b814e2a26e0d1e8b91e54bb190c4b41caa5511a0e24a68dc263eaf678203b2"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:d47880b8f643a2874c3c08e624c3f26dcdcc3d7a2da206edc55cb83d1149e746", "8.8.0--r42hdfd78af_2": "sha256:336f059a64768bc7c64ff411ea90ee61a6e68e98e399716e3fc707bcc99eb91f", "8.8.0--r43hdfd78af_3": "sha256:64178eeaeda44f78a3a33b8de17bc333f1320c59582eec3faed8cbbb251c77fc", "8.8.0--r43hdfd78af_4": "sha256:b2b814e2a26e0d1e8b91e54bb190c4b41caa5511a0e24a68dc263eaf678203b2"}, "docker": "quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db.
shpc-registry automated BioContainers addition for bioconductor-clariomdhumanprobeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db:8.8.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db/8.8.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-clariomdhumanprobeset.db/8.8.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clariomdhumanprobeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clariomdhumanprobeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clariomdhumanprobeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clariomdhumanprobeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clariomdhumanprobeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clariomdhumanprobeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clariomdhumanprobeset.db

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