---
layout: container
name:  "quay.io/biocontainers/bioconductor-redseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-redseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-redseq/container.yaml"
updated_at: "2025-11-23 04:07:54.409213"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-redseq"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-redseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-redseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-redseq", "latest": {"1.52.0--r44hdfd78af_0": "sha256:60d5dd7e2ecfbc14f318e363bf6e6e73b32276838c03849439efa6a343145453"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:97d99101a820ab31890b3f8ff95a4ecf994029007ede7c9e7cc95cbe01887511", "1.44.0--r42hdfd78af_0": "sha256:ae7b07db69d06f4488ff55a768cd5084ac1ded7f68aff26a4ce2bcbf27e3b97b", "1.46.0--r43hdfd78af_0": "sha256:ad139b2ad1a001c1e58654bdc7d66d0f271dbe2190fe58f9b9c6f3a617f04cd6", "1.48.0--r43hdfd78af_0": "sha256:746bf41d3cf33b2c52ab2750443c8f6791c497aace14afbb0d9bcd9c87addce3", "1.52.0--r44hdfd78af_0": "sha256:60d5dd7e2ecfbc14f318e363bf6e6e73b32276838c03849439efa6a343145453"}, "docker": "quay.io/biocontainers/bioconductor-redseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-redseq.
shpc-registry automated BioContainers addition for bioconductor-redseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-redseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-redseq:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-redseq/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-redseq/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-redseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-redseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-redseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-redseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-redseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-redseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-redseq

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