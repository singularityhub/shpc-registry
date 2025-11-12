---
layout: container
name:  "quay.io/biocontainers/rmats"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rmats/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rmats/container.yaml"
updated_at: "2025-11-12 03:24:11.875029"
latest: "4.3.0--py311hf2f0b74_5"
container_url: "https://biocontainers.pro/tools/rmats"

versions:
 - "4.1.2--py27ha9cf2de_4"
 - "4.2.0--py310h2385082_0"
 - "4.1.2--py310h2385082_5"
 - "4.3.0--py310h2385082_0"
 - "4.3.0--py310h1918981_1"
 - "4.3.0--py312h090a2e0_2"
 - "4.3.0--py311h051dd6f_3"
 - "4.3.0--py312h090a2e0_4"
 - "4.3.0--py311hf2f0b74_5"
description: "shpc-registry automated BioContainers addition for rmats"
config: {"url": "https://biocontainers.pro/tools/rmats", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rmats", "latest": {"4.3.0--py311hf2f0b74_5": "sha256:95d9d3a338ca8895d35c0c6d19324d8c90110d62edbb8299bd5e6eff4df9a7f5"}, "tags": {"4.1.2--py27ha9cf2de_4": "sha256:fa9c99eee212bbb11275d6c19cb9a77667dcec12b70e46f39eef488b80007b41", "4.2.0--py310h2385082_0": "sha256:470aa164ed6ecc3715bf78ee9700b3e5659607faf99917a78a9a5def252a06ef", "4.1.2--py310h2385082_5": "sha256:ca1346fb4d436c9fb65f2c4bf64659422138c4acfaccc062142453367f49a767", "4.3.0--py310h2385082_0": "sha256:4a72065e959e1b1453eaf451d80108dc24842116335333c524bcdff01fdb68f0", "4.3.0--py310h1918981_1": "sha256:b8fe634ed63c51c83223c487c77fecdd0d8fd2eda57d07e6928fa437a49d927b", "4.3.0--py312h090a2e0_2": "sha256:c35cb45d2182188372176dd0f4e3ac397ffe20180c1d402e8803b9da74fb06d1", "4.3.0--py311h051dd6f_3": "sha256:ed81bb0c2a53a187f0a600a4f06af59e55ade245bd5505d298b86158af04fe3b", "4.3.0--py312h090a2e0_4": "sha256:a7a705e6c6f155ef0c9e8338d2109a699274cf18af9aaf3d4af6811ab4186410", "4.3.0--py311hf2f0b74_5": "sha256:95d9d3a338ca8895d35c0c6d19324d8c90110d62edbb8299bd5e6eff4df9a7f5"}, "docker": "quay.io/biocontainers/rmats"}
---

This module is a singularity container wrapper for quay.io/biocontainers/rmats.
shpc-registry automated BioContainers addition for rmats
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rmats
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rmats:4.3.0--py311hf2f0b74_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rmats/4.3.0--py311hf2f0b74_5
$ module help quay.io/biocontainers/rmats/4.3.0--py311hf2f0b74_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rmats-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rmats-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rmats-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rmats-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rmats-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rmats-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### rmats

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