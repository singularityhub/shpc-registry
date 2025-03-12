---
layout: container
name:  "quay.io/biocontainers/bioconductor-genrank"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genrank/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genrank/container.yaml"
updated_at: "2025-03-12 05:06:29.702991"
latest: "1.15.0--r40_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genrank"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.15.0--r40_0"
 - "1.14.0--r36_0"
 - "1.12.0--r36_1"
 - "1.10.0--r351_0"
 - "1.8.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genrank"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genrank", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genrank", "latest": {"1.15.0--r40_0": "sha256:02773f6dc855b485fc714dd70745ca926162707077a0b4ec3956cfc9322d857c"}, "tags": {"1.8.0--r341_0": "sha256:8acddd4c9301171b02953bb47e25cdceccfd84c5c6f4c1da85ef733d833153f1", "1.15.0--r40_0": "sha256:02773f6dc855b485fc714dd70745ca926162707077a0b4ec3956cfc9322d857c", "1.14.0--r36_0": "sha256:e8e3b0f11df055bbd9b5d336a04bb5c0ee96a70247f317ef9688b3938516a20a", "1.12.0--r36_1": "sha256:671e035710e5b0f4f4929958fbc53c740132ece7e0b47fd0629e940a07c2be62", "1.10.0--r351_0": "sha256:34de32bd83b47fc0eda133c359f9da1aa6129e540cc0129ecffd67d3119e48ad", "1.8.0--r351_0": "sha256:7c0afd159c529a7a781be341f159794056fb06803e1d77ca77f3c58283549cc0"}, "docker": "quay.io/biocontainers/bioconductor-genrank", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genrank.
shpc-registry automated BioContainers addition for bioconductor-genrank
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genrank
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genrank:1.15.0--r40_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genrank/1.15.0--r40_0
$ module help quay.io/biocontainers/bioconductor-genrank/1.15.0--r40_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genrank-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genrank-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genrank-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genrank-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genrank-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genrank-inspect-deffile:

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