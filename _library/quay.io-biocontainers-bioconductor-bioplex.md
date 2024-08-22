---
layout: container
name:  "quay.io/biocontainers/bioconductor-bioplex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bioplex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bioplex/container.yaml"
updated_at: "2024-08-22 02:44:01.321667"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bioplex"

versions:
 - "1.0.1--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bioplex"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bioplex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bioplex", "latest": {"1.8.0--r43hdfd78af_0": "sha256:95056fafc2105b6443a762055def16e9879a70526367c40022f0b1115892e1bb"}, "tags": {"1.0.1--r41hdfd78af_0": "sha256:54431d9178dafcca0b9bd9814ada771cac4ba159c7dc0914748fb685c6471869", "1.4.0--r42hdfd78af_0": "sha256:67e69b2d43a23de05497a6c278b7c96cb59bf68b8a74d48b22c9b2008fc9a09a", "1.6.0--r43hdfd78af_0": "sha256:a1a8f8a9db0aebfca8e34cd374a30deea8b17b77767b91965332433a16584c57", "1.8.0--r43hdfd78af_0": "sha256:95056fafc2105b6443a762055def16e9879a70526367c40022f0b1115892e1bb"}, "docker": "quay.io/biocontainers/bioconductor-bioplex"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bioplex.
shpc-registry automated BioContainers addition for bioconductor-bioplex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bioplex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bioplex:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bioplex/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bioplex/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bioplex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioplex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioplex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bioplex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bioplex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bioplex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bioplex

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