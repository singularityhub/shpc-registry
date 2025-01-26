---
layout: container
name:  "quay.io/biocontainers/bioconductor-clippda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clippda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clippda/container.yaml"
updated_at: "2025-01-26 03:35:29.027403"
latest: "1.56.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clippda"

versions:
 - "1.44.0--r41hdfd78af_0"
 - "1.48.0--r42hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.56.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clippda"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clippda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clippda", "latest": {"1.56.0--r44hdfd78af_0": "sha256:89b23299a8e14f149113a1a3545ddaf56c2c3fb1917c85b5c8696bb1c6079213"}, "tags": {"1.44.0--r41hdfd78af_0": "sha256:8a63a3c185c090070e5df0dd3bd9e9f0901cbbd7d070c59861081726cdd04142", "1.48.0--r42hdfd78af_0": "sha256:4e33d7a1be7825275fe41fc248d2861d8aafd3d5aa9b528f97f4634ecec8d3fc", "1.50.0--r43hdfd78af_0": "sha256:5364cd5b51bbdb2e748f9d1687a7ee4592dc5d5f708bf2b6815b77f33ef34e6f", "1.52.0--r43hdfd78af_0": "sha256:01cbdbddcc16546eff921464a5fd5981734eb311ebfdc809909ecb4486bab54f", "1.56.0--r44hdfd78af_0": "sha256:89b23299a8e14f149113a1a3545ddaf56c2c3fb1917c85b5c8696bb1c6079213"}, "docker": "quay.io/biocontainers/bioconductor-clippda"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clippda.
shpc-registry automated BioContainers addition for bioconductor-clippda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clippda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clippda:1.56.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clippda/1.56.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-clippda/1.56.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clippda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clippda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clippda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clippda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clippda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clippda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-clippda

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