---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtn/container.yaml"
updated_at: "2024-03-27 02:40:28.051249"
latest: "2.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtn"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.1--r36_0"
 - "2.22.0--r42hdfd78af_0"
 - "2.18.0--r41hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.1--r40hdfd78af_0"
 - "2.12.0--r40_0"
 - "2.24.0--r43hdfd78af_0"
 - "2.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtn", "latest": {"2.26.0--r43hdfd78af_0": "sha256:43468ab9bdb3dd16cb4404151ddd76b35f3f6936b237e4ed94570ee7757093e2"}, "tags": {"2.8.1--r36_0": "sha256:35d61a9af6052720d1e7c56e62324da7c2ace255dc9520a55f511974783d04ce", "2.22.0--r42hdfd78af_0": "sha256:0b85e2cafa7db1dbb83aad70373c633bfa219805b9ed60f16ed58cd41d17420b", "2.18.0--r41hdfd78af_0": "sha256:a1a18c0276f12544627b2866d479eb99053fb7e1b1f63ac145b93d98d139334f", "2.16.0--r41hdfd78af_0": "sha256:67639d6845d1a84535f65f5832539b0534815fadc3d5fc7a6209a2660d07d03e", "2.14.1--r40hdfd78af_0": "sha256:1370b56672a33aece9b61130e429e9c64c3dd5791d000fc0940a369c74b2d1af", "2.12.0--r40_0": "sha256:6418bf24e427ec679deb6b1ec60f9462ae8b4a776a12d94843a0b27cabbe5099", "2.24.0--r43hdfd78af_0": "sha256:a31f13c5726216d81beffffd421c327e8956606f7ccf1d09f71e228d34a25e5d", "2.26.0--r43hdfd78af_0": "sha256:43468ab9bdb3dd16cb4404151ddd76b35f3f6936b237e4ed94570ee7757093e2"}, "docker": "quay.io/biocontainers/bioconductor-rtn", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtn.
shpc-registry automated BioContainers addition for bioconductor-rtn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtn:2.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtn/2.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtn/2.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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