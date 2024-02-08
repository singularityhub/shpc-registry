---
layout: container
name:  "quay.io/biocontainers/bioconductor-hubpub"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hubpub/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hubpub/container.yaml"
updated_at: "2024-02-08 07:56:06.947152"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hubpub"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hubpub"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hubpub", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hubpub", "latest": {"1.10.0--r43hdfd78af_0": "sha256:791cc69d42f51f8231c2a81fd4fc1781d911c6fbde71777e20432ce87e1840eb"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:9d642b365c6a063cfc8d8a01b2e7e82b726a2f9bbc2e69562a183dfc1ce6b3f4", "1.6.0--r42hdfd78af_0": "sha256:d285dd1691e6d52207086aa49d6da55cf8ad46a3cc0d6d452ea1af57e620ea4d", "1.8.0--r43hdfd78af_0": "sha256:06fb45aacdee745e0051fddd642bb245fa11fa46f95d0af71bd3de49d1705d46", "1.10.0--r43hdfd78af_0": "sha256:791cc69d42f51f8231c2a81fd4fc1781d911c6fbde71777e20432ce87e1840eb"}, "docker": "quay.io/biocontainers/bioconductor-hubpub"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hubpub.
shpc-registry automated BioContainers addition for bioconductor-hubpub
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hubpub
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hubpub:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hubpub/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hubpub/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hubpub-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hubpub-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hubpub-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hubpub-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hubpub-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hubpub-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hubpub

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