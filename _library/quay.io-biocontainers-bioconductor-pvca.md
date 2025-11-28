---
layout: container
name:  "quay.io/biocontainers/bioconductor-pvca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pvca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pvca/container.yaml"
updated_at: "2025-11-28 03:22:39.705359"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pvca"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pvca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pvca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pvca", "latest": {"1.46.0--r44hdfd78af_0": "sha256:74014efde2c58c7311b505a523a835476d055f8a44ed6c2bfd01c5be3ca621ee"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:899c84b896f50ee86b75acbec95709b8b97129a2748d3d8276bb734f63ad6f4a", "1.38.0--r42hdfd78af_0": "sha256:360403f4bccc1584f8556b0500cf6c1a34cb84c09a0db09502aa1bce1031e83c", "1.40.0--r43hdfd78af_0": "sha256:6e04b16f679c0574327b12712c0e5a84fa73636e38ce0873f000d6a1be38904a", "1.42.0--r43hdfd78af_0": "sha256:ef68eb7acc5abb61e70b91c3fd99907ba6e7b86548e9adc23febebc7c98d66a1", "1.46.0--r44hdfd78af_0": "sha256:74014efde2c58c7311b505a523a835476d055f8a44ed6c2bfd01c5be3ca621ee"}, "docker": "quay.io/biocontainers/bioconductor-pvca"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pvca.
shpc-registry automated BioContainers addition for bioconductor-pvca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pvca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pvca:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pvca/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pvca/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pvca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pvca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pvca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pvca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pvca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pvca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pvca

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