---
layout: container
name:  "quay.io/biocontainers/bioconductor-consensusseeker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-consensusseeker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-consensusseeker/container.yaml"
updated_at: "2023-07-25 03:23:34.443558"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-consensusseeker"
aliases:
 - "wget"
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
description: "shpc-registry automated BioContainers addition for bioconductor-consensusseeker"
config: {"url": "https://biocontainers.pro/tools/bioconductor-consensusseeker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-consensusseeker", "latest": {"1.28.0--r43hdfd78af_0": "sha256:5051195d15643e2eb92830a4f7b080e9fc4abbfe8b8d62aa84a252a2b603b218"}, "tags": {"1.8.0--r341_0": "sha256:dc8f12362f56063ed369aa5b9b987b0cd830dffdbf8f2c63e59b3470ad70dfaf", "1.26.0--r42hdfd78af_0": "sha256:28d6e2e693e769f81dfeb1f45762fa508adce593103ceb8f402942f680251706", "1.22.0--r41hdfd78af_0": "sha256:48e08dcf0aa5863e8bb3720fb8f173c5c34f257ef18d7af2a4bd099c5daf7eb4", "1.20.0--r41hdfd78af_0": "sha256:4416079b34875cdb62ca1abd3a21576e8e565cfaf6c6ad189ab7fecaa455cf2d", "1.18.0--r40hdfd78af_1": "sha256:4e4aa8bae59070dab7dd6ee06b42e4339104eedeef76d43d86f392ad5b952407", "1.16.0--r40_0": "sha256:a5ec5df8846213068f860595368c39b31e96fab080a9e0024aba9fd750a7ba25", "1.28.0--r43hdfd78af_0": "sha256:5051195d15643e2eb92830a4f7b080e9fc4abbfe8b8d62aa84a252a2b603b218"}, "docker": "quay.io/biocontainers/bioconductor-consensusseeker", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-consensusseeker.
shpc-registry automated BioContainers addition for bioconductor-consensusseeker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-consensusseeker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-consensusseeker:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-consensusseeker/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-consensusseeker/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-consensusseeker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-consensusseeker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-consensusseeker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-consensusseeker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-consensusseeker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-consensusseeker-inspect-deffile:

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