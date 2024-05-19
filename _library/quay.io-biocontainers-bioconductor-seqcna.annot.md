---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqcna.annot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqcna.annot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqcna.annot/container.yaml"
updated_at: "2024-05-19 02:53:07.912670"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqcna.annot"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqcna.annot"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqcna.annot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqcna.annot", "latest": {"1.38.0--r43hdfd78af_0": "sha256:ced73c63a31800f90f6cbb20e77095e1a931a06e62cb06ad493a514369c1c143"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:e8ecf152d88a2d43120b6fc728ad84ae2d6717badd32296677975f569c2e0bc2", "1.34.0--r42hdfd78af_0": "sha256:c81af5d756e5a08c1ed20ae2bdc213caaf9165bf7dbc15ee2e0882639bc3cb23", "1.33.0--r42hdfd78af_0": "sha256:73339dd69d669589645aa5eed87f74445fd275c44d16aaffc61e7033dc535275", "1.36.0--r43hdfd78af_0": "sha256:19115356afe13f1ccd3747db1a3a1aaa7568d793fbc8ecc3c344e784ae3c9bde", "1.38.0--r43hdfd78af_0": "sha256:ced73c63a31800f90f6cbb20e77095e1a931a06e62cb06ad493a514369c1c143"}, "docker": "quay.io/biocontainers/bioconductor-seqcna.annot"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqcna.annot.
shpc-registry automated BioContainers addition for bioconductor-seqcna.annot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqcna.annot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqcna.annot:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqcna.annot/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqcna.annot/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqcna.annot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqcna.annot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqcna.annot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqcna.annot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqcna.annot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqcna.annot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqcna.annot

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