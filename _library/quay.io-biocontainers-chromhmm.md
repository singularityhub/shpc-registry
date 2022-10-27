---
layout: container
name:  "quay.io/biocontainers/chromhmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chromhmm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/chromhmm/container.yaml"
updated_at: "2022-10-27 00:55:25.386425"
latest: "1.23--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/chromhmm"
aliases:
 - "ChromHMM.sh"
 - "download_chromhmm_data.sh"
versions:
 - "1.23--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for chromhmm"
config: {"url": "https://biocontainers.pro/tools/chromhmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chromhmm", "latest": {"1.23--hdfd78af_0": "sha256:e946f36b053df17ad5650dd13b6616e090d7eca40e088e8f7ffa2a87a8ddf2b3"}, "tags": {"1.23--hdfd78af_0": "sha256:e946f36b053df17ad5650dd13b6616e090d7eca40e088e8f7ffa2a87a8ddf2b3"}, "docker": "quay.io/biocontainers/chromhmm", "aliases": {"ChromHMM.sh": "/usr/local/bin/ChromHMM.sh", "download_chromhmm_data.sh": "/usr/local/bin/download_chromhmm_data.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chromhmm.
shpc-registry automated BioContainers addition for chromhmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chromhmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chromhmm:1.23--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chromhmm/1.23--hdfd78af_0
$ module help quay.io/biocontainers/chromhmm/1.23--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chromhmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chromhmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chromhmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chromhmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chromhmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chromhmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ChromHMM.sh

```bash
$ singularity exec <container> /usr/local/bin/ChromHMM.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ChromHMM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ChromHMM.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download_chromhmm_data.sh

```bash
$ singularity exec <container> /usr/local/bin/download_chromhmm_data.sh
$ podman run --it --rm --entrypoint /usr/local/bin/download_chromhmm_data.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download_chromhmm_data.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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