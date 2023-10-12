---
layout: container
name:  "quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38/container.yaml"
updated_at: "2023-10-12 03:17:40.783169"
latest: "3.7.1--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-phastcons7way.ucsc.hg38"

versions:
 - "3.7.1--r41hdfd78af_9"
 - "3.7.1--r42hdfd78af_10"
 - "3.7.1--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-phastcons7way.ucsc.hg38"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phastcons7way.ucsc.hg38", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phastcons7way.ucsc.hg38", "latest": {"3.7.1--r43hdfd78af_11": "sha256:57b6ae74184085d9b184574146bcde3ab5e63255d31f72ec8c0d44ddded68301"}, "tags": {"3.7.1--r41hdfd78af_9": "sha256:327397242ab9fa4b839ba8dbc219ad72f094ab3d5df1b848fbc5f0dfd751e014", "3.7.1--r42hdfd78af_10": "sha256:d0ca5fd6e5aebad77d6e69a2356c7f9884605f945b6e909c66d2ea00079a6656", "3.7.1--r43hdfd78af_11": "sha256:57b6ae74184085d9b184574146bcde3ab5e63255d31f72ec8c0d44ddded68301"}, "docker": "quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38.
shpc-registry automated BioContainers addition for bioconductor-phastcons7way.ucsc.hg38
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38:3.7.1--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38/3.7.1--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-phastcons7way.ucsc.hg38/3.7.1--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phastcons7way.ucsc.hg38-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phastcons7way.ucsc.hg38-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phastcons7way.ucsc.hg38-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phastcons7way.ucsc.hg38-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phastcons7way.ucsc.hg38-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phastcons7way.ucsc.hg38-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-phastcons7way.ucsc.hg38

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