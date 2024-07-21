---
layout: container
name:  "quay.io/biocontainers/bioconductor-structstrings"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-structstrings/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-structstrings/container.yaml"
updated_at: "2024-07-21 03:19:36.550568"
latest: "1.18.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-structstrings"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hd029910_0"
 - "1.10.0--r41hc0cfd56_2"
 - "1.14.0--r42hc0cfd56_0"
 - "1.14.0--r42ha9d7317_1"
 - "1.16.0--r43ha9d7317_0"
 - "1.18.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-structstrings"
config: {"url": "https://biocontainers.pro/tools/bioconductor-structstrings", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-structstrings", "latest": {"1.18.0--r43ha9d7317_0": "sha256:71c77d71a5cdd43a5eb5e0e973be212ce19b8c0d8c58753e937c0c1e35f2579d"}, "tags": {"1.8.0--r41hd029910_0": "sha256:8dda416ccf29528ff7e21c963eb1bef7291227a0c3f87d73460d0ed7c8d20705", "1.10.0--r41hc0cfd56_2": "sha256:980514e566d8c20d1d6153e731e722bbea8801ab3c5f6a8b9b6452400bb836d7", "1.14.0--r42hc0cfd56_0": "sha256:90ce1fc9892147f54b442b1b8ece8c66fdc433821018e6117c06031291416789", "1.14.0--r42ha9d7317_1": "sha256:c9f79a96ddb6dfcdd60b02ad08f8c55b45aaa8514543d0073242d86d2353e91b", "1.16.0--r43ha9d7317_0": "sha256:2b88e5bfab2cc2fe42adfc01869aded666b6dcc3128cd8df2fd1e26d76d24e82", "1.18.0--r43ha9d7317_0": "sha256:71c77d71a5cdd43a5eb5e0e973be212ce19b8c0d8c58753e937c0c1e35f2579d"}, "docker": "quay.io/biocontainers/bioconductor-structstrings", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-structstrings.
shpc-registry automated BioContainers addition for bioconductor-structstrings
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-structstrings
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-structstrings:1.18.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-structstrings/1.18.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-structstrings/1.18.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-structstrings-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-structstrings-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-structstrings-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-structstrings-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-structstrings-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-structstrings-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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