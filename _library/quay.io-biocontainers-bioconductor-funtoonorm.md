---
layout: container
name:  "quay.io/biocontainers/bioconductor-funtoonorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-funtoonorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-funtoonorm/container.yaml"
updated_at: "2023-04-10 02:39:56.757830"
latest: "1.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-funtoonorm"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-funtoonorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-funtoonorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-funtoonorm", "latest": {"1.22.0--r42hdfd78af_0": "sha256:902b10cb76028ab963feb2f304ef63c96d9ab2f3dca6cc48ce2658d0081a8576"}, "tags": {"1.8.0--r36_1": "sha256:875d6306e98638ccd2ed62b4dbea698a8d6d5b94c905ba1d047ba97fffc46fab", "1.22.0--r42hdfd78af_0": "sha256:902b10cb76028ab963feb2f304ef63c96d9ab2f3dca6cc48ce2658d0081a8576", "1.16.0--r41hdfd78af_0": "sha256:4cff16c502d013829013d0751313c3ecf6c6720db35238f04a57e4892a26be98", "1.14.0--r40hdfd78af_1": "sha256:b82ca121854e74100318723e46df39a8c416482bdb022374dc1bc3d77dba6717", "1.12.0--r40_0": "sha256:0d94158cd4bdaac96f826f6cca3036e45970224cb451d923bcbbd643f640dd3b", "1.10.0--r36_0": "sha256:66db075805fe14a9cdfeb3eac54cf9d0ca6ceee583039ffd8a70029b5bfc3935"}, "docker": "quay.io/biocontainers/bioconductor-funtoonorm", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-funtoonorm.
shpc-registry automated BioContainers addition for bioconductor-funtoonorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-funtoonorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-funtoonorm:1.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-funtoonorm/1.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-funtoonorm/1.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-funtoonorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-funtoonorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-funtoonorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-funtoonorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-funtoonorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-funtoonorm-inspect-deffile:

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