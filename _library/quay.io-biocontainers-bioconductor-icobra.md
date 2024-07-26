---
layout: container
name:  "quay.io/biocontainers/bioconductor-icobra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-icobra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-icobra/container.yaml"
updated_at: "2024-07-26 03:25:11.945686"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-icobra"
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
description: "shpc-registry automated BioContainers addition for bioconductor-icobra"
config: {"url": "https://biocontainers.pro/tools/bioconductor-icobra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-icobra", "latest": {"1.30.0--r43hdfd78af_0": "sha256:f1ffe8a0bb25ebbd66188406133bd896b34d78f979c85ab17b568c49bc20170e"}, "tags": {"1.8.0--r341_0": "sha256:982a8f7a2f3aabf4a32862df5a545421986ccb62e4f555e7b1097a15401a9a20", "1.26.0--r42hdfd78af_0": "sha256:ebde2c15749d16a803e0aa66cd8c9821b0369510b9f8d9bd9c225d756743b13d", "1.22.0--r41hdfd78af_0": "sha256:0c008861bd04f6daf9cf5e4ce03105d8e3b24c29dec596748553ac9ed62cf204", "1.20.0--r41hdfd78af_0": "sha256:a76f364083e4bbf04e1d9d3d2567a5d63f93552f363690cfbb257f74899e4793", "1.18.0--r40hdfd78af_1": "sha256:ade3b44aa72fbd72ba78ae2626a0956d43e69691ab55c07af80549c9dbf90746", "1.16.0--r40_0": "sha256:3d224aaf52812b0f1cfa56c119f395479f4242d1e2ab39baa76759e75057285e", "1.28.0--r43hdfd78af_0": "sha256:6f79d8d3e4bef2c8836adc982ade82cd3c0b52de1405e0b1030fdf079bff26db", "1.30.0--r43hdfd78af_0": "sha256:f1ffe8a0bb25ebbd66188406133bd896b34d78f979c85ab17b568c49bc20170e"}, "docker": "quay.io/biocontainers/bioconductor-icobra", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-icobra.
shpc-registry automated BioContainers addition for bioconductor-icobra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-icobra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-icobra:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-icobra/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-icobra/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-icobra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-icobra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-icobra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-icobra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-icobra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-icobra-inspect-deffile:

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