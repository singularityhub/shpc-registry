---
layout: container
name:  "quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38/container.yaml"
updated_at: "2025-04-25 03:47:51.656471"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-phastcons30way.ucsc.hg38"

versions:
 - "3.13.0--r41hdfd78af_1"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-phastcons30way.ucsc.hg38"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phastcons30way.ucsc.hg38", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phastcons30way.ucsc.hg38", "latest": {"3.13.0--r44hdfd78af_5": "sha256:311e2d1d2970e731c7f93ead766854cc2ee7c6fd6c6af5232dd08b20b12d2b68"}, "tags": {"3.13.0--r41hdfd78af_1": "sha256:4d7c34ee9abe464ee1fa493e11b2a984ea0e883081738282fcbff8e9f0523f39", "3.13.0--r42hdfd78af_2": "sha256:6efbabf7b24faf3bda7f4324ed7ca810fb5f0bea26862b4db1c21f5f941501f4", "3.13.0--r43hdfd78af_3": "sha256:de3a3a1fa33994dc068f4145133d390068c064f9dcca53ae33e6e38169f77ea7", "3.13.0--r43hdfd78af_4": "sha256:edd3e3c37457dcc054e7bed289dd28a417460bcb240abcb6ff86b415e502fb34", "3.13.0--r44hdfd78af_5": "sha256:311e2d1d2970e731c7f93ead766854cc2ee7c6fd6c6af5232dd08b20b12d2b68"}, "docker": "quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38.
shpc-registry automated BioContainers addition for bioconductor-phastcons30way.ucsc.hg38
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-phastcons30way.ucsc.hg38/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phastcons30way.ucsc.hg38-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phastcons30way.ucsc.hg38-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phastcons30way.ucsc.hg38-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phastcons30way.ucsc.hg38-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phastcons30way.ucsc.hg38-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phastcons30way.ucsc.hg38-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-phastcons30way.ucsc.hg38

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