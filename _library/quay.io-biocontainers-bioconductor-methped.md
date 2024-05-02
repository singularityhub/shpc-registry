---
layout: container
name:  "quay.io/biocontainers/bioconductor-methped"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methped/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methped/container.yaml"
updated_at: "2024-05-02 02:46:16.400736"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methped"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methped"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methped", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methped", "latest": {"1.30.0--r43hdfd78af_0": "sha256:97fe8581159f2702b0c0fb83eadeda6105c6a99a9b88dd9dba017c6bcf806bca"}, "tags": {"1.8.0--r341_0": "sha256:3ee49c92ce65dbbfd1346ccd1b1bbbdb2b2b9516b9eed02761addcfed0bd362d", "1.26.0--r42hdfd78af_0": "sha256:a6f527e867574bef8d7643f1e026cc070f2bc5e2c5eb184e0ee5cdec3c186b2f", "1.22.0--r41hdfd78af_0": "sha256:56acd9adcf5b399b89d655807d0a7a7eb3a8e1a17940574941bd9d526e13c932", "1.20.0--r41hdfd78af_0": "sha256:9cea3a907162e16a1f73cb6dd0873da2eadd886599db2d843c734a5cb1c6ebec", "1.18.0--r40hdfd78af_1": "sha256:5abec5adde2df9da69c07e52e726bf838eaa63cbf650f33e77cb7f1a3f7d18b2", "1.16.0--r40_0": "sha256:866af927e1f05345e692cc6c26a22e176400e6ca33f0c351b01e9c1f28a6b6f4", "1.28.0--r43hdfd78af_0": "sha256:9e2c32c80b34880ad00810517261b5c8acc5beee3bb6adfb03c889eddbc09463", "1.30.0--r43hdfd78af_0": "sha256:97fe8581159f2702b0c0fb83eadeda6105c6a99a9b88dd9dba017c6bcf806bca"}, "docker": "quay.io/biocontainers/bioconductor-methped", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methped.
shpc-registry automated BioContainers addition for bioconductor-methped
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methped
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methped:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methped/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methped/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methped-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methped-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methped-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methped-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methped-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methped-inspect-deffile:

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