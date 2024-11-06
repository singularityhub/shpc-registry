---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnamodr.ribomethseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnamodr.ribomethseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnamodr.ribomethseq/container.yaml"
updated_at: "2024-11-06 02:57:39.710467"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnamodr.ribomethseq"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnamodr.ribomethseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnamodr.ribomethseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnamodr.ribomethseq", "latest": {"1.16.0--r43hdfd78af_0": "sha256:37b7f33406968582791eef8a7955b8be91fa6df61f145633f551c789963f2fb8"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:057c1c88a05a64a628437c6a18b7d1c0338a76a158516881d8ede3b06706f482", "1.12.0--r42hdfd78af_0": "sha256:8ba560eafc79324b5ce63d6543666b4031f01994895d8e623c02aeb2f2186432", "1.14.0--r43hdfd78af_0": "sha256:d5bf985d9cf4b31ba8175909a30a36472846f6edbaccae6804cd7453adda05c1", "1.16.0--r43hdfd78af_0": "sha256:37b7f33406968582791eef8a7955b8be91fa6df61f145633f551c789963f2fb8"}, "docker": "quay.io/biocontainers/bioconductor-rnamodr.ribomethseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnamodr.ribomethseq.
shpc-registry automated BioContainers addition for bioconductor-rnamodr.ribomethseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnamodr.ribomethseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnamodr.ribomethseq:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnamodr.ribomethseq/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnamodr.ribomethseq/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnamodr.ribomethseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnamodr.ribomethseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnamodr.ribomethseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnamodr.ribomethseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnamodr.ribomethseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnamodr.ribomethseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnamodr.ribomethseq

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