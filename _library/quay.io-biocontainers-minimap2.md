---
layout: container
name:  "quay.io/biocontainers/minimap2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/minimap2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/minimap2/container.yaml"
updated_at: "2023-09-17 00:13:14.155711"
latest: "2.26--he4a0461_1"
container_url: "https://biocontainers.pro/tools/minimap2"

versions:
 - "2.9--1"
 - "2.24--h7132678_1"
 - "2.23--h5bf99c6_0"
 - "2.22--h5bf99c6_0"
 - "2.21--h5bf99c6_0"
 - "2.20--h5bf99c6_0"
 - "2.26--he4a0461_1"
 - "2.25--h7132678_0"
description: "shpc-registry automated BioContainers addition for minimap2"
config: {"url": "https://biocontainers.pro/tools/minimap2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for minimap2", "latest": {"2.26--he4a0461_1": "sha256:5eaf5622efda537f3a1694afc05cb1606a3afd2bc3fdf57984f65de7015d8441"}, "tags": {"2.9--1": "sha256:a5ffd15959aff0e491f88561c1c632db1048c23b3257d7f8bc32bf6c7a044b40", "2.24--h7132678_1": "sha256:1f23d5cfbefb25ef4f9a0ee5b4f78d3b6cb0b3c955028d80e1d8b00bc97e299a", "2.23--h5bf99c6_0": "sha256:9c92147fd11759b5fc8ae02689b80075a134fce6b8f206a0dd7708cf2513f14d", "2.22--h5bf99c6_0": "sha256:54bc2790ccb2c2c4c24e0f78a5bb9108a9cb9ad91b1c038193a9fa75ab8b71f4", "2.21--h5bf99c6_0": "sha256:0e5701f734cedfa87a664d3625042d72e4a27dc7b8a4c68f73c62b89458ab77c", "2.20--h5bf99c6_0": "sha256:8cc6619d3b914a84ea94cb8eb82ebe71ad109e9fc8a432daf0ce61dba22f0f42", "2.26--he4a0461_1": "sha256:5eaf5622efda537f3a1694afc05cb1606a3afd2bc3fdf57984f65de7015d8441", "2.25--h7132678_0": "sha256:09d9cecd5f84627b3a4151244a1c766089ab00dd9f6501da9fce3a36fb77f823"}, "docker": "quay.io/biocontainers/minimap2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/minimap2.
shpc-registry automated BioContainers addition for minimap2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/minimap2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/minimap2:2.26--he4a0461_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/minimap2/2.26--he4a0461_1
$ module help quay.io/biocontainers/minimap2/2.26--he4a0461_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### minimap2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### minimap2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### minimap2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### minimap2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### minimap2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### minimap2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### minimap2

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