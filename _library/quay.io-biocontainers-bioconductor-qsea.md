---
layout: container
name:  "quay.io/biocontainers/bioconductor-qsea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qsea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qsea/container.yaml"
updated_at: "2023-07-31 03:14:39.292502"
latest: "1.26.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qsea"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351h14c3975_0"
 - "1.24.0--r42hc0cfd56_0"
 - "1.20.0--r41hc0cfd56_2"
 - "1.18.0--r41hd029910_0"
 - "1.16.0--r40hd029910_1"
 - "1.14.0--r40h037d062_0"
 - "1.24.0--r42ha9d7317_1"
 - "1.26.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qsea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qsea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qsea", "latest": {"1.26.0--r43ha9d7317_0": "sha256:f74e33a1bec179435d5f96b0c031c51c5aeb2dec66a7264e53bc6a5473a74b0b"}, "tags": {"1.8.0--r351h14c3975_0": "sha256:c9493b747813e21437230afcb3dbe6547b4a975c2476bea28aad6c400c8bd34d", "1.24.0--r42hc0cfd56_0": "sha256:961b63ed3f231471f2e701d1c6f755ca14354af6f5138aab2b126725e07082dc", "1.20.0--r41hc0cfd56_2": "sha256:fac5be1dda60196b46a8bffece43a53134fd83213da41d7f95eac5bcff33ded8", "1.18.0--r41hd029910_0": "sha256:c160a8ffcd5127f29883ccc7b4be002007783fa4b000b6ef45926ea5c398412f", "1.16.0--r40hd029910_1": "sha256:d4071a697dfca8dcbc5dd792508a4cbb6a633dbbdadbc64fefa29978f33392a6", "1.14.0--r40h037d062_0": "sha256:f363b76896013873b0d757a81db1aa2caf8e8463efdc2968d955e0e715bc015f", "1.24.0--r42ha9d7317_1": "sha256:18a1c61e50add3479be95e4ea3092da45b88c7ccc4c6d26f187fced22760edb4", "1.26.0--r43ha9d7317_0": "sha256:f74e33a1bec179435d5f96b0c031c51c5aeb2dec66a7264e53bc6a5473a74b0b"}, "docker": "quay.io/biocontainers/bioconductor-qsea", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qsea.
shpc-registry automated BioContainers addition for bioconductor-qsea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qsea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qsea:1.26.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qsea/1.26.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-qsea/1.26.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qsea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qsea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qsea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qsea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qsea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qsea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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