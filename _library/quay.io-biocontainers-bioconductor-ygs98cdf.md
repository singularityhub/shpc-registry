---
layout: container
name:  "quay.io/biocontainers/bioconductor-ygs98cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ygs98cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ygs98cdf/container.yaml"
updated_at: "2024-10-17 03:03:08.677450"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-ygs98cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-ygs98cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ygs98cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ygs98cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:353713837c5c1dfa8258e39d6a0a46b1e4842f650f288fa64e3b1a1d1324995c"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:b84f16f5ad2cc9cd3abc398d0f597ba38f63385d6826eab9d54f8104d5575787", "2.18.0--r42hdfd78af_10": "sha256:8b3e7a1393a0b689d5848daf165a0af74809ec969fa7708451a362e496896a16", "2.18.0--r43hdfd78af_11": "sha256:5a58a9a378869cadd74c25b60dcaf08a0fd6950a0ceba6c3b77cae91cd7fb5b7", "2.18.0--r43hdfd78af_12": "sha256:353713837c5c1dfa8258e39d6a0a46b1e4842f650f288fa64e3b1a1d1324995c"}, "docker": "quay.io/biocontainers/bioconductor-ygs98cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ygs98cdf.
shpc-registry automated BioContainers addition for bioconductor-ygs98cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ygs98cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ygs98cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ygs98cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-ygs98cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ygs98cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ygs98cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ygs98cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ygs98cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ygs98cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ygs98cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ygs98cdf

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