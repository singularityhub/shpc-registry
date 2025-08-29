---
layout: container
name:  "quay.io/biocontainers/atlas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/atlas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/atlas/container.yaml"
updated_at: "2025-08-29 03:38:49.883217"
latest: "2.0.0--hadca570_7"
container_url: "https://biocontainers.pro/tools/atlas"
aliases:
 - "atlas"
versions:
 - "0.9.9--h42556f1_1"
 - "0.9.9--h0bf65d5_3"
 - "2.0.0--h523fec3_0"
 - "2.0.0--h48c1dbe_1"
 - "2.0.0--h48c1dbe_2"
 - "2.0.0--h48c1dbe_3"
 - "2.0.0--hbb3d6a8_5"
 - "2.0.0--hadca570_7"
description: "shpc-registry automated BioContainers addition for atlas"
config: {"url": "https://biocontainers.pro/tools/atlas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for atlas", "latest": {"2.0.0--hadca570_7": "sha256:a64baaf1e2943a4925752acc63677784ecbb8da239b592455405b819437fe206"}, "tags": {"0.9.9--h42556f1_1": "sha256:b356e7fa38d7c7a1cb110479105437c32084a33fedeebfe58c9d8f37fdc50383", "0.9.9--h0bf65d5_3": "sha256:a67db52475ff46c2debb1eb5704f001b1e1130aeca1d12ceb8ed6884d78e50a1", "2.0.0--h523fec3_0": "sha256:76e66fb197ec9cc664427d47650c891b14ce2ba87a14396a68fa6122ba6d449c", "2.0.0--h48c1dbe_1": "sha256:7bc2d77ea409ce6d49e2434d2acc82f5787384942e13a1cc87319d8eb522322b", "2.0.0--h48c1dbe_2": "sha256:f441ef01f768c0918e3e71610f2f39191133ef394bcef02089e6d4420799e5dc", "2.0.0--h48c1dbe_3": "sha256:2513f94d98f5bdcfc22516d490964ae4e567977cd81bbaaf53d050810c7d3ffa", "2.0.0--hbb3d6a8_5": "sha256:f6917b3182de0ea0d4de3b68bfd13a9360b29573b3a7b01c3d934f3e30322c6e", "2.0.0--hadca570_7": "sha256:a64baaf1e2943a4925752acc63677784ecbb8da239b592455405b819437fe206"}, "docker": "quay.io/biocontainers/atlas", "aliases": {"atlas": "/usr/local/bin/atlas"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/atlas.
shpc-registry automated BioContainers addition for atlas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/atlas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/atlas:2.0.0--hadca570_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/atlas/2.0.0--hadca570_7
$ module help quay.io/biocontainers/atlas/2.0.0--hadca570_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### atlas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### atlas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### atlas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### atlas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### atlas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### atlas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### atlas

```bash
$ singularity exec <container> /usr/local/bin/atlas
$ podman run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
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