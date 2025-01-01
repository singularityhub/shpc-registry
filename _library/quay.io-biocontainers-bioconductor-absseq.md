---
layout: container
name:  "quay.io/biocontainers/bioconductor-absseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-absseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-absseq/container.yaml"
updated_at: "2025-01-01 03:12:09.226354"
latest: "1.56.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-absseq"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-absseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-absseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-absseq", "latest": {"1.56.0--r43hdfd78af_0": "sha256:a75dabec305800939328b4beb59472e37585922a7da36e550d19a2b051c69e9d"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:1f8399ca53d256e1ae032032c9583bf47660ad79e959dcb54ce4e86d77ed92c2", "1.52.0--r42hdfd78af_0": "sha256:2ceef9dc773fd845527dd715a9330e9814e7bc95c5502d257c751b7064816054", "1.54.0--r43hdfd78af_0": "sha256:5e31c6d348ac340af3aabf6b77906c6a59ebde8ffc64375dfac27eae238bf4c6", "1.56.0--r43hdfd78af_0": "sha256:a75dabec305800939328b4beb59472e37585922a7da36e550d19a2b051c69e9d"}, "docker": "quay.io/biocontainers/bioconductor-absseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-absseq.
shpc-registry automated BioContainers addition for bioconductor-absseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-absseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-absseq:1.56.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-absseq/1.56.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-absseq/1.56.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-absseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-absseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-absseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-absseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-absseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-absseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-absseq

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