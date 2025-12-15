---
layout: container
name:  "quay.io/biocontainers/bioconductor-raex10stprobeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-raex10stprobeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-raex10stprobeset.db/container.yaml"
updated_at: "2025-12-15 04:22:41.991259"
latest: "8.8.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-raex10stprobeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
 - "8.8.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-raex10stprobeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-raex10stprobeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-raex10stprobeset.db", "latest": {"8.8.0--r44hdfd78af_5": "sha256:351552e047586c4eac39273c73ad6c9823c30b580ed6573afd08993a04445ba0"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:deaa23172e8e069fcbd1ce35643f822183ed02543fbfab9c0c9b959c7c0a5f53", "8.8.0--r42hdfd78af_2": "sha256:db99fba02f227d8af739d4d860891afd2b4859bbfbd9ea0debdbb42dfdfb37cd", "8.8.0--r43hdfd78af_3": "sha256:dea52caf84c82d980597e7ea5eeabb35de75d49e64ba9e1b9bf73e9d8b82c073", "8.8.0--r43hdfd78af_4": "sha256:7599f288d32e6e20799e1b029dd8aedc6aa6dfea3689d261be7f0c72efecfaf6", "8.8.0--r44hdfd78af_5": "sha256:351552e047586c4eac39273c73ad6c9823c30b580ed6573afd08993a04445ba0"}, "docker": "quay.io/biocontainers/bioconductor-raex10stprobeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-raex10stprobeset.db.
shpc-registry automated BioContainers addition for bioconductor-raex10stprobeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-raex10stprobeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-raex10stprobeset.db:8.8.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-raex10stprobeset.db/8.8.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-raex10stprobeset.db/8.8.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-raex10stprobeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-raex10stprobeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-raex10stprobeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-raex10stprobeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-raex10stprobeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-raex10stprobeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-raex10stprobeset.db

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