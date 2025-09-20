---
layout: container
name:  "quay.io/biocontainers/parsnp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/parsnp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/parsnp/container.yaml"
updated_at: "2025-09-20 03:38:24.598610"
latest: "2.1.4--h077b44d_0"
container_url: "https://biocontainers.pro/tools/parsnp"
aliases:
 - "Phi"
 - "Profile"
 - "extend.py"
 - "harvesttools"
 - "logger.py"
 - "parsnp"
 - "template.ini"
 - "fastANI"
 - "raxmlHPC"
 - "raxmlHPC-AVX2"
 - "raxmlHPC-PTHREADS"
 - "raxmlHPC-PTHREADS-AVX2"
 - "raxmlHPC-PTHREADS-SSE3"
 - "raxmlHPC-SSE3"
 - "capnp"
 - "capnpc"
 - "capnpc-c++"
versions:
 - "1.7.4--hd03093a_1"
 - "1.7.4--hdcf5f25_2"
 - "2.0.2--hdcf5f25_0"
 - "2.0.3--hdcf5f25_0"
 - "2.0.4--hdcf5f25_0"
 - "2.0.5--hdcf5f25_0"
 - "2.0.6--hdcf5f25_0"
 - "2.1.1--hdcf5f25_0"
 - "2.1.1--h077b44d_1"
 - "2.1.3--h077b44d_0"
 - "2.1.4--h077b44d_0"
description: "shpc-registry automated BioContainers addition for parsnp"
config: {"url": "https://biocontainers.pro/tools/parsnp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for parsnp", "latest": {"2.1.4--h077b44d_0": "sha256:593e0288e807f9d1c727ebf3e5b8825e68d8808e9bfe372678b8e75b857ca8ec"}, "tags": {"1.7.4--hd03093a_1": "sha256:92ec26ccc5ad8c73fc010f9deb5594ce9e63874516ca12aad069988256fb5158", "1.7.4--hdcf5f25_2": "sha256:635ec260e74a45ba1a1c98361ca0a6426214cd1a4fbf2630160621110378033f", "2.0.2--hdcf5f25_0": "sha256:92f65467c9c98dee883cccf053b0846a6fd9b9a37cca30fe3fe3582017278850", "2.0.3--hdcf5f25_0": "sha256:b46999fb9842f183443dd6226b461c1d8074d4c1391c1f2b1e51cc20cee8f8b2", "2.0.4--hdcf5f25_0": "sha256:5d0b3ef0a891f7064db985564797a09e5dc0c7b3c009a11893f5a45f4f417408", "2.0.5--hdcf5f25_0": "sha256:d7954254f6af345c8c35e789a20683b4dd5eaceb2a20edd3d6a6dbd422d9479d", "2.0.6--hdcf5f25_0": "sha256:e5f2ff49ee20e1b31a064dcf8dd6b8792a6cbc8c37b1b8a98c738adfbe63a6d6", "2.1.1--hdcf5f25_0": "sha256:1dba3077c6bd87ba756b59df29159f61e529810f40043ef36c66f7316c8f7b53", "2.1.1--h077b44d_1": "sha256:c0f45b26811d475e82c5f23a000927966bbf3370f66681d9c48cb43c13fcebc5", "2.1.3--h077b44d_0": "sha256:754b84963ab966b8b4bd1615d2290d9c87e5988fec72808717b947f6cc0b9a8e", "2.1.4--h077b44d_0": "sha256:593e0288e807f9d1c727ebf3e5b8825e68d8808e9bfe372678b8e75b857ca8ec"}, "docker": "quay.io/biocontainers/parsnp", "aliases": {"Phi": "/usr/local/bin/Phi", "Profile": "/usr/local/bin/Profile", "extend.py": "/usr/local/bin/extend.py", "harvesttools": "/usr/local/bin/harvesttools", "logger.py": "/usr/local/bin/logger.py", "parsnp": "/usr/local/bin/parsnp", "template.ini": "/usr/local/bin/template.ini", "fastANI": "/usr/local/bin/fastANI", "raxmlHPC": "/usr/local/bin/raxmlHPC", "raxmlHPC-AVX2": "/usr/local/bin/raxmlHPC-AVX2", "raxmlHPC-PTHREADS": "/usr/local/bin/raxmlHPC-PTHREADS", "raxmlHPC-PTHREADS-AVX2": "/usr/local/bin/raxmlHPC-PTHREADS-AVX2", "raxmlHPC-PTHREADS-SSE3": "/usr/local/bin/raxmlHPC-PTHREADS-SSE3", "raxmlHPC-SSE3": "/usr/local/bin/raxmlHPC-SSE3", "capnp": "/usr/local/bin/capnp", "capnpc": "/usr/local/bin/capnpc", "capnpc-c++": "/usr/local/bin/capnpc-c++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/parsnp.
shpc-registry automated BioContainers addition for parsnp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/parsnp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/parsnp:2.1.4--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/parsnp/2.1.4--h077b44d_0
$ module help quay.io/biocontainers/parsnp/2.1.4--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parsnp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parsnp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parsnp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parsnp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parsnp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parsnp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Phi

```bash
$ singularity exec <container> /usr/local/bin/Phi
$ podman run --it --rm --entrypoint /usr/local/bin/Phi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Phi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Profile

```bash
$ singularity exec <container> /usr/local/bin/Profile
$ podman run --it --rm --entrypoint /usr/local/bin/Profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extend.py

```bash
$ singularity exec <container> /usr/local/bin/extend.py
$ podman run --it --rm --entrypoint /usr/local/bin/extend.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extend.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### harvesttools

```bash
$ singularity exec <container> /usr/local/bin/harvesttools
$ podman run --it --rm --entrypoint /usr/local/bin/harvesttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/harvesttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### logger.py

```bash
$ singularity exec <container> /usr/local/bin/logger.py
$ podman run --it --rm --entrypoint /usr/local/bin/logger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/logger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsnp

```bash
$ singularity exec <container> /usr/local/bin/parsnp
$ podman run --it --rm --entrypoint /usr/local/bin/parsnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### template.ini

```bash
$ singularity exec <container> /usr/local/bin/template.ini
$ podman run --it --rm --entrypoint /usr/local/bin/template.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/template.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-AVX2

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-AVX2
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-AVX2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-PTHREADS-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-PTHREADS-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-PTHREADS-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raxmlHPC-SSE3

```bash
$ singularity exec <container> /usr/local/bin/raxmlHPC-SSE3
$ podman run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raxmlHPC-SSE3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnp

```bash
$ singularity exec <container> /usr/local/bin/capnp
$ podman run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc

```bash
$ singularity exec <container> /usr/local/bin/capnpc
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### capnpc-c++

```bash
$ singularity exec <container> /usr/local/bin/capnpc-c++
$ podman run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/capnpc-c++   -v ${PWD} -w ${PWD} <container> -c " $@"
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