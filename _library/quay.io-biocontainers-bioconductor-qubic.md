---
layout: container
name:  "quay.io/biocontainers/bioconductor-qubic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qubic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qubic/container.yaml"
updated_at: "2025-04-25 02:21:20.587244"
latest: "1.34.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qubic"

versions:
 - "1.22.0--r41hc247a5b_2"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hc247a5b_1"
 - "1.26.0--r42hf17093f_2"
 - "1.28.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
 - "1.34.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qubic"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qubic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qubic", "latest": {"1.34.0--r44he5774e6_0": "sha256:88bc028dcd9953b21cb488c18139cc69645973e0f1bd98467de89c8f1f95c450"}, "tags": {"1.22.0--r41hc247a5b_2": "sha256:e79cc58c714ecb1941ab1ef734edf66578379ac2dbb71ed7461001dc12d02e53", "1.26.0--r42hc247a5b_0": "sha256:acacd2f4a470640d3c3a58d379198dfcc259b2dae40f937c56f1a1e2b0b6d698", "1.26.0--r42hc247a5b_1": "sha256:17e27f54c624c0ace1d3e09f82a2cad0e862f8e9ea2ee120481eb173c3a31cfe", "1.26.0--r42hf17093f_2": "sha256:040815432aa72726b4623f1671977daae5e192492d80cb5e20585d5f5c70ab36", "1.28.0--r43hf17093f_0": "sha256:ed4aa6aa7c63d1ffa534f0f6bb804812471e85292f058398b1b56524108b4d15", "1.30.0--r43hf17093f_0": "sha256:742b92ad1227fca7518c4a9e82d385d919c8dcc305f459de4b4f4b08b1c80fa7", "1.34.0--r44he5774e6_0": "sha256:88bc028dcd9953b21cb488c18139cc69645973e0f1bd98467de89c8f1f95c450"}, "docker": "quay.io/biocontainers/bioconductor-qubic"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qubic.
shpc-registry automated BioContainers addition for bioconductor-qubic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qubic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qubic:1.34.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qubic/1.34.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-qubic/1.34.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qubic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qubic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qubic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qubic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qubic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qubic-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-qubic

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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