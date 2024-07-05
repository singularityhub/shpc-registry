---
layout: container
name:  "quay.io/biocontainers/ncbi-vdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-vdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-vdb/container.yaml"
updated_at: "2024-07-05 03:06:33.817219"
latest: "3.1.1--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/ncbi-vdb"

versions:
 - "3.0.0--pl5321h87f3376_0"
 - "3.0.2--h87f3376_0"
 - "3.0.5--h87f3376_0"
 - "3.0.5--hdbdd923_2"
 - "3.0.6--hdbdd923_0"
 - "3.0.7--hdbdd923_0"
 - "3.0.8--hdbdd923_0"
 - "3.0.9--hdbdd923_0"
 - "3.0.10--hdbdd923_0"
 - "3.1.0--hdbdd923_0"
 - "3.1.0--h4ac6f70_2"
 - "3.1.1--h4ac6f70_0"
description: "shpc-registry automated BioContainers addition for ncbi-vdb"
config: {"url": "https://biocontainers.pro/tools/ncbi-vdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncbi-vdb", "latest": {"3.1.1--h4ac6f70_0": "sha256:b852f80b46cb35d4bbbc23419e16980fc4c410c87b0735e055a48e08398bf5b2"}, "tags": {"3.0.0--pl5321h87f3376_0": "sha256:3b6375b7218a284bb56576729f38aa69f5a0ee208535f90fbfbc21022e71057d", "3.0.2--h87f3376_0": "sha256:aba43c21a8b43784d533b628aa938ea862735e780bdefbfbc38874fc747644bb", "3.0.5--h87f3376_0": "sha256:6fdeb8dac5974c888aa8c986af7709da148127d749e1998588b47ddc922f2c8a", "3.0.5--hdbdd923_2": "sha256:7fbaa66b85908c236f293990058119f1be03a45ac71d7818d4ec2b3015a523d0", "3.0.6--hdbdd923_0": "sha256:c6e72eb236d94a9d3912ecdf5a6a2214b2540e28901264efb591fa726d6a94b3", "3.0.7--hdbdd923_0": "sha256:57ddf224432db34055d6c54c386a4c59aae2b3cc2f6c6e7fadf59640699c79f7", "3.0.8--hdbdd923_0": "sha256:daad465684c05c71ae2592a6d32627333f8b34511592025f2c3c2ddb33408801", "3.0.9--hdbdd923_0": "sha256:4d64164c398e63672f870dcffc3dd9ab2d67e0dee6caf2da9f4b7dcdc5126ca4", "3.0.10--hdbdd923_0": "sha256:06de6ae7a5acd4f7fcfede5633d1deed8b61812768fd66cf366e6fee7cd73664", "3.1.0--hdbdd923_0": "sha256:c6e348844b1917d257d9a8d3361124c0884d941777069072a891dae9fc3f264b", "3.1.0--h4ac6f70_2": "sha256:61a1f45e088b3986aef0b10a6e704b5bff0a4fe0355bf8032e01b8e5b700805b", "3.1.1--h4ac6f70_0": "sha256:b852f80b46cb35d4bbbc23419e16980fc4c410c87b0735e055a48e08398bf5b2"}, "docker": "quay.io/biocontainers/ncbi-vdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-vdb.
shpc-registry automated BioContainers addition for ncbi-vdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-vdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-vdb:3.1.1--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-vdb/3.1.1--h4ac6f70_0
$ module help quay.io/biocontainers/ncbi-vdb/3.1.1--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-vdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-vdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-vdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-vdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-vdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-vdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ncbi-vdb

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