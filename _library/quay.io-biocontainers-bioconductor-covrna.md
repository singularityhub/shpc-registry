---
layout: container
name:  "quay.io/biocontainers/bioconductor-covrna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-covrna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-covrna/container.yaml"
updated_at: "2024-05-15 03:09:47.441646"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-covrna"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-covrna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-covrna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-covrna", "latest": {"1.26.0--r43hdfd78af_0": "sha256:bbc3194cbfa4e6115b9b21e0e7e6c8bc2059de178e0022f21aae7fa7a35f2874"}, "tags": {"1.8.0--r351_0": "sha256:1db0d791ece8ebe899f32ffdf3abaac235cb3f60597d847e0bf9d4fb891f13b3", "1.24.0--r42hdfd78af_0": "sha256:b85abed95bfa8a1ed68ed09520b62fd8ba4581084c93a723b4dd97041aadfecb", "1.20.0--r41hdfd78af_0": "sha256:0bca191f6ad3c1cef419628bd1d5955c5f3715a2f5d2c766c277ef14a4da8478", "1.18.0--r41hdfd78af_0": "sha256:576031e6132e3e4cba0479417abff7119621ece892dfe39d896f6b8f8f7de3e1", "1.16.0--r40hdfd78af_1": "sha256:deb488679e37ccce1d1ce5aae8817dc52b1dbc46eb7fe7d7b57ba17040ed6ac0", "1.14.0--r40_0": "sha256:c48e3919b5fb043e26ceaa4f8bfa793ad2ede427bbfd8373d76c18d934493645", "1.26.0--r43hdfd78af_0": "sha256:bbc3194cbfa4e6115b9b21e0e7e6c8bc2059de178e0022f21aae7fa7a35f2874"}, "docker": "quay.io/biocontainers/bioconductor-covrna", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-covrna.
shpc-registry automated BioContainers addition for bioconductor-covrna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-covrna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-covrna:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-covrna/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-covrna/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-covrna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-covrna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-covrna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-covrna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-covrna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-covrna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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