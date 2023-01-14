---
layout: container
name:  "quay.io/biocontainers/bioconductor-sangeranalyser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sangeranalyser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sangeranalyser/container.yaml"
updated_at: "2023-01-14 02:57:36.216652"
latest: "1.8.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sangeranalyser"
aliases:
 - "pandoc"
versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sangeranalyser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sangeranalyser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sangeranalyser", "latest": {"1.8.0--r42hdfd78af_0": "sha256:d23f36c71ba00e09b51be72fb99700994c3c6f26aa110e95130dee19a6481398"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:c942dc80b19593cc867c70dc109bd21c999d3157276b92f448bf109e3fd54e99", "1.8.0--r42hdfd78af_0": "sha256:d23f36c71ba00e09b51be72fb99700994c3c6f26aa110e95130dee19a6481398"}, "docker": "quay.io/biocontainers/bioconductor-sangeranalyser", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sangeranalyser.
shpc-registry automated BioContainers addition for bioconductor-sangeranalyser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sangeranalyser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sangeranalyser:1.8.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sangeranalyser/1.8.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sangeranalyser/1.8.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sangeranalyser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sangeranalyser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sangeranalyser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sangeranalyser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sangeranalyser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sangeranalyser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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