---
layout: container
name:  "quay.io/biocontainers/bioconductor-maaslin2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maaslin2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maaslin2/container.yaml"
updated_at: "2025-02-03 04:06:55.772804"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-maaslin2"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.1--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_1"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-maaslin2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maaslin2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maaslin2", "latest": {"1.18.0--r43hdfd78af_0": "sha256:09cce6238de60b9f72cd8ba22cbb7d9aa9f498a21973905ea7527d0476321941"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:e412db0ee818b9416615c69c48439436160c4a5658cc896e4abd05aea45cfbf1", "1.12.0--r42hdfd78af_0": "sha256:1752d210c58e37d78d74b41ef64c8959d777a2e6f6580ca91f9d0c6bc9faf4f7", "1.14.1--r43hdfd78af_0": "sha256:5374055127bc28833dabb5232584dffcb65336b3ce0ef41aa83f267c43b2dbcd", "1.16.0--r43hdfd78af_0": "sha256:d71aaf90bcf4980a87e248e096c73bb898692f6e85b37e33c9a15cfac2a2fe66", "1.16.0--r43hdfd78af_1": "sha256:25e9cb2f18aca2462656b9dc3a0dc2834c84c448e29e4940de29c250e9f7556c", "1.18.0--r43hdfd78af_0": "sha256:09cce6238de60b9f72cd8ba22cbb7d9aa9f498a21973905ea7527d0476321941"}, "docker": "quay.io/biocontainers/bioconductor-maaslin2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maaslin2.
shpc-registry automated BioContainers addition for bioconductor-maaslin2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maaslin2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maaslin2:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maaslin2/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-maaslin2/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maaslin2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maaslin2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maaslin2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maaslin2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maaslin2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maaslin2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maaslin2

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