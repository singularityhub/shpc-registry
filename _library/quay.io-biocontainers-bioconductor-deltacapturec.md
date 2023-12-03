---
layout: container
name:  "quay.io/biocontainers/bioconductor-deltacapturec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-deltacapturec/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-deltacapturec/container.yaml"
updated_at: "2023-12-03 02:40:42.265530"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-deltacapturec"

versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-deltacapturec"
config: {"url": "https://biocontainers.pro/tools/bioconductor-deltacapturec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-deltacapturec", "latest": {"1.14.0--r43hdfd78af_0": "sha256:c2ff3b0cb424c87ebbcc3bbec86f741ee98255d157e6b8407d7e7a4f833d4d40"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:cfa7254c4b730089da10272106e695dcf76ce1baa002051f1e9709d9a662175b", "1.12.0--r42hdfd78af_0": "sha256:175bb74fb0b10b962e64fcb735932655b73e5d6d27ec5d632d5e3421ba609f31", "1.14.0--r43hdfd78af_0": "sha256:c2ff3b0cb424c87ebbcc3bbec86f741ee98255d157e6b8407d7e7a4f833d4d40"}, "docker": "quay.io/biocontainers/bioconductor-deltacapturec"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-deltacapturec.
shpc-registry automated BioContainers addition for bioconductor-deltacapturec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-deltacapturec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-deltacapturec:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-deltacapturec/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-deltacapturec/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-deltacapturec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deltacapturec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-deltacapturec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-deltacapturec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-deltacapturec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-deltacapturec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-deltacapturec

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