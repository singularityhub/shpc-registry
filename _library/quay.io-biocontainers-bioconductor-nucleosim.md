---
layout: container
name:  "quay.io/biocontainers/bioconductor-nucleosim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nucleosim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nucleosim/container.yaml"
updated_at: "2024-03-23 03:00:54.127515"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nucleosim"
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
description: "shpc-registry automated BioContainers addition for bioconductor-nucleosim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nucleosim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nucleosim", "latest": {"1.30.0--r43hdfd78af_0": "sha256:0e0f690109c3e7dd0bc6114812a0206df79c99f04efa607ba6f60e539235d11c"}, "tags": {"1.8.0--r341_0": "sha256:685a84c3e33a46e48e632d2d14df119dec66e5fb00f0b00c6bf193295239582e", "1.26.0--r42hdfd78af_0": "sha256:683b0d2af42ea69be57b2ab9c5a3c61c7eacef67e7fba550e1af7ce7b0fde04d", "1.22.0--r41hdfd78af_0": "sha256:8e7da37c2a6103c4707150a1982311fe7416ece148d65cd2c51d41eeef7a3dc5", "1.20.0--r41hdfd78af_0": "sha256:98ee89b97a9470f5f09f54f0a0833750780586d9e464e4699c3c3d8d150faebe", "1.18.0--r40hdfd78af_1": "sha256:cc80ae1fa474b24b7c830ba38f00ba7dc09c3bf85f077cbad3ae1350ce766959", "1.16.0--r40_0": "sha256:c49d733e3a02367911ea08c02436d5b721ceb98981cf34da324dee2e27bee8b1", "1.28.0--r43hdfd78af_0": "sha256:5990d7e6dfac798111ae6ebfad20d23afb183e993ca4a4f7d2afa2825338948f", "1.30.0--r43hdfd78af_0": "sha256:0e0f690109c3e7dd0bc6114812a0206df79c99f04efa607ba6f60e539235d11c"}, "docker": "quay.io/biocontainers/bioconductor-nucleosim", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nucleosim.
shpc-registry automated BioContainers addition for bioconductor-nucleosim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nucleosim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nucleosim:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nucleosim/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nucleosim/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nucleosim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nucleosim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nucleosim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nucleosim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nucleosim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nucleosim-inspect-deffile:

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