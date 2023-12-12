---
layout: container
name:  "quay.io/biocontainers/consel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/consel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/consel/container.yaml"
updated_at: "2023-12-12 03:06:09.548457"
latest: "0.20--h516909a_1"
container_url: "https://biocontainers.pro/tools/consel"
aliases:
 - "catass"
 - "catci"
 - "catmt"
 - "catpv"
 - "catrep"
 - "consel"
 - "makerep"
 - "makermt"
 - "randrep"
 - "seqmt"
 - "treeass"
versions:
 - "0.20--h516909a_1"
description: "shpc-registry automated BioContainers addition for consel"
config: {"url": "https://biocontainers.pro/tools/consel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for consel", "latest": {"0.20--h516909a_1": "sha256:51033387819d0deee2fc8511ce6fb1650122573defd8bec4319c89dff2d92a45"}, "tags": {"0.20--h516909a_1": "sha256:51033387819d0deee2fc8511ce6fb1650122573defd8bec4319c89dff2d92a45"}, "docker": "quay.io/biocontainers/consel", "aliases": {"catass": "/usr/local/bin/catass", "catci": "/usr/local/bin/catci", "catmt": "/usr/local/bin/catmt", "catpv": "/usr/local/bin/catpv", "catrep": "/usr/local/bin/catrep", "consel": "/usr/local/bin/consel", "makerep": "/usr/local/bin/makerep", "makermt": "/usr/local/bin/makermt", "randrep": "/usr/local/bin/randrep", "seqmt": "/usr/local/bin/seqmt", "treeass": "/usr/local/bin/treeass"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/consel.
shpc-registry automated BioContainers addition for consel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/consel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/consel:0.20--h516909a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/consel/0.20--h516909a_1
$ module help quay.io/biocontainers/consel/0.20--h516909a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### consel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### consel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### consel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### consel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### consel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### consel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### catass

```bash
$ singularity exec <container> /usr/local/bin/catass
$ podman run --it --rm --entrypoint /usr/local/bin/catass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catci

```bash
$ singularity exec <container> /usr/local/bin/catci
$ podman run --it --rm --entrypoint /usr/local/bin/catci   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catci   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catmt

```bash
$ singularity exec <container> /usr/local/bin/catmt
$ podman run --it --rm --entrypoint /usr/local/bin/catmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catmt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catpv

```bash
$ singularity exec <container> /usr/local/bin/catpv
$ podman run --it --rm --entrypoint /usr/local/bin/catpv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catpv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catrep

```bash
$ singularity exec <container> /usr/local/bin/catrep
$ podman run --it --rm --entrypoint /usr/local/bin/catrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### consel

```bash
$ singularity exec <container> /usr/local/bin/consel
$ podman run --it --rm --entrypoint /usr/local/bin/consel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/consel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makerep

```bash
$ singularity exec <container> /usr/local/bin/makerep
$ podman run --it --rm --entrypoint /usr/local/bin/makerep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makerep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makermt

```bash
$ singularity exec <container> /usr/local/bin/makermt
$ podman run --it --rm --entrypoint /usr/local/bin/makermt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makermt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randrep

```bash
$ singularity exec <container> /usr/local/bin/randrep
$ podman run --it --rm --entrypoint /usr/local/bin/randrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqmt

```bash
$ singularity exec <container> /usr/local/bin/seqmt
$ podman run --it --rm --entrypoint /usr/local/bin/seqmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqmt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treeass

```bash
$ singularity exec <container> /usr/local/bin/treeass
$ podman run --it --rm --entrypoint /usr/local/bin/treeass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treeass   -v ${PWD} -w ${PWD} <container> -c " $@"
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