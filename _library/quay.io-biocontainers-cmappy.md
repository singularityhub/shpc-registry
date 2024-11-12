---
layout: container
name:  "quay.io/biocontainers/cmappy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cmappy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cmappy/container.yaml"
updated_at: "2024-11-12 03:31:03.657665"
latest: "4.0.1--py312h28adbb1_7"
container_url: "https://biocontainers.pro/tools/cmappy"
aliases:
 - "concat"
 - "gct2gctx"
 - "gctx2gct"
 - "subset"
 - "f2py3.6"
 - "normalizer"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
 - "python3.6m-config"
 - "pyvenv-3.6"
versions:
 - "4.0.1--py36h2ad2d48_3"
 - "4.0.1--py39h1f90b4d_5"
 - "4.0.1--py38h2494328_5"
 - "4.0.1--py38h2494328_6"
 - "4.0.1--py312h28adbb1_7"
description: "shpc-registry automated BioContainers addition for cmappy"
config: {"url": "https://biocontainers.pro/tools/cmappy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cmappy", "latest": {"4.0.1--py312h28adbb1_7": "sha256:180dccdfea0c1170648945db29cc22c897c06fd69271c37727b28fb5beb23ea5"}, "tags": {"4.0.1--py36h2ad2d48_3": "sha256:c9d662975bca8b6407f524713286ae2cbb87f0e1089c3542e1e21c250e7daa51", "4.0.1--py39h1f90b4d_5": "sha256:2d43fe3a3c5151dd9051204527337ca5224df23b3ea46433141784bf28b83398", "4.0.1--py38h2494328_5": "sha256:f3b752dd4e92b9661cac071c2ed6188d17177a44476fc28ece25407fa6c9836f", "4.0.1--py38h2494328_6": "sha256:b44120780f163ab2137fde06f78a3e1bd7223aa059c67f242f25f9a3ce9d4c6d", "4.0.1--py312h28adbb1_7": "sha256:180dccdfea0c1170648945db29cc22c897c06fd69271c37727b28fb5beb23ea5"}, "docker": "quay.io/biocontainers/cmappy", "aliases": {"concat": "/usr/local/bin/concat", "gct2gctx": "/usr/local/bin/gct2gctx", "gctx2gct": "/usr/local/bin/gctx2gct", "subset": "/usr/local/bin/subset", "f2py3.6": "/usr/local/bin/f2py3.6", "normalizer": "/usr/local/bin/normalizer", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m", "python3.6m-config": "/usr/local/bin/python3.6m-config", "pyvenv-3.6": "/usr/local/bin/pyvenv-3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cmappy.
shpc-registry automated BioContainers addition for cmappy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cmappy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cmappy:4.0.1--py312h28adbb1_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cmappy/4.0.1--py312h28adbb1_7
$ module help quay.io/biocontainers/cmappy/4.0.1--py312h28adbb1_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cmappy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cmappy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cmappy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cmappy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cmappy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cmappy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### concat

```bash
$ singularity exec <container> /usr/local/bin/concat
$ podman run --it --rm --entrypoint /usr/local/bin/concat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gct2gctx

```bash
$ singularity exec <container> /usr/local/bin/gct2gctx
$ podman run --it --rm --entrypoint /usr/local/bin/gct2gctx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gct2gctx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gctx2gct

```bash
$ singularity exec <container> /usr/local/bin/gctx2gct
$ podman run --it --rm --entrypoint /usr/local/bin/gctx2gct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gctx2gct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### subset

```bash
$ singularity exec <container> /usr/local/bin/subset
$ podman run --it --rm --entrypoint /usr/local/bin/subset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/subset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6m-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyvenv-3.6

```bash
$ singularity exec <container> /usr/local/bin/pyvenv-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyvenv-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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