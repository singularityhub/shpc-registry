---
layout: container
name:  "quay.io/biocontainers/bioconductor-nanostringqcpro"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nanostringqcpro/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nanostringqcpro/container.yaml"
updated_at: "2024-08-31 03:28:07.683807"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nanostringqcpro"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nanostringqcpro"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nanostringqcpro", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nanostringqcpro", "latest": {"1.32.0--r43hdfd78af_0": "sha256:04e85f4f7b0b02302d10a39c780df5c88dd857c295c83676154fdf695edab40c"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:2daaec354853ad3cc781f243074d2c28c3b146af4be9aee502b2d53170f1efcc", "1.30.0--r42hdfd78af_0": "sha256:7a535ebca209c51a65ae80516b766c854b871fc4023061c3df18de9c9739425d", "1.32.0--r43hdfd78af_0": "sha256:04e85f4f7b0b02302d10a39c780df5c88dd857c295c83676154fdf695edab40c"}, "docker": "quay.io/biocontainers/bioconductor-nanostringqcpro"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nanostringqcpro.
shpc-registry automated BioContainers addition for bioconductor-nanostringqcpro
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nanostringqcpro
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nanostringqcpro:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nanostringqcpro/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nanostringqcpro/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nanostringqcpro-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanostringqcpro-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanostringqcpro-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nanostringqcpro-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nanostringqcpro-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nanostringqcpro-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nanostringqcpro

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