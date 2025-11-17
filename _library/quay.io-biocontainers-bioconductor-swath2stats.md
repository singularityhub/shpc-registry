---
layout: container
name:  "quay.io/biocontainers/bioconductor-swath2stats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-swath2stats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-swath2stats/container.yaml"
updated_at: "2025-11-17 03:44:15.709013"
latest: "1.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-swath2stats"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.1--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.1--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-swath2stats"
config: {"url": "https://biocontainers.pro/tools/bioconductor-swath2stats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-swath2stats", "latest": {"1.36.0--r44hdfd78af_0": "sha256:4a263a6012158d7467822fd5ea9573015f6cc2275c847f04c0d1f7bdc541a5eb"}, "tags": {"1.8.1--r3.4.1_0": "sha256:0ba0298c5c47581611df4e172b5b791e8acf5ac94e64d21aba4266c503c7e30f", "1.24.0--r41hdfd78af_0": "sha256:e1c1587575b37e79a54c9b76f6cf41702d386a0bf9ed960c546de133e5042f94", "1.22.0--r41hdfd78af_0": "sha256:db5b6ce6194a52ba99cc15ce7eb82410a0ef10b1b66a63ad2e2602bda3a2dbe0", "1.20.0--r40hdfd78af_1": "sha256:79de54bd13fba270d737571cee5a5f5fe1f403e675dcdae6febc5d948b45b4b1", "1.18.0--r40_0": "sha256:8e04c63f34a815fb9247f64980f2fe93ec1d0072cca5738936d02bc894df227c", "1.16.0--r36_0": "sha256:ba2fd8c532aea2e436d53faab2ac67c77ea397ee1758144279f48207e5cb30bb", "1.28.0--r42hdfd78af_0": "sha256:d27cff694c4b9b7d7323d403ecfdc3d7810e4ac22047e1528816b0f19bf78f6e", "1.30.1--r43hdfd78af_0": "sha256:6b4507478e73df65d8bf0127410abdf6c64170e85e0c91c385105a2ad298767f", "1.32.0--r43hdfd78af_0": "sha256:ab556b3f164806c9d050632c8c533134f88df883375214bf965ed71e2cc63e13", "1.36.0--r44hdfd78af_0": "sha256:4a263a6012158d7467822fd5ea9573015f6cc2275c847f04c0d1f7bdc541a5eb"}, "docker": "quay.io/biocontainers/bioconductor-swath2stats", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-swath2stats.
shpc-registry automated BioContainers addition for bioconductor-swath2stats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-swath2stats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-swath2stats:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-swath2stats/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-swath2stats/1.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-swath2stats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-swath2stats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-swath2stats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-swath2stats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-swath2stats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-swath2stats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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