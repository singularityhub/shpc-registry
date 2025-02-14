---
layout: container
name:  "quay.io/biocontainers/bioconductor-clipper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-clipper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-clipper/container.yaml"
updated_at: "2025-02-14 03:18:25.608141"
latest: "1.46.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-clipper"
aliases:
 - "glpsol"
versions:
 - "1.34.0--r41hc247a5b_2"
 - "1.38.0--r42hc247a5b_0"
 - "1.38.0--r42hf17093f_1"
 - "1.40.0--r43hf17093f_0"
 - "1.42.0--r43hf17093f_0"
 - "1.46.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-clipper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-clipper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-clipper", "latest": {"1.46.0--r44he5774e6_0": "sha256:9345a7a45ed4c8efbda93b52473958f24b40982533bb2fdb23ba63d40f1716e0"}, "tags": {"1.34.0--r41hc247a5b_2": "sha256:af25fa54acf82e3fe612e1cd3f4b918869e853f72293382407dd5e26831581a6", "1.38.0--r42hc247a5b_0": "sha256:61ee1f0761e526de95824c67bc437a3c5f6d6c7e7b5bc5276cf5a5e01cd3cf28", "1.38.0--r42hf17093f_1": "sha256:eef0423732423a4e590928ebdd8effa17932a8770056022f05d4d4d9c060a20d", "1.40.0--r43hf17093f_0": "sha256:d563da82ddf5706ebc2766699c069bea9bdc9ac3345cbf27e4c4f13949dca304", "1.42.0--r43hf17093f_0": "sha256:e20d54f6d3ebbfb2cc6b7c635e5e7814de4fe63b9057daa35fbbe0cbed9891dd", "1.46.0--r44he5774e6_0": "sha256:9345a7a45ed4c8efbda93b52473958f24b40982533bb2fdb23ba63d40f1716e0"}, "docker": "quay.io/biocontainers/bioconductor-clipper", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-clipper.
shpc-registry automated BioContainers addition for bioconductor-clipper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-clipper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-clipper:1.46.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-clipper/1.46.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-clipper/1.46.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-clipper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clipper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-clipper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-clipper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-clipper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-clipper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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