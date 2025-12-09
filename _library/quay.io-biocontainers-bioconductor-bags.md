---
layout: container
name:  "quay.io/biocontainers/bioconductor-bags"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bags/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bags/container.yaml"
updated_at: "2025-12-09 03:53:16.866863"
latest: "2.46.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bags"

versions:
 - "2.34.0--r41hc0cfd56_2"
 - "2.38.0--r42hc0cfd56_0"
 - "2.38.0--r42ha9d7317_1"
 - "2.40.0--r43ha9d7317_0"
 - "2.42.0--r43ha9d7317_0"
 - "2.46.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bags"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bags", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bags", "latest": {"2.46.0--r44h3df3fcb_0": "sha256:60d7bb0ada10983fc3facc6695ced0116a23d450ccab80b678ae875cb02e66d6"}, "tags": {"2.34.0--r41hc0cfd56_2": "sha256:e19834e60b160acce84abf426a9144ee909129a362e5ef856ca556fb86417ca1", "2.38.0--r42hc0cfd56_0": "sha256:a9ee479894d37901b0455ea21d59e9379d1ee04a81a7765079e48e686319bd07", "2.38.0--r42ha9d7317_1": "sha256:4e4b17bafd7a04fbd9e6f670c429a41c8e2416fd2344d727105d1e3037f415f4", "2.40.0--r43ha9d7317_0": "sha256:59f4c804e0315574096c984f142eb44a228580f2983c618a2e104d16e31bd24c", "2.42.0--r43ha9d7317_0": "sha256:a59a146b588d36f2db9331dcb6e08dc2cefcea8ed4193ebb4f862d7f95be182b", "2.46.0--r44h3df3fcb_0": "sha256:60d7bb0ada10983fc3facc6695ced0116a23d450ccab80b678ae875cb02e66d6"}, "docker": "quay.io/biocontainers/bioconductor-bags"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bags.
shpc-registry automated BioContainers addition for bioconductor-bags
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bags
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bags:2.46.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bags/2.46.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-bags/2.46.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bags-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bags-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bags-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bags-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bags-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bags-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bags

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