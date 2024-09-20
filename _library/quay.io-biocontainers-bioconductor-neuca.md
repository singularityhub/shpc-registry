---
layout: container
name:  "quay.io/biocontainers/bioconductor-neuca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-neuca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-neuca/container.yaml"
updated_at: "2024-09-20 03:48:03.737650"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-neuca"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-neuca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-neuca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-neuca", "latest": {"1.6.0--r43hdfd78af_0": "sha256:8dd7347ff7ec9ac90271814463b417a3218393e33a163eeaf52fe9446d41e19e"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:fd53727db491e6b4f3384d913becc5e33209a69bd28c20fbbd8eee3ae4ed4881", "1.4.0--r42hdfd78af_0": "sha256:cd7c0bb9138585a18fce06b3d47a51dfa26ca73f660a3599cf3d59f0a27ddea9", "1.6.0--r43hdfd78af_0": "sha256:8dd7347ff7ec9ac90271814463b417a3218393e33a163eeaf52fe9446d41e19e"}, "docker": "quay.io/biocontainers/bioconductor-neuca"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-neuca.
shpc-registry automated BioContainers addition for bioconductor-neuca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-neuca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-neuca:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-neuca/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-neuca/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-neuca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-neuca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-neuca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-neuca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-neuca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-neuca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-neuca

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