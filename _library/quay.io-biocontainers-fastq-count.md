---
layout: container
name:  "quay.io/biocontainers/fastq-count"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-count/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-count/container.yaml"
updated_at: "2025-12-21 03:45:20.866722"
latest: "0.1.0--h7b50bb2_6"
container_url: "https://biocontainers.pro/tools/fastq-count"
aliases:
 - "fastq-count"
versions:
 - "0.1.0--hec16e2b_3"
 - "0.1.0--h031d066_5"
 - "0.1.0--h7b50bb2_6"
description: "shpc-registry automated BioContainers addition for fastq-count"
config: {"url": "https://biocontainers.pro/tools/fastq-count", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-count", "latest": {"0.1.0--h7b50bb2_6": "sha256:f731e16033c0af1ca7a716b28e149a627d3f0348f8b682c28366960247a2e79a"}, "tags": {"0.1.0--hec16e2b_3": "sha256:3caaf46f6f52f5421b4e9988c0f801224338b1bdee18fa9b2c975a0d4675f84c", "0.1.0--h031d066_5": "sha256:4a487f59d84f79b4fe91709ccb42cf176395f45387e6b590e2de58ca592f19fe", "0.1.0--h7b50bb2_6": "sha256:f731e16033c0af1ca7a716b28e149a627d3f0348f8b682c28366960247a2e79a"}, "docker": "quay.io/biocontainers/fastq-count", "aliases": {"fastq-count": "/usr/local/bin/fastq-count"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-count.
shpc-registry automated BioContainers addition for fastq-count
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-count
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-count:0.1.0--h7b50bb2_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-count/0.1.0--h7b50bb2_6
$ module help quay.io/biocontainers/fastq-count/0.1.0--h7b50bb2_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-count-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-count-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-count-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-count-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-count-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-count-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-count

```bash
$ singularity exec <container> /usr/local/bin/fastq-count
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-count   -v ${PWD} -w ${PWD} <container> -c " $@"
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