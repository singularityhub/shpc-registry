---
layout: container
name:  "quay.io/biocontainers/bioconductor-lola"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lola/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lola/container.yaml"
updated_at: "2023-08-02 02:29:19.967487"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lola"
aliases:
 - "wget"
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
description: "shpc-registry automated BioContainers addition for bioconductor-lola"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lola", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lola", "latest": {"1.30.0--r43hdfd78af_0": "sha256:a8d7e46e2382528bccb88ff3eec0e1164be1810b9be0e8449dd5d3c7bbd2ac5f"}, "tags": {"1.8.0--r3.4.1_0": "sha256:f01b34ef072d05e4e314dc157c86a025b42d441629f90c0f9172b0b21431ca1b", "1.28.0--r42hdfd78af_0": "sha256:5cfbf82bf06c1d13d9757654bb08c64000c551686eecfaf3cded32a216f8e8ba", "1.24.0--r41hdfd78af_0": "sha256:522771a2b593c64bba76831486bc7c70446339cd5c781968415bf2c24099fd8b", "1.22.0--r41hdfd78af_0": "sha256:2198679c541db615de9ec8911279ca3bda3ba5305165e451892e5fe7fd577044", "1.20.0--r40hdfd78af_1": "sha256:771cc982c69a964c2a42a9c8d5dd9a10febe9641a0c2c1864ea2b4b12061cc31", "1.18.0--r40_0": "sha256:ac953af7e8f1ccc37d1feee6928c6b287b56b097c776da36deb6389858cdd08a", "1.30.0--r43hdfd78af_0": "sha256:a8d7e46e2382528bccb88ff3eec0e1164be1810b9be0e8449dd5d3c7bbd2ac5f"}, "docker": "quay.io/biocontainers/bioconductor-lola", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lola.
shpc-registry automated BioContainers addition for bioconductor-lola
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lola
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lola:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lola/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lola/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lola-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lola-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lola-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lola-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lola-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lola-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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