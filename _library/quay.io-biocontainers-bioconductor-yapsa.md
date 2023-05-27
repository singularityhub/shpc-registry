---
layout: container
name:  "quay.io/biocontainers/bioconductor-yapsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yapsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yapsa/container.yaml"
updated_at: "2023-05-27 03:03:41.659033"
latest: "1.24.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-yapsa"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.19.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-yapsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yapsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yapsa", "latest": {"1.24.0--r42hdfd78af_0": "sha256:98558d2991b4b4a029a3b9b056288000b11653a6a40df19a6b805e17792ce368"}, "tags": {"1.8.0--r351_0": "sha256:111aa7dbfac5cf3f026c4d92ff2c67a3e368e4ac888e8da1948c16a25af5626e", "1.19.0--r41hdfd78af_0": "sha256:d1edb509042ce5e98f84aa2e3896614add1c2c2a7ce4e83720ae39df88ed505f", "1.18.0--r41hdfd78af_0": "sha256:a190ea549efc3ed8c501c241056bdc1842bdcb14284ba89e44dc9f5c9fc286f6", "1.16.0--r40hdfd78af_1": "sha256:d1c6d668f201ceb40814d4824546afe5f4f9274399f090f76eac3c63b2eeb860", "1.14.0--r40_0": "sha256:86f05776829b2657bbaddea45f207b94264349612f5cf2543a645fbecc6d66b3", "1.12.0--r36_0": "sha256:f8a43f15c998106cddd743d40edccaecdc2545dcad19dd6e61a3948b5cbc58a0", "1.24.0--r42hdfd78af_0": "sha256:98558d2991b4b4a029a3b9b056288000b11653a6a40df19a6b805e17792ce368"}, "docker": "quay.io/biocontainers/bioconductor-yapsa", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yapsa.
shpc-registry automated BioContainers addition for bioconductor-yapsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yapsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yapsa:1.24.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yapsa/1.24.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-yapsa/1.24.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yapsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yapsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yapsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yapsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yapsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yapsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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