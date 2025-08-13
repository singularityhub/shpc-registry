---
layout: container
name:  "quay.io/biocontainers/bioconductor-lumiratall.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lumiratall.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lumiratall.db/container.yaml"
updated_at: "2025-08-13 03:50:03.261862"
latest: "1.22.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-lumiratall.db"

versions:
 - "1.22.0--r41hdfd78af_9"
 - "1.22.0--r42hdfd78af_10"
 - "1.22.0--r43hdfd78af_11"
 - "1.22.0--r43hdfd78af_12"
 - "1.22.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-lumiratall.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lumiratall.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lumiratall.db", "latest": {"1.22.0--r44hdfd78af_13": "sha256:c226e6113c1eefa67983f70e90478d590df24315b309cc32108838d535db85e6"}, "tags": {"1.22.0--r41hdfd78af_9": "sha256:075ea54a967e0281f167808240ffe6aa8789b7a10e56db8b807d42adcf51e2be", "1.22.0--r42hdfd78af_10": "sha256:87d7c05c556e10057645b93809dc7047f5c456dd5e7b2c05b1c65d655343ad38", "1.22.0--r43hdfd78af_11": "sha256:33f30423a7270b4f2bed50b0539bdab8f1b3c7ae6f4ed0b789c70bf08c0adf68", "1.22.0--r43hdfd78af_12": "sha256:3afedfd1cfd80aa7653f55da922d897e7cbea4d0f82c64ccec98eb375b98a39b", "1.22.0--r44hdfd78af_13": "sha256:c226e6113c1eefa67983f70e90478d590df24315b309cc32108838d535db85e6"}, "docker": "quay.io/biocontainers/bioconductor-lumiratall.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lumiratall.db.
shpc-registry automated BioContainers addition for bioconductor-lumiratall.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lumiratall.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lumiratall.db:1.22.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lumiratall.db/1.22.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-lumiratall.db/1.22.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lumiratall.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumiratall.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lumiratall.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lumiratall.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lumiratall.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lumiratall.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lumiratall.db

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