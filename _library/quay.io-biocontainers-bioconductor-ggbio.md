---
layout: container
name:  "quay.io/biocontainers/bioconductor-ggbio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ggbio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ggbio/container.yaml"
updated_at: "2024-05-02 02:50:38.337180"
latest: "1.50.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ggbio"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ggbio"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ggbio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ggbio", "latest": {"1.50.0--r43hdfd78af_0": "sha256:f8e8979cdece1ba0cad848f8a58585a6cb892afd450618b3fc6f3f2408594e97"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:61e99f5247749f67e252a814ba5bf0febb433f98244a766217ea1bff813efd2c", "1.46.0--r42hdfd78af_0": "sha256:bf0884ee65c46ac652a6f34a212b7ee5bad4ba03c91daee6b095fc7e80c7ebf1", "1.48.0--r43hdfd78af_0": "sha256:54d61e22008d8d448274b7cd4e77dc560acd740c48d36ab647468bde195a20a2", "1.50.0--r43hdfd78af_0": "sha256:f8e8979cdece1ba0cad848f8a58585a6cb892afd450618b3fc6f3f2408594e97"}, "docker": "quay.io/biocontainers/bioconductor-ggbio"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ggbio.
shpc-registry automated BioContainers addition for bioconductor-ggbio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ggbio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ggbio:1.50.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ggbio/1.50.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ggbio/1.50.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ggbio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggbio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ggbio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ggbio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ggbio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ggbio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ggbio

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