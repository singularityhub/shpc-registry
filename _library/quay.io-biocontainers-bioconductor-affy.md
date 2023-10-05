---
layout: container
name:  "quay.io/biocontainers/bioconductor-affy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affy/container.yaml"
updated_at: "2023-10-05 03:10:07.411836"
latest: "1.78.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-affy"

versions:
 - "1.72.0--r41hc0cfd56_2"
 - "1.76.0--r42hc0cfd56_0"
 - "1.76.0--r42hc0cfd56_2"
 - "1.78.0--r43ha9d7317_0"
 - "1.78.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-affy"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affy", "latest": {"1.78.0--r43ha9d7317_1": "sha256:9410b76d40ababc33fa3798a54fe3ffc46b8e466ed7e1fe50e07e443f054448b"}, "tags": {"1.72.0--r41hc0cfd56_2": "sha256:6867a3eb35e617cad3721b839ab1e3b2a91c9fe3d1c54c0bd133f552ba069435", "1.76.0--r42hc0cfd56_0": "sha256:391dc8d72484a0bfe471b8cd6f24145d1eaeea70cb03a3002b673af88114cc96", "1.76.0--r42hc0cfd56_2": "sha256:e829a3df6aa3dfd79fda77a4f07fbcb8606c68c72b008bc0e27c1eb2642199d3", "1.78.0--r43ha9d7317_0": "sha256:751884217487f769527350f63d02ff4e93a17812832d9bf2ea2e1c87e631bf8d", "1.78.0--r43ha9d7317_1": "sha256:9410b76d40ababc33fa3798a54fe3ffc46b8e466ed7e1fe50e07e443f054448b"}, "docker": "quay.io/biocontainers/bioconductor-affy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affy.
shpc-registry automated BioContainers addition for bioconductor-affy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affy:1.78.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affy/1.78.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-affy/1.78.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affy

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