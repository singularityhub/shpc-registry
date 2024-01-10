---
layout: container
name:  "quay.io/biocontainers/bioconductor-rvs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rvs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rvs/container.yaml"
updated_at: "2024-01-10 03:00:51.178412"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rvs"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rvs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rvs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rvs", "latest": {"1.24.0--r43hdfd78af_0": "sha256:167ff2bc72576d559fe7a43caad3548131736ca3ebf8de4f1799539e22582ee4"}, "tags": {"1.8.0--r36_0": "sha256:db4241a77862d17434b8b9fc4ec13c916c1a01f1290a44e937d01314cb4e1c1f", "1.20.0--r42hdfd78af_0": "sha256:dfa521904890a1f0ecd14b2a8487c3067a0a58086be1d6349b581750aa42d000", "1.16.0--r41hdfd78af_0": "sha256:7ff4766468331cdb3a2310175f53e749bba90cd852a7683fe40428df8265a1c1", "1.14.0--r41hdfd78af_0": "sha256:a2a27b15fbd5bb2f04080868c295b392492b1c853b806e1d04c74858d18f4766", "1.12.0--r40hdfd78af_1": "sha256:c5345c1c8f0c41c3738f77dab06d099d851bbb62edac27ccce872504d0ac81a3", "1.10.0--r40_0": "sha256:30e9e760369be6ed6b2bb4e08ed57bc65bcf61639d3e0561ca9c8647feaf8a5b", "1.22.0--r43hdfd78af_0": "sha256:0c3427145807eb8cd78df3f00cc71976fa3a54275190d3a3992e22d1d18abbf3", "1.24.0--r43hdfd78af_0": "sha256:167ff2bc72576d559fe7a43caad3548131736ca3ebf8de4f1799539e22582ee4"}, "docker": "quay.io/biocontainers/bioconductor-rvs", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rvs.
shpc-registry automated BioContainers addition for bioconductor-rvs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rvs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rvs:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rvs/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rvs/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rvs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rvs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rvs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rvs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rvs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rvs-inspect-deffile:

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