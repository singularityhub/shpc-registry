---
layout: container
name:  "quay.io/biocontainers/bioconductor-dks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dks/container.yaml"
updated_at: "2026-01-15 04:10:18.764272"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dks"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dks"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dks", "latest": {"1.52.0--r44hdfd78af_0": "sha256:49121b21242655983a0bd2616b448a9dabdfe69f47b4645c76e2205601c76907"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:7b41b7fc6128ae3b1f5e472664397dfa7318997c07bf9786ee45cc02da6114af", "1.44.0--r42hdfd78af_0": "sha256:6f9bc57af796b8141ecadf247389b94c815896c948572c2413cc4348487d76d3", "1.46.0--r43hdfd78af_0": "sha256:f20c5eeb0bc9592ef61e1f0b21f397e9e4967e27c28f1a1194714fa1601e611f", "1.48.0--r43hdfd78af_0": "sha256:0db6f6860f500c2edb07a26c3e13852219b829094cbe7cbad6bb0d0c29e474cb", "1.52.0--r44hdfd78af_0": "sha256:49121b21242655983a0bd2616b448a9dabdfe69f47b4645c76e2205601c76907"}, "docker": "quay.io/biocontainers/bioconductor-dks"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dks.
shpc-registry automated BioContainers addition for bioconductor-dks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dks:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dks/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dks/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dks

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