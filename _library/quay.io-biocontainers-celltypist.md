---
layout: container
name:  "quay.io/biocontainers/celltypist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/celltypist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/celltypist/container.yaml"
updated_at: "2023-10-28 02:37:25.465430"
latest: "1.6.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/celltypist"
aliases:
 - "celltypist"
 - "scanpy"
 - "docutils"
 - "igraph"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "pybabel"
 - "cmpfillin"
 - "gpmetis"
versions:
 - "1.2.0--pyhdfd78af_0"
 - "1.3.0--pyhdfd78af_0"
 - "1.5.0--pyhdfd78af_0"
 - "1.5.2--pyhdfd78af_0"
 - "1.6.0--pyhdfd78af_0"
 - "1.5.3--pyhdfd78af_1"
 - "1.6.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for celltypist"
config: {"url": "https://biocontainers.pro/tools/celltypist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for celltypist", "latest": {"1.6.1--pyhdfd78af_0": "sha256:b657426499d1f1dca3d8516181621ec671f145460725cb518418ed457b1daaf8"}, "tags": {"1.2.0--pyhdfd78af_0": "sha256:0ff91df0cb1b0635c7a1969f4ac54943329c4252cd73bb79fbfefef4207c37f6", "1.3.0--pyhdfd78af_0": "sha256:e5e359cf8ce142ac0f8d020a56cca75ad2f5342a5758f4ff0dcbdaed976cf24d", "1.5.0--pyhdfd78af_0": "sha256:667052924ab7865b32aaa8d6a7342c01a30207c9cb6611580873abe8860d40b3", "1.5.2--pyhdfd78af_0": "sha256:dffabc16e9c64f9150ba98d6c913f6f7a27a188b61fffaa79c20678e6b4ec509", "1.6.0--pyhdfd78af_0": "sha256:c376f6305fe8ea34cbc404e1b287b95e8692323cca6c28706cfbe8afea585e27", "1.5.3--pyhdfd78af_1": "sha256:38b1b851a805df6e8c9ca31347cc2a320eabd393237ba48efcde2a649ed58415", "1.6.1--pyhdfd78af_0": "sha256:b657426499d1f1dca3d8516181621ec671f145460725cb518418ed457b1daaf8"}, "docker": "quay.io/biocontainers/celltypist", "aliases": {"celltypist": "/usr/local/bin/celltypist", "scanpy": "/usr/local/bin/scanpy", "docutils": "/usr/local/bin/docutils", "igraph": "/usr/local/bin/igraph", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "pybabel": "/usr/local/bin/pybabel", "cmpfillin": "/usr/local/bin/cmpfillin", "gpmetis": "/usr/local/bin/gpmetis"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/celltypist.
shpc-registry automated BioContainers addition for celltypist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/celltypist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/celltypist:1.6.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/celltypist/1.6.1--pyhdfd78af_0
$ module help quay.io/biocontainers/celltypist/1.6.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### celltypist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### celltypist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### celltypist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### celltypist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### celltypist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### celltypist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### celltypist

```bash
$ singularity exec <container> /usr/local/bin/celltypist
$ podman run --it --rm --entrypoint /usr/local/bin/celltypist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/celltypist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
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