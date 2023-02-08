---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnu34cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnu34cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnu34cdf/container.yaml"
updated_at: "2023-02-08 03:29:23.580044"
latest: "2.18.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-rnu34cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-rnu34cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnu34cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnu34cdf", "latest": {"2.18.0--r42hdfd78af_10": "sha256:25efc0cc2fb257eda7cf70a06aca0237afdc242fdbeb7065480dba6643e0ff9b"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:830249f93bcbdadf9682cb4f2b1bae6bc751cea956942f90f041b536e7a5c8e1", "2.18.0--r42hdfd78af_10": "sha256:25efc0cc2fb257eda7cf70a06aca0237afdc242fdbeb7065480dba6643e0ff9b"}, "docker": "quay.io/biocontainers/bioconductor-rnu34cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnu34cdf.
shpc-registry automated BioContainers addition for bioconductor-rnu34cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnu34cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnu34cdf:2.18.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnu34cdf/2.18.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-rnu34cdf/2.18.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnu34cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnu34cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnu34cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnu34cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnu34cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnu34cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnu34cdf

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