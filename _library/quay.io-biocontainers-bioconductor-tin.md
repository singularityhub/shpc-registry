---
layout: container
name:  "quay.io/biocontainers/bioconductor-tin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tin/container.yaml"
updated_at: "2025-03-04 03:09:29.923484"
latest: "1.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tin"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tin"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tin", "latest": {"1.38.0--r44hdfd78af_0": "sha256:ab1d6eacb46826c287d88451ccd58b99fa77003c6cb2aa25b20cb0abfe976517"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:393801e4db14f74080e4486773762464d2af1e4e891ffb8a0009044a25851398", "1.30.0--r42hdfd78af_0": "sha256:d53919f96ca69397ac45551361482669d2198b58832509d22ba883edee41bbad", "1.32.0--r43hdfd78af_0": "sha256:1d5ecd39c2572fe62cdd159ed584e0117bfc88ad9c73c76d4988fa3f2e7aad5b", "1.34.0--r43hdfd78af_0": "sha256:54986c86b9ab19a0a10dde9256b966782d18a2cc64ee38018d30beb7ea96a270", "1.38.0--r44hdfd78af_0": "sha256:ab1d6eacb46826c287d88451ccd58b99fa77003c6cb2aa25b20cb0abfe976517"}, "docker": "quay.io/biocontainers/bioconductor-tin"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tin.
shpc-registry automated BioContainers addition for bioconductor-tin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tin:1.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tin/1.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tin/1.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tin

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