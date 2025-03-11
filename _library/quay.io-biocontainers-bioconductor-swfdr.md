---
layout: container
name:  "quay.io/biocontainers/bioconductor-swfdr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-swfdr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-swfdr/container.yaml"
updated_at: "2025-03-11 03:00:08.176026"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-swfdr"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-swfdr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-swfdr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-swfdr", "latest": {"1.32.0--r44hdfd78af_0": "sha256:28f131be6a7679944aa5af40fae59d9c1ff49b9fd65aa7e6686154fb12f4240d"}, "tags": {"1.8.0--r351_0": "sha256:e9102990533315f2adf7f5a433f8677587639e9415c58a58f52afda80c75da4f", "1.24.0--r42hdfd78af_0": "sha256:059bd51a8b73c62955a63ea610ac52503c5e0609bbd6e56089e49c8267d4c48a", "1.20.0--r41hdfd78af_0": "sha256:7d53c7417417fe125ce5f928b799b1d27dd58c3633ac05812e49a0e3bd451ffe", "1.18.0--r41hdfd78af_0": "sha256:470614e57b78bfc01a8b4a270911d21a74fb83dc64068353eb34001f7d8a0c0e", "1.16.0--r40hdfd78af_1": "sha256:1af449ecc27b7083028caf7815bfcccd1ca4bf70108152dd62fc73afbbabbd95", "1.14.0--r40_0": "sha256:a9bf7ae9037e8c0c973233b9f8741ec340f67bc1745add925b41d8969ae90070", "1.26.0--r43hdfd78af_0": "sha256:ca04ebbd4fa3b2ae4d28b1c4871ed424e6eb2649601ce3f1314a82f41ddc4725", "1.28.0--r43hdfd78af_0": "sha256:f7feb9704149eedb0e8dc807cf32ed3e27afb14831652bb97d78f07a5baffafc", "1.32.0--r44hdfd78af_0": "sha256:28f131be6a7679944aa5af40fae59d9c1ff49b9fd65aa7e6686154fb12f4240d"}, "docker": "quay.io/biocontainers/bioconductor-swfdr", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-swfdr.
shpc-registry automated BioContainers addition for bioconductor-swfdr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-swfdr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-swfdr:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-swfdr/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-swfdr/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-swfdr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-swfdr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-swfdr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-swfdr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-swfdr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-swfdr-inspect-deffile:

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