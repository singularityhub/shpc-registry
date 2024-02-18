---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcgabiolinks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcgabiolinks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcgabiolinks/container.yaml"
updated_at: "2024-02-18 02:47:08.148083"
latest: "2.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tcgabiolinks"
aliases:
 - "wget"
versions:
 - "2.8.4--r351_0"
 - "2.25.3--r42hdfd78af_0"
 - "2.22.1--r41hdfd78af_0"
 - "2.20.0--r41hdfd78af_0"
 - "2.18.0--r40hdfd78af_1"
 - "2.16.0--r40_0"
 - "2.28.3--r43hdfd78af_0"
 - "2.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tcgabiolinks"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcgabiolinks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcgabiolinks", "latest": {"2.30.0--r43hdfd78af_0": "sha256:7e8f6dd9eb9bccf32c82303f7bc551d68b1387f29d8d09333ddf9a8524011a56"}, "tags": {"2.8.4--r351_0": "sha256:5869c07ab826e15b5ec0eb991cf2130f8ee07159dfdf3bd0ed4ff2c88ef6f777", "2.25.3--r42hdfd78af_0": "sha256:66acd002968eb5d8e9d31d54333a0d64385c2faa1d74197a593b6ed9529bbaf6", "2.22.1--r41hdfd78af_0": "sha256:c65ffc8f751d4338aec03d4724d52acdd5d3c98ee139699480659392782a7bb6", "2.20.0--r41hdfd78af_0": "sha256:640d26edd969727f529aac2a3538eab53673310a86a8d2ecc2ea121e471dfee4", "2.18.0--r40hdfd78af_1": "sha256:c0ece0a64c9a5d0082ff369fac13d815a9d0e3560fa81b0fbf804bb8c4846158", "2.16.0--r40_0": "sha256:dba52bff875da6dd69cf077be2efeb9e7428adb34fc09e3ed5d74e2742bf4099", "2.28.3--r43hdfd78af_0": "sha256:2b0b967c6478bcdb29796658624a55b3ae4c16f3874c0ea3d0f9bfecfc5a22c8", "2.30.0--r43hdfd78af_0": "sha256:7e8f6dd9eb9bccf32c82303f7bc551d68b1387f29d8d09333ddf9a8524011a56"}, "docker": "quay.io/biocontainers/bioconductor-tcgabiolinks", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcgabiolinks.
shpc-registry automated BioContainers addition for bioconductor-tcgabiolinks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgabiolinks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgabiolinks:2.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcgabiolinks/2.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tcgabiolinks/2.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcgabiolinks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgabiolinks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgabiolinks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcgabiolinks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcgabiolinks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcgabiolinks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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