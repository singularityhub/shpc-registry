---
layout: container
name:  "quay.io/biocontainers/bioconductor-bsubtilisprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bsubtilisprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bsubtilisprobe/container.yaml"
updated_at: "2023-01-26 03:14:43.781135"
latest: "2.18.0--r42hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-bsubtilisprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r41hdfd78af_10"
 - "2.18.0--r42hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-bsubtilisprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bsubtilisprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bsubtilisprobe", "latest": {"2.18.0--r42hdfd78af_11": "sha256:49a5ec54e053f46a9486a713d2f5619091b4a59ab3c38c522817d4239763b00a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5694d92e361de3c13c79cf46e31f78e21f04d7c3d28fc653c1ac0df4481b62f8", "2.18.0--r41hdfd78af_10": "sha256:da06301239dbb607dcf610b0f804d78d09592e12b9a5d15d0b8ddbd096f54216", "2.18.0--r42hdfd78af_11": "sha256:49a5ec54e053f46a9486a713d2f5619091b4a59ab3c38c522817d4239763b00a"}, "docker": "quay.io/biocontainers/bioconductor-bsubtilisprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bsubtilisprobe.
shpc-registry automated BioContainers addition for bioconductor-bsubtilisprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bsubtilisprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bsubtilisprobe:2.18.0--r42hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bsubtilisprobe/2.18.0--r42hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-bsubtilisprobe/2.18.0--r42hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bsubtilisprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bsubtilisprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bsubtilisprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bsubtilisprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bsubtilisprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bsubtilisprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bsubtilisprobe

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