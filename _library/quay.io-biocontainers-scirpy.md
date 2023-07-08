---
layout: container
name:  "quay.io/biocontainers/scirpy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scirpy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scirpy/container.yaml"
updated_at: "2023-07-08 03:22:43.781389"
latest: "0.12.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/scirpy"
aliases:
 - "airr-tools"
 - "dunamai"
 - "scanpy"
 - "igraph"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "pybabel"
 - "cmpfillin"
 - "gpmetis"
 - "graphchk"
versions:
 - "0.9.1--pyhdfd78af_0"
 - "0.11.1--pyhdfd78af_0"
 - "0.10.1--pyhdfd78af_0"
 - "0.11.2--pyhdfd78af_0"
 - "0.12.0--pyhdfd78af_0"
 - "0.12.1--pyhdfd78af_0"
 - "0.12.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for scirpy"
config: {"url": "https://biocontainers.pro/tools/scirpy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scirpy", "latest": {"0.12.2--pyhdfd78af_0": "sha256:f29afa55e31fc1ddcd5b891314357ef2fae110952a0e78a094fbf2bed77a52cf"}, "tags": {"0.9.1--pyhdfd78af_0": "sha256:b9c7892ee076733df38e6d66abacdce0a5900964a9391437cf5923d5afc89bd8", "0.11.1--pyhdfd78af_0": "sha256:111e7aa99a5e2acabfde209ea48930a61f2ff03545aaca3617d3e21c77bed890", "0.10.1--pyhdfd78af_0": "sha256:c151e600fbd6e13f091ac1664ab790c0c6ba01ebc07e2f2a136b558099d74c82", "0.11.2--pyhdfd78af_0": "sha256:d164e82da90a50a656cb1103d9fa39770ebd306cace80c65d827b1d086296943", "0.12.0--pyhdfd78af_0": "sha256:bf6f5950938b32dc493ac33333bc80eceaa26ee8ada95b80e2c4664088f00e2e", "0.12.1--pyhdfd78af_0": "sha256:5d4ea23990e56f19a3e15e2598402fe02a2a3cffcb59fd2e277facd9e54b9e94", "0.12.2--pyhdfd78af_0": "sha256:f29afa55e31fc1ddcd5b891314357ef2fae110952a0e78a094fbf2bed77a52cf"}, "docker": "quay.io/biocontainers/scirpy", "aliases": {"airr-tools": "/usr/local/bin/airr-tools", "dunamai": "/usr/local/bin/dunamai", "scanpy": "/usr/local/bin/scanpy", "igraph": "/usr/local/bin/igraph", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "pybabel": "/usr/local/bin/pybabel", "cmpfillin": "/usr/local/bin/cmpfillin", "gpmetis": "/usr/local/bin/gpmetis", "graphchk": "/usr/local/bin/graphchk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scirpy.
shpc-registry automated BioContainers addition for scirpy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scirpy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scirpy:0.12.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scirpy/0.12.2--pyhdfd78af_0
$ module help quay.io/biocontainers/scirpy/0.12.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scirpy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scirpy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scirpy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scirpy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scirpy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scirpy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### airr-tools

```bash
$ singularity exec <container> /usr/local/bin/airr-tools
$ podman run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dunamai

```bash
$ singularity exec <container> /usr/local/bin/dunamai
$ podman run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-build

```bash
$ singularity exec <container> /usr/local/bin/sphinx-build
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-quickstart

```bash
$ singularity exec <container> /usr/local/bin/sphinx-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpmetis

```bash
$ singularity exec <container> /usr/local/bin/gpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphchk

```bash
$ singularity exec <container> /usr/local/bin/graphchk
$ podman run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
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