---
layout: container
name:  "quay.io/biocontainers/bioconductor-desousa2013"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-desousa2013/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-desousa2013/container.yaml"
updated_at: "2024-10-17 18:19:54.717677"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-desousa2013"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-desousa2013"
config: {"url": "https://biocontainers.pro/tools/bioconductor-desousa2013", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-desousa2013", "latest": {"1.38.0--r43hdfd78af_0": "sha256:220a18f5c420a09c76ba10c8ab9a954dfc67ea9cf4090320ba4b1dc4b6d0aee1"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:dd42fe45abc7f0acb1643bd78863588004e3867a2ef32f80b666053de38baf0b", "1.34.0--r42hdfd78af_0": "sha256:86c13f86722a10dd4f1af67d78cf8206ed705be4c57d32dcd8261510a05f31a8", "1.36.0--r43hdfd78af_0": "sha256:9da3f8bf5987c8fc66d817dec9290fd20188bf160e773863f19cd0ca77230f71", "1.38.0--r43hdfd78af_0": "sha256:220a18f5c420a09c76ba10c8ab9a954dfc67ea9cf4090320ba4b1dc4b6d0aee1"}, "docker": "quay.io/biocontainers/bioconductor-desousa2013"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-desousa2013.
shpc-registry automated BioContainers addition for bioconductor-desousa2013
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-desousa2013
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-desousa2013:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-desousa2013/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-desousa2013/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-desousa2013-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-desousa2013-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-desousa2013-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-desousa2013-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-desousa2013-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-desousa2013-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-desousa2013

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