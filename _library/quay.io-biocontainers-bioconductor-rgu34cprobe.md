---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgu34cprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgu34cprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgu34cprobe/container.yaml"
updated_at: "2023-11-20 03:13:56.295506"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-rgu34cprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-rgu34cprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgu34cprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgu34cprobe", "latest": {"2.18.0--r43hdfd78af_11": "sha256:313cca05fcb7f831ce213bb44b7ec5b8f56f8945e4e58ae0670e772fb55397b8"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:fa6223fb414d1616904e478a4b7fd309d546e8fad8b75829bf419660041764d5", "2.18.0--r42hdfd78af_10": "sha256:360a0cf097d39d03fcfec85503ed06bd0fd44cb1f792d74166d12fd17c03feb2", "2.18.0--r43hdfd78af_11": "sha256:313cca05fcb7f831ce213bb44b7ec5b8f56f8945e4e58ae0670e772fb55397b8"}, "docker": "quay.io/biocontainers/bioconductor-rgu34cprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgu34cprobe.
shpc-registry automated BioContainers addition for bioconductor-rgu34cprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34cprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34cprobe:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgu34cprobe/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-rgu34cprobe/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgu34cprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34cprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34cprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgu34cprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgu34cprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgu34cprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgu34cprobe

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