---
layout: container
name:  "quay.io/biocontainers/bioconductor-rattoxfxprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rattoxfxprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rattoxfxprobe/container.yaml"
updated_at: "2024-06-01 02:39:42.613393"
latest: "2.18.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rattoxfxprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rattoxfxprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rattoxfxprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rattoxfxprobe", "latest": {"2.18.0--r43hdfd78af_13": "sha256:384014c341c261a0d3eb5a8c19bb8e9af4c09180ef7286ecc48723021cbbae4f"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:a6e18d1d3436005a8482ba1e3bfa5e18f2133e690efa5dade5374bb71dc66123", "2.18.0--r42hdfd78af_11": "sha256:5bf5c8dbb2ef3963adcc9ec4f24ce7285407dd2b6f916c35495a01c7d2a9b330", "2.18.0--r43hdfd78af_12": "sha256:1a8a232f56e756a8456235d80de8c04faff378ddf6d95f49a22b4c1b1c1d91bc", "2.18.0--r43hdfd78af_13": "sha256:384014c341c261a0d3eb5a8c19bb8e9af4c09180ef7286ecc48723021cbbae4f"}, "docker": "quay.io/biocontainers/bioconductor-rattoxfxprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rattoxfxprobe.
shpc-registry automated BioContainers addition for bioconductor-rattoxfxprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rattoxfxprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rattoxfxprobe:2.18.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rattoxfxprobe/2.18.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rattoxfxprobe/2.18.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rattoxfxprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rattoxfxprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rattoxfxprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rattoxfxprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rattoxfxprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rattoxfxprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rattoxfxprobe

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