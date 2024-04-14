---
layout: container
name:  "quay.io/biocontainers/bioconductor-moe430acdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moe430acdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moe430acdf/container.yaml"
updated_at: "2024-04-14 03:23:28.275929"
latest: "2.18.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-moe430acdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-moe430acdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moe430acdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moe430acdf", "latest": {"2.18.0--r43hdfd78af_13": "sha256:00e5b7bb379fbf175adf9d6f9f18672ceb2cef296fbeabd824da76dd5b03d641"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:72f94eaf567a19d0a90f0bc591d75c1835b8a3caa700d31780d360491638ad2d", "2.18.0--r41hdfd78af_10": "sha256:2f3dc7e127400c807c13d1ee78bec8f9ab478794f326f7bbe4ff82e18a87d9c6", "2.18.0--r42hdfd78af_11": "sha256:ad4f41317db4a16fcda0d28296824b9a3725b88e77145bf6faf980f1bcd3314a", "2.18.0--r43hdfd78af_12": "sha256:a39ba97fba5be61994a57ec599d1686f5bb0a63e18692c442b9f1d40e345a8e1", "2.18.0--r43hdfd78af_13": "sha256:00e5b7bb379fbf175adf9d6f9f18672ceb2cef296fbeabd824da76dd5b03d641"}, "docker": "quay.io/biocontainers/bioconductor-moe430acdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moe430acdf.
shpc-registry automated BioContainers addition for bioconductor-moe430acdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430acdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moe430acdf:2.18.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moe430acdf/2.18.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-moe430acdf/2.18.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moe430acdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430acdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moe430acdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moe430acdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moe430acdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moe430acdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-moe430acdf

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