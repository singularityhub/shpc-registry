---
layout: container
name:  "quay.io/biocontainers/hyphy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hyphy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hyphy/container.yaml"
updated_at: "2024-11-24 03:30:12.581674"
latest: "2.5.63--h0d74fca_0"
container_url: "https://biocontainers.pro/tools/hyphy"

versions:
 - "2.5.9--ha076c6e_0"
 - "2.5.38--h91ae1e9_0"
 - "2.5.60--h0705fce_0"
 - "2.5.61--h0705fce_0"
 - "2.5.62--h0705fce_0"
 - "2.5.62--h0d74fca_1"
 - "2.5.63--h0d74fca_0"
description: "shpc-registry automated BioContainers addition for hyphy"
config: {"url": "https://biocontainers.pro/tools/hyphy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hyphy", "latest": {"2.5.63--h0d74fca_0": "sha256:89c67de33a8e24b2d2edf699b6be04b3698801a58de30f90d63d239cafb05271"}, "tags": {"2.5.9--ha076c6e_0": "sha256:a84936a03479d9782d991344e44db9539804065e04d9c6850ae911c068b723d3", "2.5.38--h91ae1e9_0": "sha256:9f943f4c5c10e4017da77ede652df4b920858fcdc9926a077b426b4fbad18d2a", "2.5.60--h0705fce_0": "sha256:b670b6db8c9eca3d1ff98cfe570b2be953c7bfa2de0abbfb10638d6a16ff9dc3", "2.5.61--h0705fce_0": "sha256:8e61391e27896771fee920c536a432afb3082a088256388f0f8c57a149276505", "2.5.62--h0705fce_0": "sha256:30c12f7c985c372db8296c8eba88e27ecdd98bf7c07da23210265cd379128e41", "2.5.62--h0d74fca_1": "sha256:c1334ec0cb099fd3eeadd070a4bebe90d89d9e9ba9dcbebdff85013fc6403a07", "2.5.63--h0d74fca_0": "sha256:89c67de33a8e24b2d2edf699b6be04b3698801a58de30f90d63d239cafb05271"}, "docker": "quay.io/biocontainers/hyphy"}
---

This module is a singularity container wrapper for quay.io/biocontainers/hyphy.
shpc-registry automated BioContainers addition for hyphy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hyphy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hyphy:2.5.63--h0d74fca_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hyphy/2.5.63--h0d74fca_0
$ module help quay.io/biocontainers/hyphy/2.5.63--h0d74fca_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hyphy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hyphy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hyphy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hyphy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hyphy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hyphy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### hyphy

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