---
layout: container
name:  "quay.io/biocontainers/mpra-data-access-portal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mpra-data-access-portal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mpra-data-access-portal/container.yaml"
updated_at: "2022-12-19 02:54:52.007717"
latest: "0.1.8--hdfd78af_3"
container_url: "https://biocontainers.pro/tools/mpra-data-access-portal"
aliases:
 - "mpra-data-access-portal"
 - "phantomjs"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1.8--hdfd78af_3"
description: "shpc-registry automated BioContainers addition for mpra-data-access-portal"
config: {"url": "https://biocontainers.pro/tools/mpra-data-access-portal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mpra-data-access-portal", "latest": {"0.1.8--hdfd78af_3": "sha256:9ede44226d22207714469b96ea96bb0ef2b87f73d3a228579d0f5abbc2c256d7"}, "tags": {"0.1.8--hdfd78af_3": "sha256:9ede44226d22207714469b96ea96bb0ef2b87f73d3a228579d0f5abbc2c256d7"}, "docker": "quay.io/biocontainers/mpra-data-access-portal", "aliases": {"mpra-data-access-portal": "/usr/local/bin/mpra-data-access-portal", "phantomjs": "/usr/local/bin/phantomjs", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mpra-data-access-portal.
shpc-registry automated BioContainers addition for mpra-data-access-portal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mpra-data-access-portal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mpra-data-access-portal:0.1.8--hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mpra-data-access-portal/0.1.8--hdfd78af_3
$ module help quay.io/biocontainers/mpra-data-access-portal/0.1.8--hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mpra-data-access-portal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mpra-data-access-portal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mpra-data-access-portal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mpra-data-access-portal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mpra-data-access-portal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mpra-data-access-portal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mpra-data-access-portal

```bash
$ singularity exec <container> /usr/local/bin/mpra-data-access-portal
$ podman run --it --rm --entrypoint /usr/local/bin/mpra-data-access-portal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpra-data-access-portal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phantomjs

```bash
$ singularity exec <container> /usr/local/bin/phantomjs
$ podman run --it --rm --entrypoint /usr/local/bin/phantomjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phantomjs   -v ${PWD} -w ${PWD} <container> -c " $@"
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