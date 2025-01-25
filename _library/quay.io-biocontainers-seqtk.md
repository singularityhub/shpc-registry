---
layout: container
name:  "quay.io/biocontainers/seqtk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqtk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqtk/container.yaml"
updated_at: "2025-01-25 02:44:39.526476"
latest: "r93--0"
container_url: "https://biocontainers.pro/tools/seqtk"
aliases:
 - "seqtk"
versions:
 - "1.3--h7132678_4"
 - "r93--0"
 - "r82--1"
 - "1.3--he4a0461_6"
 - "1.4--he4a0461_1"
 - "1.4--he4a0461_2"
 - "1.4--h577a1d6_3"
description: "shpc-registry automated BioContainers addition for seqtk"
config: {"url": "https://biocontainers.pro/tools/seqtk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqtk", "latest": {"r93--0": "sha256:27341afe2cde846258a76378b1fce7a0177a2865375c6f5014731c883cea95e7"}, "tags": {"1.3--h7132678_4": "sha256:93e4f7c1a202e3ebfa1c3b692c733b6d520b41c4e12eeb6f099a7ca3871fd1a9", "r93--0": "sha256:27341afe2cde846258a76378b1fce7a0177a2865375c6f5014731c883cea95e7", "r82--1": "sha256:236de7d97156142b50b2f9b218baa4cb0c93f478385be4a1c910e9211bff586d", "1.3--he4a0461_6": "sha256:bb9bce3228bd88d06cbcbfbf6628a59ed1a8920655ddd3159091b7a4b358912e", "1.4--he4a0461_1": "sha256:24a4a7ebb63af178822c166befb4fcafc77d1b6754fe52fb085f0835cc274496", "1.4--he4a0461_2": "sha256:90e886efc9e10feb9cbe9f5112f2356a0dd8d8f32b0c2d40e075816ddfde519b", "1.4--h577a1d6_3": "sha256:52cd844e55162e1d81410596ec8d74cca561b05582ed786028a226bb466ce44e"}, "docker": "quay.io/biocontainers/seqtk", "aliases": {"seqtk": "/usr/local/bin/seqtk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqtk.
shpc-registry automated BioContainers addition for seqtk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqtk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqtk:r93--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqtk/r93--0
$ module help quay.io/biocontainers/seqtk/r93--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqtk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqtk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqtk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqtk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqtk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqtk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
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