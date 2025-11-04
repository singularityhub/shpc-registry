---
layout: container
name:  "quay.io/biocontainers/bioconductor-eatonetalchipseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-eatonetalchipseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-eatonetalchipseq/container.yaml"
updated_at: "2025-11-04 03:13:50.223163"
latest: "0.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-eatonetalchipseq"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.36.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
 - "0.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-eatonetalchipseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-eatonetalchipseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-eatonetalchipseq", "latest": {"0.44.0--r44hdfd78af_0": "sha256:45f97f6351bb7cbe60323c9a4866c2faabda8e0d3729c79d3fc50594fd91094f"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:5e205c8132f80a6ac8591eb2fb452ad303ce28117bdc8030046a4d5174c58a58", "0.36.0--r42hdfd78af_0": "sha256:a51c1957c2d8a979a5992fe8095c807d2771a81c5d70567b62ee565a926b3d96", "0.38.0--r43hdfd78af_0": "sha256:cabc13a3ac0b59b0220a39f7b14e5734530d2c6f0d09472964225c35c102ad6f", "0.40.0--r43hdfd78af_0": "sha256:b099b909ab6e2086aa69cff20a3731d45ecad91d597a559c132b06aba95788dd", "0.44.0--r44hdfd78af_0": "sha256:45f97f6351bb7cbe60323c9a4866c2faabda8e0d3729c79d3fc50594fd91094f"}, "docker": "quay.io/biocontainers/bioconductor-eatonetalchipseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-eatonetalchipseq.
shpc-registry automated BioContainers addition for bioconductor-eatonetalchipseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-eatonetalchipseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-eatonetalchipseq:0.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-eatonetalchipseq/0.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-eatonetalchipseq/0.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-eatonetalchipseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eatonetalchipseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-eatonetalchipseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-eatonetalchipseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-eatonetalchipseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-eatonetalchipseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-eatonetalchipseq

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