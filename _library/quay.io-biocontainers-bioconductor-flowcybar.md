---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowcybar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowcybar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowcybar/container.yaml"
updated_at: "2024-09-30 04:04:11.598479"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowcybar"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowcybar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowcybar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowcybar", "latest": {"1.38.0--r43hdfd78af_0": "sha256:cc79c90fc3ee6deaaf85855526d239bde177209643e095a225df7d4eb713351b"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:ddd98fc940d1f4a5ee832111d805b6eef04a21a2a3368da259fe46a3e7bd8574", "1.34.0--r42hdfd78af_0": "sha256:3276326e49e277c7ef98cbed5489023b9f5d06d7e2c1167cdfa50c1bafdbf043", "1.36.0--r43hdfd78af_0": "sha256:3299c3010e7bfe4d5de3b4cf5bb416f20469c78f28a7e664756ed061d5a97e5d", "1.38.0--r43hdfd78af_0": "sha256:cc79c90fc3ee6deaaf85855526d239bde177209643e095a225df7d4eb713351b"}, "docker": "quay.io/biocontainers/bioconductor-flowcybar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowcybar.
shpc-registry automated BioContainers addition for bioconductor-flowcybar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowcybar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowcybar:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowcybar/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowcybar/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowcybar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowcybar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowcybar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowcybar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowcybar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowcybar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowcybar

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