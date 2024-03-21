---
layout: container
name:  "quay.io/biocontainers/bioconductor-santa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-santa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-santa/container.yaml"
updated_at: "2024-03-21 03:02:24.256025"
latest: "2.38.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-santa"
aliases:
 - "glpsol"
versions:
 - "2.30.0--r41hc0cfd56_2"
 - "2.34.0--r42hc0cfd56_0"
 - "2.34.0--r42ha9d7317_2"
 - "2.36.0--r43ha9d7317_0"
 - "2.38.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-santa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-santa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-santa", "latest": {"2.38.0--r43ha9d7317_1": "sha256:848f60cca1e63bbb22ddae3a4051b94178ca9dc7be5cfaa35444560224d341e2"}, "tags": {"2.30.0--r41hc0cfd56_2": "sha256:c1446254ca0e49aa8bc386edfe9fcf1964aa736f5814860331d17e9347ebdd1a", "2.34.0--r42hc0cfd56_0": "sha256:421a4e8125128b8cb738447b1df6b7d335151e6b022d540b1c40b9451f636c52", "2.34.0--r42ha9d7317_2": "sha256:a72678b87b7d3d6c9017911522c7f7fa842eaade4d99bba9a63460b34adbbfc6", "2.36.0--r43ha9d7317_0": "sha256:aab3c8d75e1b423bc4c39643495a3e9cd550c6f9c6f303074d437fdf6c9cb6ae", "2.38.0--r43ha9d7317_1": "sha256:848f60cca1e63bbb22ddae3a4051b94178ca9dc7be5cfaa35444560224d341e2"}, "docker": "quay.io/biocontainers/bioconductor-santa", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-santa.
shpc-registry automated BioContainers addition for bioconductor-santa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-santa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-santa:2.38.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-santa/2.38.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-santa/2.38.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-santa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-santa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-santa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-santa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-santa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-santa-inspect-deffile:

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