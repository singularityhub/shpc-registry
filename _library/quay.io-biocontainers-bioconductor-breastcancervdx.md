---
layout: container
name:  "quay.io/biocontainers/bioconductor-breastcancervdx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-breastcancervdx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-breastcancervdx/container.yaml"
updated_at: "2024-05-21 03:05:16.748573"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-breastcancervdx"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-breastcancervdx"
config: {"url": "https://biocontainers.pro/tools/bioconductor-breastcancervdx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-breastcancervdx", "latest": {"1.40.0--r43hdfd78af_0": "sha256:5d25a975aabaf71c0fbce60d8c3458e84f567b8ea81da567d172d60c25f28dad"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:c760db37de16a22d5a6dd79680d8e1d7ec7c1bd79c775d1796b6c5ea6805b7f7", "1.36.0--r42hdfd78af_0": "sha256:cfce44a32723676d1cf4d162fd31226b843bd4046d242541337bde06fa96c482", "1.35.0--r42hdfd78af_0": "sha256:fa45800f431ec33e62de9ca0b10ac15edb9f8264d28f9387efe770e8241b50e3", "1.38.0--r43hdfd78af_0": "sha256:49f6581ab9e3f8bbc5320fb25d0a2a9d335926cfc37af5fd811b71681824a1e3", "1.40.0--r43hdfd78af_0": "sha256:5d25a975aabaf71c0fbce60d8c3458e84f567b8ea81da567d172d60c25f28dad"}, "docker": "quay.io/biocontainers/bioconductor-breastcancervdx"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-breastcancervdx.
shpc-registry automated BioContainers addition for bioconductor-breastcancervdx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-breastcancervdx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-breastcancervdx:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-breastcancervdx/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-breastcancervdx/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-breastcancervdx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breastcancervdx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breastcancervdx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-breastcancervdx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-breastcancervdx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-breastcancervdx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-breastcancervdx

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