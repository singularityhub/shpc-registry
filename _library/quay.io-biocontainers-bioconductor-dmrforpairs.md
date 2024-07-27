---
layout: container
name:  "quay.io/biocontainers/bioconductor-dmrforpairs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dmrforpairs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dmrforpairs/container.yaml"
updated_at: "2024-07-27 03:19:03.591098"
latest: "1.35.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dmrforpairs"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.35.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dmrforpairs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dmrforpairs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dmrforpairs", "latest": {"1.35.0--r43hdfd78af_0": "sha256:e3d177dcc318af649d751975ea5daff128bfaae4a04a52a5b9660ac29126d572"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:0c2d87846719792bfcec02130e4512d8650783b91d0f38440a615319add412ec", "1.34.0--r42hdfd78af_0": "sha256:86d387f4b234eaf1a43e941c64c6af84485bf6c7747013d874e336987b68f52d", "1.35.0--r43hdfd78af_0": "sha256:e3d177dcc318af649d751975ea5daff128bfaae4a04a52a5b9660ac29126d572"}, "docker": "quay.io/biocontainers/bioconductor-dmrforpairs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dmrforpairs.
shpc-registry automated BioContainers addition for bioconductor-dmrforpairs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dmrforpairs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dmrforpairs:1.35.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dmrforpairs/1.35.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dmrforpairs/1.35.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dmrforpairs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmrforpairs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dmrforpairs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dmrforpairs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dmrforpairs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dmrforpairs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dmrforpairs

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