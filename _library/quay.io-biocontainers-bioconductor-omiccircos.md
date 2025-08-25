---
layout: container
name:  "quay.io/biocontainers/bioconductor-omiccircos"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-omiccircos/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-omiccircos/container.yaml"
updated_at: "2025-08-25 03:57:55.516944"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-omiccircos"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-omiccircos"
config: {"url": "https://biocontainers.pro/tools/bioconductor-omiccircos", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-omiccircos", "latest": {"1.44.0--r44hdfd78af_0": "sha256:2cf969829f7ad66badcfc57f78661ab344c62f09de6228e1e6bd125b03cf22ff"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:be43aa4a3c918b29e3f5a91cfce51bd9621c99f8513c3d70b0b118ba010539b9", "1.36.0--r42hdfd78af_0": "sha256:41666a920126468233482cabe75e8be9cb115b890bde9cf43b7dfdfd7a5b4ca0", "1.38.0--r43hdfd78af_0": "sha256:41e8257cf7af4a6bbef93df8533552d760ed959b9e25315b0ced3837d5c5c9f4", "1.40.0--r43hdfd78af_0": "sha256:fd5c3ae6ec4476d61aad2d963fc0f1c5868bcf02c25b277f2060df5f028e2587", "1.44.0--r44hdfd78af_0": "sha256:2cf969829f7ad66badcfc57f78661ab344c62f09de6228e1e6bd125b03cf22ff"}, "docker": "quay.io/biocontainers/bioconductor-omiccircos"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-omiccircos.
shpc-registry automated BioContainers addition for bioconductor-omiccircos
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-omiccircos
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-omiccircos:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-omiccircos/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-omiccircos/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-omiccircos-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omiccircos-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omiccircos-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-omiccircos-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-omiccircos-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-omiccircos-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-omiccircos

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