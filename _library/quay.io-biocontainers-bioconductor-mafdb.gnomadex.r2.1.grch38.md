---
layout: container
name:  "quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38/container.yaml"
updated_at: "2024-06-16 03:07:48.269465"
latest: "3.10.0--r43hdfd78af_9"
container_url: "https://biocontainers.pro/tools/bioconductor-mafdb.gnomadex.r2.1.grch38"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.9.0--r36_1"
 - "3.10.0--r42hdfd78af_7"
 - "3.10.0--r43hdfd78af_8"
 - "3.10.0--r43hdfd78af_9"
description: "shpc-registry automated BioContainers addition for bioconductor-mafdb.gnomadex.r2.1.grch38"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mafdb.gnomadex.r2.1.grch38", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mafdb.gnomadex.r2.1.grch38", "latest": {"3.10.0--r43hdfd78af_9": "sha256:f37e37b8ed6d352c2f515dec9bf3553988f79cb322d2e41a6d63a37544791794"}, "tags": {"3.9.0--r36_1": "sha256:3ba9bf4351281a62852de5e40de1d35b201f7dd3436929767f46d48056b48842", "3.10.0--r42hdfd78af_7": "sha256:08aa01bf991cc97fcf4786ecb9d50eac24c6a686579ac55cc7aed65056bb6461", "3.10.0--r43hdfd78af_8": "sha256:3f0e6b0ae65043508ce0365208ec28a4db8bcb267ab532c4b4e79135635479de", "3.10.0--r43hdfd78af_9": "sha256:f37e37b8ed6d352c2f515dec9bf3553988f79cb322d2e41a6d63a37544791794"}, "docker": "quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38.
shpc-registry automated BioContainers addition for bioconductor-mafdb.gnomadex.r2.1.grch38
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38:3.10.0--r43hdfd78af_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38/3.10.0--r43hdfd78af_9
$ module help quay.io/biocontainers/bioconductor-mafdb.gnomadex.r2.1.grch38/3.10.0--r43hdfd78af_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mafdb.gnomadex.r2.1.grch38-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.gnomadex.r2.1.grch38-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.gnomadex.r2.1.grch38-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mafdb.gnomadex.r2.1.grch38-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mafdb.gnomadex.r2.1.grch38-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mafdb.gnomadex.r2.1.grch38-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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