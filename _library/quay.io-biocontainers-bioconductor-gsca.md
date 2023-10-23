---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsca/container.yaml"
updated_at: "2023-10-23 02:28:39.003479"
latest: "2.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsca"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r3.4.1_0"
 - "2.28.0--r42hdfd78af_0"
 - "2.24.0--r41hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r40hdfd78af_1"
 - "2.17.0--r40_0"
 - "2.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsca", "latest": {"2.30.0--r43hdfd78af_0": "sha256:269ead0a8883faecaefd17fbfc90a5ca620ba66a98d9a4bccc559b5841a6ab7b"}, "tags": {"2.8.0--r3.4.1_0": "sha256:4f7ca4caf6a403b32bcf8a432f4568071ae340d47774fc4e86fc813ef4ab3d25", "2.28.0--r42hdfd78af_0": "sha256:d7353dc02e81cb505ecb279871d55c001e41674742cdc0e1c9e5467fe1f63c99", "2.24.0--r41hdfd78af_0": "sha256:1a05e6b2457fcbe42ed0706f74dd0e83a244b8230b31136b2eaa49bf54e18a4d", "2.22.0--r41hdfd78af_0": "sha256:4502432489f53d48567c03548b3d5391644bf2256b850a7995d922d96873f172", "2.20.0--r40hdfd78af_1": "sha256:127cf77e22a06c3ebd709fc668fa5ef900b03b25b8abead93b57f04d7aee5256", "2.17.0--r40_0": "sha256:1480cd3d8cae4e018b7fc1a1bc8369cad5fe64a10ed70bbca15f86b04a1c2866", "2.30.0--r43hdfd78af_0": "sha256:269ead0a8883faecaefd17fbfc90a5ca620ba66a98d9a4bccc559b5841a6ab7b"}, "docker": "quay.io/biocontainers/bioconductor-gsca", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsca.
shpc-registry automated BioContainers addition for bioconductor-gsca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsca:2.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsca/2.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gsca/2.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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