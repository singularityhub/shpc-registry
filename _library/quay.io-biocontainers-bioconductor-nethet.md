---
layout: container
name:  "quay.io/biocontainers/bioconductor-nethet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nethet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nethet/container.yaml"
updated_at: "2024-05-22 02:41:17.497340"
latest: "1.34.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nethet"
aliases:
 - "glpsol"
versions:
 - "1.26.0--r41hc0cfd56_2"
 - "1.30.0--r42hc0cfd56_0"
 - "1.30.0--r42ha9d7317_1"
 - "1.32.0--r43ha9d7317_0"
 - "1.34.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nethet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nethet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nethet", "latest": {"1.34.0--r43ha9d7317_0": "sha256:ccef8c427d3f1e4ec7251ef72643cc20be60c04727c783fc680971c6024464c8"}, "tags": {"1.26.0--r41hc0cfd56_2": "sha256:606ab5d73d12de16cadba639f8a1031503f858d5e807bb87b6141b938132204c", "1.30.0--r42hc0cfd56_0": "sha256:5eb539835fa488c7b2a9cbca52b28a64e0e2578d47b096d4e30cce5a3ea3ca37", "1.30.0--r42ha9d7317_1": "sha256:ca0bf5fd29967612e51e92e768da4829f3036f36fd07e5e17e9e09c16715c26a", "1.32.0--r43ha9d7317_0": "sha256:dfa08070b315854efe9fe70050ef6234c094e15164729d8d3c9e3cb4d2606680", "1.34.0--r43ha9d7317_0": "sha256:ccef8c427d3f1e4ec7251ef72643cc20be60c04727c783fc680971c6024464c8"}, "docker": "quay.io/biocontainers/bioconductor-nethet", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nethet.
shpc-registry automated BioContainers addition for bioconductor-nethet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nethet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nethet:1.34.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nethet/1.34.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-nethet/1.34.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nethet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nethet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nethet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nethet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nethet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nethet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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