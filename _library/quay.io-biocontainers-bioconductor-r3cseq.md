---
layout: container
name:  "quay.io/biocontainers/bioconductor-r3cseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-r3cseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-r3cseq/container.yaml"
updated_at: "2025-09-16 03:40:22.615115"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-r3cseq"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-r3cseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-r3cseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-r3cseq", "latest": {"1.52.0--r44hdfd78af_0": "sha256:e028c75d97b7276f27cdf6165c67190745232276bacc67b9c6e75e935b6015b1"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:1692a68c9d2b600a88e1dbb1ed89d13649e5fc8350b8413ffd98ec2327d0e8d4", "1.44.0--r42hdfd78af_0": "sha256:3b3fd2ab6b34d52a4ce3ae3e39ac91d655c52cf7fb370dd46c8870557ed4bf48", "1.46.0--r43hdfd78af_0": "sha256:ca7bb186e8cfaad4d42d453fb87e790eb98d9b95627808c4d11f785299aa5ffb", "1.48.0--r43hdfd78af_0": "sha256:6aa79e3cf161dfc7a19f917113ab8452a4460fcbe813f1c5add84c4b07ea97a1", "1.52.0--r44hdfd78af_0": "sha256:e028c75d97b7276f27cdf6165c67190745232276bacc67b9c6e75e935b6015b1"}, "docker": "quay.io/biocontainers/bioconductor-r3cseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-r3cseq.
shpc-registry automated BioContainers addition for bioconductor-r3cseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-r3cseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-r3cseq:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-r3cseq/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-r3cseq/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-r3cseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-r3cseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-r3cseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-r3cseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-r3cseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-r3cseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-r3cseq

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