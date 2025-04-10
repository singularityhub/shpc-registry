---
layout: container
name:  "quay.io/biocontainers/bioconductor-gcapc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gcapc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gcapc/container.yaml"
updated_at: "2025-04-10 03:56:36.686952"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gcapc"
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
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gcapc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gcapc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gcapc", "latest": {"1.30.0--r44hdfd78af_0": "sha256:7f56b8d2e3a3c641047017508fea7e2ef1f4e59dd17aa704e6d6448840e0f647"}, "tags": {"1.8.0--r36_1": "sha256:2840525f69b38d8635c6775ae36d45d7536cd5bc1727f9fd1641208fc89e2ee2", "1.22.0--r42hdfd78af_0": "sha256:65387ea288c48008a40a104db42a1d0abbe1759d7726d17b6d3493c871b9776a", "1.18.0--r41hdfd78af_0": "sha256:28cc3ba47b1704fb12c70b1f5e13af19c19849fba4981a845c3e8db58e0ba679", "1.16.0--r41hdfd78af_0": "sha256:d8a1cd5a62042adeed3a3bd4a63c0b6ad0af9acec3c7fb791e6463defa7a57e8", "1.14.0--r40hdfd78af_1": "sha256:ebf7fe8d2ca61c194bfbf2945d7732206a61572a4b0064d6afa4fbc46907636e", "1.12.0--r40_0": "sha256:1453723b2fa2e5ebb7926efbc28e328d31aa94124d0af0dcbb561732cb4005ce", "1.24.0--r43hdfd78af_0": "sha256:69e528f4e235bd50f23ed0506d1c807a373ec5f48efcfc8acbf91c057f44fb5d", "1.26.0--r43hdfd78af_0": "sha256:110141c878a2723f32f167d502b99256e7f8a3bc791361f648848112ae4e3f9f", "1.30.0--r44hdfd78af_0": "sha256:7f56b8d2e3a3c641047017508fea7e2ef1f4e59dd17aa704e6d6448840e0f647"}, "docker": "quay.io/biocontainers/bioconductor-gcapc", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gcapc.
shpc-registry automated BioContainers addition for bioconductor-gcapc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gcapc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gcapc:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gcapc/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gcapc/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gcapc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcapc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gcapc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gcapc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gcapc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gcapc-inspect-deffile:

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