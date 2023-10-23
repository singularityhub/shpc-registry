---
layout: container
name:  "quay.io/biocontainers/bioconductor-huex10stprobeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-huex10stprobeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-huex10stprobeset.db/container.yaml"
updated_at: "2023-10-23 03:28:18.312442"
latest: "8.8.0--r43hdfd78af_3"
container_url: "https://biocontainers.pro/tools/bioconductor-huex10stprobeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
description: "shpc-registry automated BioContainers addition for bioconductor-huex10stprobeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-huex10stprobeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-huex10stprobeset.db", "latest": {"8.8.0--r43hdfd78af_3": "sha256:48736c82c20e1e99a1fcb1a3ea9fef6e41c3965cf071115b31300c16f2add3ca"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:ec416066ab85c4fdf9050682d6d5c36ccb5e3ca7561b14e52a85e30593bbc497", "8.8.0--r42hdfd78af_2": "sha256:cda189b58e13193398df2b5d231ab0734cfbe04a179684fa53d769e9c014bd1c", "8.8.0--r43hdfd78af_3": "sha256:48736c82c20e1e99a1fcb1a3ea9fef6e41c3965cf071115b31300c16f2add3ca"}, "docker": "quay.io/biocontainers/bioconductor-huex10stprobeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-huex10stprobeset.db.
shpc-registry automated BioContainers addition for bioconductor-huex10stprobeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-huex10stprobeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-huex10stprobeset.db:8.8.0--r43hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-huex10stprobeset.db/8.8.0--r43hdfd78af_3
$ module help quay.io/biocontainers/bioconductor-huex10stprobeset.db/8.8.0--r43hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-huex10stprobeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huex10stprobeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huex10stprobeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-huex10stprobeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-huex10stprobeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-huex10stprobeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-huex10stprobeset.db

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