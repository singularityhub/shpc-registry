---
layout: container
name:  "quay.io/biocontainers/bioconductor-celeganscdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-celeganscdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-celeganscdf/container.yaml"
updated_at: "2025-07-20 00:58:48.459391"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-celeganscdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-celeganscdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-celeganscdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-celeganscdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:05a2060565d812f9e740a070a95ca3b022db1d3b6e7e82ddd340bdb45f9de8c9"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:850fe34fdf991fe4be6cbd4ad77972637a0de722da56179c5e4261f49d95b861", "2.18.0--r42hdfd78af_10": "sha256:cb4529f9b142253281db618613f2b49cbcc9919ebacb5118c052d1a17e9a0d7e", "2.18.0--r43hdfd78af_11": "sha256:5045e3a3cb460b8fb899dfa8c9bc341fd4ea89b8710937cc8ec23bf690b7c0fe", "2.18.0--r43hdfd78af_12": "sha256:d64c7378833e00e62cc4f69fed9a9672941287a977dcb566d7220b7571133dc9", "2.18.0--r44hdfd78af_13": "sha256:05a2060565d812f9e740a070a95ca3b022db1d3b6e7e82ddd340bdb45f9de8c9"}, "docker": "quay.io/biocontainers/bioconductor-celeganscdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-celeganscdf.
shpc-registry automated BioContainers addition for bioconductor-celeganscdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-celeganscdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-celeganscdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-celeganscdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-celeganscdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-celeganscdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celeganscdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celeganscdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-celeganscdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-celeganscdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-celeganscdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-celeganscdf

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