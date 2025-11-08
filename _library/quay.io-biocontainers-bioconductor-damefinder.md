---
layout: container
name:  "quay.io/biocontainers/bioconductor-damefinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-damefinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-damefinder/container.yaml"
updated_at: "2025-11-08 03:50:57.604397"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-damefinder"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-damefinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-damefinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-damefinder", "latest": {"1.18.0--r44hdfd78af_0": "sha256:8d5c1f1220d64feed2238bab8ae12ffdb6a1ea168c23d8924ac9fd35bdf5f371"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:65dc271d5151bd851e87c58be7f3171d7242300a18cbd8a0e655e902548ca66e", "1.10.0--r42hdfd78af_0": "sha256:346a98fedd0c118c764eb94f68252d0f8cb6c32712aafa8307043239c9f86280", "1.12.0--r43hdfd78af_0": "sha256:0f1cbaefa0b2fb80fce4deac3085a94033ae1da23f03180000c2b3dfa253e1d8", "1.14.0--r43hdfd78af_0": "sha256:4415f58f987352308b304e4c14be4cf20d2371cb7f484de471f32e0d4c3ecfe5", "1.18.0--r44hdfd78af_0": "sha256:8d5c1f1220d64feed2238bab8ae12ffdb6a1ea168c23d8924ac9fd35bdf5f371"}, "docker": "quay.io/biocontainers/bioconductor-damefinder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-damefinder.
shpc-registry automated BioContainers addition for bioconductor-damefinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-damefinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-damefinder:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-damefinder/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-damefinder/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-damefinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-damefinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-damefinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-damefinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-damefinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-damefinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-damefinder

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