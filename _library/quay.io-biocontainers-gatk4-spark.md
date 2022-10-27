---
layout: container
name:  "quay.io/biocontainers/gatk4-spark"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gatk4-spark/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gatk4-spark/container.yaml"
updated_at: "2022-10-27 01:05:25.929125"
latest: "4.3.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/gatk4-spark"

versions:
 - "4.3.0.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for gatk4-spark"
config: {"url": "https://biocontainers.pro/tools/gatk4-spark", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gatk4-spark", "latest": {"4.3.0.0--hdfd78af_0": "sha256:b891cccd973b5e356f6596a6e41eb9baf214305a502af22020ed87a8e0e84f90"}, "tags": {"4.3.0.0--hdfd78af_0": "sha256:b891cccd973b5e356f6596a6e41eb9baf214305a502af22020ed87a8e0e84f90"}, "docker": "quay.io/biocontainers/gatk4-spark"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gatk4-spark.
shpc-registry automated BioContainers addition for gatk4-spark
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gatk4-spark
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gatk4-spark:4.3.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gatk4-spark/4.3.0.0--hdfd78af_0
$ module help quay.io/biocontainers/gatk4-spark/4.3.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gatk4-spark-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gatk4-spark-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gatk4-spark-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gatk4-spark-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gatk4-spark-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gatk4-spark-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gatk4-spark

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