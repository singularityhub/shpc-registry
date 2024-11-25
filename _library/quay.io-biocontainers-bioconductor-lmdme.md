---
layout: container
name:  "quay.io/biocontainers/bioconductor-lmdme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lmdme/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lmdme/container.yaml"
updated_at: "2024-11-25 03:48:18.459092"
latest: "1.44.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lmdme"

versions:
 - "1.36.0--r41hdfd78af_0"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lmdme"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lmdme", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lmdme", "latest": {"1.44.0--r43hdfd78af_0": "sha256:1def1e11c8a91d9485dce88ec5258f8db60520ce31d1c0248dd424e1fde17a9a"}, "tags": {"1.36.0--r41hdfd78af_0": "sha256:2afb0a43e3df24fc288a48c24ba49a212c04b043c221990a789777b89a65fc00", "1.40.0--r42hdfd78af_0": "sha256:5c13c489998666e12095a70c18b4654e6527add72d3d0e9b992fcaf617924a6a", "1.42.0--r43hdfd78af_0": "sha256:0e71e1c31e30014db93e305dbe9ea89b52fec91437244f743aac12ef5fbddb45", "1.44.0--r43hdfd78af_0": "sha256:1def1e11c8a91d9485dce88ec5258f8db60520ce31d1c0248dd424e1fde17a9a"}, "docker": "quay.io/biocontainers/bioconductor-lmdme"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lmdme.
shpc-registry automated BioContainers addition for bioconductor-lmdme
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lmdme
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lmdme:1.44.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lmdme/1.44.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lmdme/1.44.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lmdme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lmdme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lmdme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lmdme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lmdme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lmdme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lmdme

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