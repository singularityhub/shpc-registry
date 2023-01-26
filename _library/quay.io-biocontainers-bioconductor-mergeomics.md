---
layout: container
name:  "quay.io/biocontainers/bioconductor-mergeomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mergeomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mergeomics/container.yaml"
updated_at: "2023-01-26 03:19:36.674724"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mergeomics"
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
description: "shpc-registry automated BioContainers addition for bioconductor-mergeomics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mergeomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mergeomics", "latest": {"1.26.0--r42hdfd78af_0": "sha256:7ab8f5eb88d130451a9cef4ca123ad4e98e0286811cd30bf3a33e02cef19fe45"}, "tags": {"1.8.0--r341_0": "sha256:99e0fd7e78a931c30c4d6ef73c8e19ef4dc18777a26c75b19e09051ce3c781bc", "1.26.0--r42hdfd78af_0": "sha256:7ab8f5eb88d130451a9cef4ca123ad4e98e0286811cd30bf3a33e02cef19fe45", "1.22.0--r41hdfd78af_0": "sha256:b31a4878a686e17465a0c08516773d715b81ab0c7f54d52908fb3f36affc15c3", "1.20.0--r41hdfd78af_0": "sha256:becd5c7f6e081273ab41a8127e5dfb9c24cf80fc3336fc887e8dd222896fc95c", "1.18.0--r40hdfd78af_1": "sha256:015252a0599a541efbda2a507201a0e8a18151e8d7f59b9e4e5e1f5a590173b4", "1.16.0--r40_0": "sha256:7bf62c4e003b237be0544953947016ccf23a220d7e532e48d83b81238df413df"}, "docker": "quay.io/biocontainers/bioconductor-mergeomics", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mergeomics.
shpc-registry automated BioContainers addition for bioconductor-mergeomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mergeomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mergeomics:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mergeomics/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mergeomics/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mergeomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mergeomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mergeomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mergeomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mergeomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mergeomics-inspect-deffile:

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