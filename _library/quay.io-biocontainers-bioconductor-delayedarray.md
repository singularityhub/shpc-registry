---
layout: container
name:  "quay.io/biocontainers/bioconductor-delayedarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-delayedarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-delayedarray/container.yaml"
updated_at: "2024-11-18 03:20:16.896781"
latest: "0.28.0--r43ha9d7317_2"
container_url: "https://biocontainers.pro/tools/bioconductor-delayedarray"
aliases:
 - "c89"
 - "c99"
versions:
 - "0.8.0--r351h14c3975_0"
 - "0.24.0--r42hc0cfd56_0"
 - "0.20.0--r41hc0cfd56_2"
 - "0.18.0--r41hd029910_0"
 - "0.16.3--r40hd029910_0"
 - "0.14.0--r40h037d062_0"
 - "0.24.0--r42ha9d7317_1"
 - "0.26.6--r43ha9d7317_0"
 - "0.28.0--r43ha9d7317_1"
 - "0.28.0--r43ha9d7317_2"
description: "shpc-registry automated BioContainers addition for bioconductor-delayedarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-delayedarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-delayedarray", "latest": {"0.28.0--r43ha9d7317_2": "sha256:b32b5f366ef4bc097d634874cdd1fe7570b76b5622716a969caa15b9c55c5c59"}, "tags": {"0.8.0--r351h14c3975_0": "sha256:0b945d7155de70e961ddb914b596ccff70d76c9f0ca0b5360b48e0aa103ef01e", "0.24.0--r42hc0cfd56_0": "sha256:af5bfcd1ad096fb66eaea08d137317419856076729d3c0afb084b6432062fd3c", "0.20.0--r41hc0cfd56_2": "sha256:c3f36980beb5a98ebb4d4498c011e002984345e46648e900e798405acb0bbea9", "0.18.0--r41hd029910_0": "sha256:e917f1eacafcd961697870976fc9ca9c866425e341db286ec7d480536033a114", "0.16.3--r40hd029910_0": "sha256:9cf7b96dc636853343fac2c23ac3fab5ceb680f0f9d9042d0c25beddeb76130b", "0.14.0--r40h037d062_0": "sha256:412647ce998d5ece4e13668281b6ad6369d0968a643da48bd6c83662a9003b69", "0.24.0--r42ha9d7317_1": "sha256:f270b4f033526670036a24a3069743d6f9b332750e4112f61f12cd8db6ab5d8e", "0.26.6--r43ha9d7317_0": "sha256:135d937d7a1699854c6bef8ff6aa62c5a028f8d4726d36834dda07a497f53db7", "0.28.0--r43ha9d7317_1": "sha256:4d170846a1438499c210745aa45dae15c1f21c4a14e12a59d86cdf8285804884", "0.28.0--r43ha9d7317_2": "sha256:b32b5f366ef4bc097d634874cdd1fe7570b76b5622716a969caa15b9c55c5c59"}, "docker": "quay.io/biocontainers/bioconductor-delayedarray", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-delayedarray.
shpc-registry automated BioContainers addition for bioconductor-delayedarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-delayedarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-delayedarray:0.28.0--r43ha9d7317_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-delayedarray/0.28.0--r43ha9d7317_2
$ module help quay.io/biocontainers/bioconductor-delayedarray/0.28.0--r43ha9d7317_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-delayedarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayedarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayedarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-delayedarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-delayedarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-delayedarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
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