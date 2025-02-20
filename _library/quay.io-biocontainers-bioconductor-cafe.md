---
layout: container
name:  "quay.io/biocontainers/bioconductor-cafe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cafe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cafe/container.yaml"
updated_at: "2025-02-20 03:31:38.726290"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cafe"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cafe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cafe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cafe", "latest": {"1.42.0--r44hdfd78af_0": "sha256:8ca3ed5ac014564814f86b1b347ffea7e25ba69263264c4966bfbad0cf75fe7d"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:b8e471bd5ecbf19b1617a1f37901fa7c4173710d3123533aeee7c29f441ae090", "1.34.0--r42hdfd78af_0": "sha256:843c53fbaa79c67fc4f05ac43768f04ba8a10731e9eaf1dfe9d63fe1b22d8d03", "1.36.0--r43hdfd78af_0": "sha256:508fc513089231bba2b8866d1efd0d7dd163308083c073449cac03532615b155", "1.38.0--r43hdfd78af_0": "sha256:848609a87291d8bed9fb0d4ff4cc310c534978b49c24b194e2af7e7b07dea860", "1.42.0--r44hdfd78af_0": "sha256:8ca3ed5ac014564814f86b1b347ffea7e25ba69263264c4966bfbad0cf75fe7d"}, "docker": "quay.io/biocontainers/bioconductor-cafe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cafe.
shpc-registry automated BioContainers addition for bioconductor-cafe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cafe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cafe:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cafe/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cafe/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cafe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cafe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cafe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cafe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cafe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cafe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cafe

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