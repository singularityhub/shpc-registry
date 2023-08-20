---
layout: container
name:  "quay.io/biocontainers/bioconductor-gispa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gispa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gispa/container.yaml"
updated_at: "2023-08-20 02:28:58.891919"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gispa"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gispa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gispa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gispa", "latest": {"1.24.0--r43hdfd78af_0": "sha256:ddde1f0c0b9b2ff82ae240ae765f3946963dbc151e1569620214eef9d1070e0e"}, "tags": {"1.8.0--r36_1": "sha256:c39cb2413aadf39e45934f8183e27e4a40fe83d098482c9e9bfa9928f8aa429e", "1.22.0--r42hdfd78af_0": "sha256:bf95ea75833edeacf277924acf3be70d45ba17561ddeef5dfdd828e1aeeb33b3", "1.18.0--r41hdfd78af_0": "sha256:4cafc5b71b182c10f0750f81797fe4c2ecefe019fd86ce54d46ce58adb5d679f", "1.16.0--r41hdfd78af_0": "sha256:ab12f116db3e74136b12d70b039b5c7cbd28422e1d8d8f8fdace3ac30f80b69d", "1.14.0--r40hdfd78af_1": "sha256:93d339a274fea6f221b295bce529ec0de744a3a4f2a0744b714bf9bcde03da13", "1.12.0--r40_0": "sha256:631efe5a01bc860bb858a38326da1feefb95a6bc2f860cda7e3329d9f06925cf", "1.24.0--r43hdfd78af_0": "sha256:ddde1f0c0b9b2ff82ae240ae765f3946963dbc151e1569620214eef9d1070e0e"}, "docker": "quay.io/biocontainers/bioconductor-gispa", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gispa.
shpc-registry automated BioContainers addition for bioconductor-gispa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gispa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gispa:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gispa/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gispa/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gispa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gispa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gispa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gispa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gispa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gispa-inspect-deffile:

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