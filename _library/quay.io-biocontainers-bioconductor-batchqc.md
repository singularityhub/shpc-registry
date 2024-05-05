---
layout: container
name:  "quay.io/biocontainers/bioconductor-batchqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-batchqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-batchqc/container.yaml"
updated_at: "2024-05-05 02:35:13.069366"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-batchqc"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.1--r341_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.14.0--r36_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-batchqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-batchqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-batchqc", "latest": {"1.30.0--r43hdfd78af_0": "sha256:5daec6ea50ee7e4431da215980cf53060d52c1b588366756ce41cb5979f1faf7"}, "tags": {"1.8.1--r341_0": "sha256:062acb6fefd3cebf9aeb4a746505af223d2e81d34279a1bc419c7fcc32207d80", "1.22.0--r41hdfd78af_0": "sha256:2aab3e97b6fd52d50ebaf54e25e27fe559c9e8aba2d7d5264c5102b57d3fa81b", "1.20.0--r41hdfd78af_0": "sha256:f9de4d493be98a61e1506a44fa85617808844d12e33540c078879ccebdec2a39", "1.18.0--r40hdfd78af_1": "sha256:2e36c9adfb19e53d748fd5c38afcc2611126933059f367dabcb48058d4aad4df", "1.16.0--r40_0": "sha256:b63f47ef0f9718439e4e9958d0f080ebbcdb8a3390eb76b51152485daad2541d", "1.14.0--r36_0": "sha256:a5c908528cb0fe1b6f3979773282f90fda023d294bb6678cee735e217e1bd1ba", "1.26.0--r42hdfd78af_0": "sha256:7bfda4d1528ebe90b50c20b31251bed6544867bc24ae4947879b2975c03cad27", "1.28.0--r43hdfd78af_0": "sha256:c522f53a5f7b10bb3f60a0435e70257f831f7e98990f4e768463950728d96ff0", "1.30.0--r43hdfd78af_0": "sha256:5daec6ea50ee7e4431da215980cf53060d52c1b588366756ce41cb5979f1faf7"}, "docker": "quay.io/biocontainers/bioconductor-batchqc", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-batchqc.
shpc-registry automated BioContainers addition for bioconductor-batchqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-batchqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-batchqc:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-batchqc/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-batchqc/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-batchqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-batchqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-batchqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-batchqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-batchqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-batchqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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