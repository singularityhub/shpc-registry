---
layout: container
name:  "quay.io/biocontainers/bioconductor-diffloop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-diffloop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-diffloop/container.yaml"
updated_at: "2023-06-17 03:19:38.521360"
latest: "1.22.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-diffloop"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.14.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-diffloop"
config: {"url": "https://biocontainers.pro/tools/bioconductor-diffloop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-diffloop", "latest": {"1.22.0--r41hdfd78af_0": "sha256:801c8d4f61c75a3dcb50d72700149ce706659a0111e6431978e9c2d868a47338"}, "tags": {"1.8.0--r351_0": "sha256:a190e8be8ea936f4f5a567695526edfafd7b3bbea0d2c07b281a56469a173966", "1.22.0--r41hdfd78af_0": "sha256:801c8d4f61c75a3dcb50d72700149ce706659a0111e6431978e9c2d868a47338", "1.20.0--r41hdfd78af_0": "sha256:194a62b87b92ffbc69aaf46147c6ca78b317b39ae335ae41dc25223426374850", "1.18.0--r40hdfd78af_1": "sha256:1bf7dd711ce6129d77963933f344f594dbfac560f36d24b668fa0a07abb56a90", "1.16.0--r40_0": "sha256:568efd23e36a173bc3bf6521abe97d8a853b01dc8bcc3f2621282618da2dbddc", "1.14.0--r36_0": "sha256:a9ac8e48190a88e6cac7a7ceaa238a8a2b82809641159926fae55924f760de6d"}, "docker": "quay.io/biocontainers/bioconductor-diffloop", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-diffloop.
shpc-registry automated BioContainers addition for bioconductor-diffloop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-diffloop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-diffloop:1.22.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-diffloop/1.22.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-diffloop/1.22.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-diffloop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diffloop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diffloop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-diffloop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-diffloop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-diffloop-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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