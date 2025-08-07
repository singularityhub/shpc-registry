---
layout: container
name:  "quay.io/biocontainers/bioconductor-gaschyhs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gaschyhs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gaschyhs/container.yaml"
updated_at: "2025-08-07 04:10:55.291853"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gaschyhs"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gaschyhs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gaschyhs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gaschyhs", "latest": {"1.44.0--r44hdfd78af_0": "sha256:b44018009e9bd4ff7e20cce578372514a3347956a8cce7e501a5a9494fec909d"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:802c68c746eaebda337ba0daad1ff75a09287391c5a13d7ec4027e18bfd69afc", "1.36.0--r42hdfd78af_0": "sha256:dd12495a239fdae3e8092e0c66cdc94c2f977b58f95878061f5ef745d37d9566", "1.38.0--r43hdfd78af_0": "sha256:abb20b1eb5ae49d284926bdbc30fb7598f664d66bf50fafded4be4e733f3c81c", "1.40.0--r43hdfd78af_0": "sha256:26e7bdac48e37dd8ad9201ead5d9d2d90097cc6ea4244c24fc8894ec59a23efb", "1.44.0--r44hdfd78af_0": "sha256:b44018009e9bd4ff7e20cce578372514a3347956a8cce7e501a5a9494fec909d"}, "docker": "quay.io/biocontainers/bioconductor-gaschyhs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gaschyhs.
shpc-registry automated BioContainers addition for bioconductor-gaschyhs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gaschyhs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gaschyhs:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gaschyhs/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gaschyhs/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gaschyhs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gaschyhs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gaschyhs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gaschyhs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gaschyhs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gaschyhs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gaschyhs

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