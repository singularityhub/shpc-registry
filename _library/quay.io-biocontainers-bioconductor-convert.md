---
layout: container
name:  "quay.io/biocontainers/bioconductor-convert"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-convert/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-convert/container.yaml"
updated_at: "2024-09-07 03:17:28.042572"
latest: "1.78.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-convert"

versions:
 - "1.70.0--r41hdfd78af_0"
 - "1.74.0--r42hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-convert"
config: {"url": "https://biocontainers.pro/tools/bioconductor-convert", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-convert", "latest": {"1.78.0--r43hdfd78af_0": "sha256:5cc33d63cfd08449d5e58b32f9cd4d9904512794e3ef94546e543ea78c93cbd7"}, "tags": {"1.70.0--r41hdfd78af_0": "sha256:9eeb0b510b0f8c994feb75d9b2c37a7df19aed4a3fdd274cc567593c51197a53", "1.74.0--r42hdfd78af_0": "sha256:ae0476b172b742267f4dfd41b0a6ae378a7068c99f024f1299b2e20253895488", "1.76.0--r43hdfd78af_0": "sha256:8a48867950f0a99cc222777b2add9c87ac2287f2ca242ce2e16830a7271dffff", "1.78.0--r43hdfd78af_0": "sha256:5cc33d63cfd08449d5e58b32f9cd4d9904512794e3ef94546e543ea78c93cbd7"}, "docker": "quay.io/biocontainers/bioconductor-convert"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-convert.
shpc-registry automated BioContainers addition for bioconductor-convert
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-convert
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-convert:1.78.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-convert/1.78.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-convert/1.78.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-convert-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-convert-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-convert-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-convert-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-convert-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-convert-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-convert

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