---
layout: container
name:  "quay.io/biocontainers/bioconductor-yarn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yarn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yarn/container.yaml"
updated_at: "2024-04-29 03:01:44.061751"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-yarn"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-yarn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yarn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yarn", "latest": {"1.28.0--r43hdfd78af_0": "sha256:fade8f05661b85f79445c431087d47c7d25696c2b8ea99d93385e7522f641231"}, "tags": {"1.8.0--r351_0": "sha256:28d0a139a27e473ff709bc7ee4301e1c501040230d0212ef3aa389acc3106b4f", "1.24.0--r42hdfd78af_0": "sha256:dcd86f0c9c28016f6ed9498adbc30d2d1ca1129d0ef95aab108a53bb94469165", "1.20.0--r41hdfd78af_0": "sha256:97365a6d69cb93fcd4ba135851a6b67bfec34ea98062e9a2d6d7aab0f3acbcb8", "1.18.0--r41hdfd78af_0": "sha256:5ff74f46eae3326cdfcd62a7863aa3c1df40571bf6bde6b9e7c728f58d84067a", "1.16.0--r40hdfd78af_1": "sha256:cb1be6d32dff01c7ae28ce32630ef170fddc9d7d13d6e83616d894e6896c9abb", "1.14.0--r40_0": "sha256:bd3fd3c581f530cd407508d06522e9ff13e9a1bd7d0ae57123da25d027132e29", "1.26.0--r43hdfd78af_0": "sha256:c62bec0bf7341e3eb3dcc903f29ce28b70457d1ed20452cecbca47344e69454b", "1.28.0--r43hdfd78af_0": "sha256:fade8f05661b85f79445c431087d47c7d25696c2b8ea99d93385e7522f641231"}, "docker": "quay.io/biocontainers/bioconductor-yarn", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yarn.
shpc-registry automated BioContainers addition for bioconductor-yarn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yarn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yarn:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yarn/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-yarn/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yarn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yarn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yarn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yarn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yarn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yarn-inspect-deffile:

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