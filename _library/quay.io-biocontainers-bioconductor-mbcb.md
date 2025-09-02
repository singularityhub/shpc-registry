---
layout: container
name:  "quay.io/biocontainers/bioconductor-mbcb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mbcb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mbcb/container.yaml"
updated_at: "2025-09-02 03:51:25.728249"
latest: "1.60.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mbcb"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
 - "1.60.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mbcb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mbcb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mbcb", "latest": {"1.60.0--r44hdfd78af_0": "sha256:52879fe6afbc2d44db3120c20de7013af8868b12d1c4b8633a07a05eb6260a6a"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:1e38c7d87c4f206e198e8def1b6ff704c687f3c442db284a5f8bc92239d262ee", "1.52.0--r42hdfd78af_0": "sha256:4124c50bb1de95a5e8a60cc224395cd4cae76893f35c37fc2f458c082c9bdc40", "1.54.0--r43hdfd78af_0": "sha256:a2ae8a77988625afb474c48b422c8af480300b058f72f5518c30c9c7ebe0fa26", "1.56.0--r43hdfd78af_0": "sha256:89b774587a7be7febe4bdbe749bd4d3618f7895f2bbcb1efce714c88db1e877b", "1.60.0--r44hdfd78af_0": "sha256:52879fe6afbc2d44db3120c20de7013af8868b12d1c4b8633a07a05eb6260a6a"}, "docker": "quay.io/biocontainers/bioconductor-mbcb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mbcb.
shpc-registry automated BioContainers addition for bioconductor-mbcb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mbcb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mbcb:1.60.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mbcb/1.60.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mbcb/1.60.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mbcb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbcb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbcb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mbcb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mbcb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mbcb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mbcb

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