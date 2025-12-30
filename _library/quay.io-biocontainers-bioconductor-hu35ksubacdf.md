---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu35ksubacdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu35ksubacdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu35ksubacdf/container.yaml"
updated_at: "2025-12-30 03:52:10.921922"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hu35ksubacdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hu35ksubacdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu35ksubacdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu35ksubacdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:57426321db50f3668e63f93389812037fc21cde8885cc11f75c7ad455ec24720"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:b8f89e5eac24aadf0d62b121d99ac270c9ab5e40d179ce06f76dbb7154549be4", "2.18.0--r42hdfd78af_10": "sha256:4c9d169d92f3e9701d5883864158583ba594e09c2d41190ecf19f6d402416670", "2.18.0--r43hdfd78af_11": "sha256:d01dd2d204f5461fd977f88cfa0832b9080e93c0a967447478d5c5b6c74d5c7a", "2.18.0--r43hdfd78af_12": "sha256:8a9908933c84afd3e12dd029fdaa3ed817061b081f090433f15474f985184049", "2.18.0--r44hdfd78af_13": "sha256:57426321db50f3668e63f93389812037fc21cde8885cc11f75c7ad455ec24720"}, "docker": "quay.io/biocontainers/bioconductor-hu35ksubacdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu35ksubacdf.
shpc-registry automated BioContainers addition for bioconductor-hu35ksubacdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu35ksubacdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu35ksubacdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu35ksubacdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hu35ksubacdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu35ksubacdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu35ksubacdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu35ksubacdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu35ksubacdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu35ksubacdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu35ksubacdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hu35ksubacdf

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