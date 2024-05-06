---
layout: container
name:  "quay.io/biocontainers/bioconductor-sscu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sscu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sscu/container.yaml"
updated_at: "2024-05-06 04:46:33.258009"
latest: "2.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sscu"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r3.4.1_0"
 - "2.28.0--r42hdfd78af_0"
 - "2.24.0--r41hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r40hdfd78af_1"
 - "2.18.0--r40_0"
 - "2.30.0--r43hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sscu"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sscu", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sscu", "latest": {"2.32.0--r43hdfd78af_0": "sha256:44e34d8586de0b12053ebfdb60d58429c4fa15f97bf3cb40f6c2dbb8e9768ef0"}, "tags": {"2.8.0--r3.4.1_0": "sha256:84292bf0b534dfa362136ac8297db50f0b978642b86dcf9c293a94e71bb5fd79", "2.28.0--r42hdfd78af_0": "sha256:48b7b9ffcc04cc05d6a6f11989026d02556c9abe631d3bb1b89d592776ec0521", "2.24.0--r41hdfd78af_0": "sha256:a3c4d93b45659c6ebfac3c7c6d70776a7215ea655ec31576a44cfcb7594c18bd", "2.22.0--r41hdfd78af_0": "sha256:ba7f364fe730aa7c9f5a3006b2ce40253755367e1c406f93d6d837ca68629150", "2.20.0--r40hdfd78af_1": "sha256:71eb1d02c19d3a64a28db6ef3c69c307b536753b7068f5617e64268a1de3a3a6", "2.18.0--r40_0": "sha256:9f3754efa7fe719c2f633e73173d78881a5f033b02d0cad7200032aeec5413c7", "2.30.0--r43hdfd78af_0": "sha256:7184b95729522f8badbe6601a1568f99f8f4f0d906eeced8a80c45eca8bba5bf", "2.32.0--r43hdfd78af_0": "sha256:44e34d8586de0b12053ebfdb60d58429c4fa15f97bf3cb40f6c2dbb8e9768ef0"}, "docker": "quay.io/biocontainers/bioconductor-sscu", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sscu.
shpc-registry automated BioContainers addition for bioconductor-sscu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sscu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sscu:2.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sscu/2.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sscu/2.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sscu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sscu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sscu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sscu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sscu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sscu-inspect-deffile:

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