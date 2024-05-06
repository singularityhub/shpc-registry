---
layout: container
name:  "quay.io/biocontainers/bioconductor-orfhunter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-orfhunter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-orfhunter/container.yaml"
updated_at: "2024-05-06 03:02:22.597968"
latest: "1.10.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-orfhunter"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-orfhunter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-orfhunter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-orfhunter", "latest": {"1.10.0--r43hf17093f_0": "sha256:8691e024c4ba430ff3cd6aad5e0946b61ce747d4b66832afef0c9084de662583"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:cb6de33915c389a042224f5e8116f22c7b5c4d9f64639fed693077437070c49e", "1.6.0--r42hc247a5b_0": "sha256:9c8c8b17f1de5d21fe4f69420ddc25e816c5437c3a118e2df74d613e3a7b250d", "1.6.0--r42hf17093f_1": "sha256:c2c2508a0c1b0712f63647d2ddc930a24d0d9519f9a459f2e3b1baa26bf57775", "1.8.0--r43hf17093f_0": "sha256:3234dfe1764641efb8904e9f917b37b54e8251acd0b786f4fee520722d2aab76", "1.10.0--r43hf17093f_0": "sha256:8691e024c4ba430ff3cd6aad5e0946b61ce747d4b66832afef0c9084de662583"}, "docker": "quay.io/biocontainers/bioconductor-orfhunter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-orfhunter.
shpc-registry automated BioContainers addition for bioconductor-orfhunter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-orfhunter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-orfhunter:1.10.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-orfhunter/1.10.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-orfhunter/1.10.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-orfhunter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orfhunter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orfhunter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-orfhunter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-orfhunter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-orfhunter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-orfhunter

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