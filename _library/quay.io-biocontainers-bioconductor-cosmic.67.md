---
layout: container
name:  "quay.io/biocontainers/bioconductor-cosmic.67"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cosmic.67/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cosmic.67/container.yaml"
updated_at: "2023-11-16 03:10:43.477343"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cosmic.67"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cosmic.67"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cosmic.67", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cosmic.67", "latest": {"1.36.0--r43hdfd78af_0": "sha256:e7f4ddc0d62bea8da258c144e1b07fee196015f87dbe85c657ab3e1400b18628"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:76e895768a0957ffb4af2a3da9627cb1f490dbd782966fd5c027d1b8d8020e92", "1.34.0--r42hdfd78af_0": "sha256:1278951be57a3d4102ec0cb9abc207e5002e4a66beaba25fb1addad17b7e8371", "1.36.0--r43hdfd78af_0": "sha256:e7f4ddc0d62bea8da258c144e1b07fee196015f87dbe85c657ab3e1400b18628"}, "docker": "quay.io/biocontainers/bioconductor-cosmic.67"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cosmic.67.
shpc-registry automated BioContainers addition for bioconductor-cosmic.67
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cosmic.67
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cosmic.67:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cosmic.67/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cosmic.67/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cosmic.67-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cosmic.67-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cosmic.67-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cosmic.67-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cosmic.67-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cosmic.67-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cosmic.67

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