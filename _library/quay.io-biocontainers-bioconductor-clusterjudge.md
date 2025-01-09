---
layout: container
name:  "quay.io/biocontainers/bioconductor-clusterjudge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clusterjudge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clusterjudge/container.yaml"
updated_at: "2025-01-09 14:06:30.577479"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clusterjudge"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.1--r40hdfd78af_0"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clusterjudge"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clusterjudge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clusterjudge", "latest": {"1.24.0--r43hdfd78af_0": "sha256:3dfc96eb00aa08a1d4bd4d6f4b1ee2230e850701286d0dcfca6513335288f2ba"}, "tags": {"1.8.0--r36_0": "sha256:eec9c0de94590de05a8f2269615c5cdda5102685339358bc0a604cb0056b2152", "1.20.0--r42hdfd78af_0": "sha256:f8da4305c035cca698f0d13d10f87cf76e17ecc69b9b1904d4fe4a90154642d1", "1.16.0--r41hdfd78af_0": "sha256:40f6adc2234619aac16d490de01368bbfcdfd44f2ce0ebef7fe6452d904bbd3b", "1.14.0--r41hdfd78af_0": "sha256:7e1517912ee6df17eb7d376fd7e864649a87c16f29d3a417dbd7cc7878ab9040", "1.12.1--r40hdfd78af_0": "sha256:8d171c438a4599b1a2a87ed1d340baf1513e5459a051e235ac2ddcfbe0634fd0", "1.10.0--r40_0": "sha256:665d06a9510072e9442d7b01f3e4721d474e6b1d9ad2bbfc73e5a6907e5757bb", "1.22.0--r43hdfd78af_0": "sha256:2e12dc429625953e69e4bb8fc42117202647128f2bcd608df3cbec14034699a1", "1.24.0--r43hdfd78af_0": "sha256:3dfc96eb00aa08a1d4bd4d6f4b1ee2230e850701286d0dcfca6513335288f2ba"}, "docker": "quay.io/biocontainers/bioconductor-clusterjudge", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clusterjudge.
shpc-registry automated BioContainers addition for bioconductor-clusterjudge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clusterjudge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clusterjudge:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clusterjudge/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clusterjudge/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clusterjudge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clusterjudge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clusterjudge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clusterjudge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clusterjudge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clusterjudge-inspect-deffile:

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