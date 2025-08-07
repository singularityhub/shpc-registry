---
layout: container
name:  "quay.io/biocontainers/bioconductor-dexseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dexseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dexseq/container.yaml"
updated_at: "2025-08-07 04:40:59.326176"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dexseq"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.44.0--r42hdfd78af_2"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_1"
 - "1.48.0--r43hdfd78af_2"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dexseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dexseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dexseq", "latest": {"1.52.0--r44hdfd78af_0": "sha256:9948b2235a639998a17406d73e66251c9e06311656113aade7dd29bc46ffa378"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:a682473c623a834bc5b221baa2503b921420f3c9bbcda8e16b5f8743361b8d42", "1.44.0--r42hdfd78af_0": "sha256:57a263b14740d0605ab2d257a857e5da3cfdfea3354a187b178d1382383d53ef", "1.44.0--r42hdfd78af_2": "sha256:169d81fd01689860459241da11d47b3a20702a965c0613f4e0378d3b7c0eed24", "1.46.0--r43hdfd78af_0": "sha256:98ea567d62a73692f027afec34ec6bfcafd6019d55c96d417d8db759b963fb5b", "1.48.0--r43hdfd78af_1": "sha256:f37182a8896ffe38b5ca48e5999d7d46185ddf8a70909f2b3106ba1eadceb904", "1.48.0--r43hdfd78af_2": "sha256:7d30ecc0df6f23647beb7761947ce08fa3bb43cb5ece177fe52e9e9de00542b4", "1.52.0--r44hdfd78af_0": "sha256:9948b2235a639998a17406d73e66251c9e06311656113aade7dd29bc46ffa378"}, "docker": "quay.io/biocontainers/bioconductor-dexseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dexseq.
shpc-registry automated BioContainers addition for bioconductor-dexseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dexseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dexseq:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dexseq/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dexseq/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dexseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dexseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dexseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dexseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dexseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dexseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dexseq

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