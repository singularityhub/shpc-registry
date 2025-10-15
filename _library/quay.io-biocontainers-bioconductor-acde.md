---
layout: container
name:  "quay.io/biocontainers/bioconductor-acde"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-acde/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-acde/container.yaml"
updated_at: "2025-10-15 03:54:02.617543"
latest: "1.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-acde"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-acde"
config: {"url": "https://biocontainers.pro/tools/bioconductor-acde", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-acde", "latest": {"1.36.0--r44hdfd78af_0": "sha256:72385e4562fec8a81f6bd098b5e8a15f7977b56285400608ca363c9093593aa5"}, "tags": {"1.8.0--r3.4.1_0": "sha256:85c9befe514ef5e7682f4b96518eaa7f32b1a28a307794c3ef80760ac0cff0d9", "1.28.0--r42hdfd78af_0": "sha256:dc8b78014a5987c5f127cdee58dfb4bf47b44d7f24ca484c14af19cd4bd9e379", "1.24.0--r41hdfd78af_0": "sha256:adc335bdd46cb249a7cb0f1bd75309875b423a42ff7dadc318fe4ff050287b29", "1.22.0--r41hdfd78af_0": "sha256:2b1d5038fbb20e7d02277e9065d3feca26091fb1ab52f68b492f3e9c3a2598ab", "1.20.0--r40hdfd78af_1": "sha256:20d1b81d410f4d22553c1e37586952061cb5fd46a589d239365d1528248df76b", "1.18.0--r40_0": "sha256:a11898f1693a3628461b485bc8ac2d6414e990b5f0b53647472aea8db5068821", "1.30.0--r43hdfd78af_0": "sha256:40cd71eb82610f9aedde7a1a7e3c6ae6f28f2e08b562a7763d6b06b2c149d22d", "1.32.0--r43hdfd78af_0": "sha256:00ae3777c2ff184fbc870d669f054e20b27269bae281a6dab6915c480f9735a8", "1.36.0--r44hdfd78af_0": "sha256:72385e4562fec8a81f6bd098b5e8a15f7977b56285400608ca363c9093593aa5"}, "docker": "quay.io/biocontainers/bioconductor-acde", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-acde.
shpc-registry automated BioContainers addition for bioconductor-acde
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-acde
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-acde:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-acde/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-acde/1.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-acde-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-acde-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-acde-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-acde-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-acde-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-acde-inspect-deffile:

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