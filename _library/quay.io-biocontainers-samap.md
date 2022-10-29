---
layout: container
name:  "quay.io/biocontainers/samap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samap/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/samap/container.yaml"
updated_at: "2022-10-29 05:46:49.026932"
latest: "1.0.7--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/samap"
aliases:
 - "scalar"
 - "2to3-3.7"
 - "brotli"
 - "cmpfillin"
 - "docutils"
 - "dunamai"
 - "f2py3.7"
 - "fonttools"
 - "get_objgraph"
 - "gif2h5"
 - "git"
versions:
 - "1.0.7--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for samap"
config: {"url": "https://biocontainers.pro/tools/samap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samap", "latest": {"1.0.7--pyhdfd78af_0": "sha256:93a5196803174d1ec72294bdbd01c00d002ab37bb9ff1b4de85757861545f3c5"}, "tags": {"1.0.7--pyhdfd78af_0": "sha256:93a5196803174d1ec72294bdbd01c00d002ab37bb9ff1b4de85757861545f3c5"}, "docker": "quay.io/biocontainers/samap", "aliases": {"scalar": "/usr/local/bin/scalar", "2to3-3.7": "/usr/local/bin/2to3-3.7", "brotli": "/usr/local/bin/brotli", "cmpfillin": "/usr/local/bin/cmpfillin", "docutils": "/usr/local/bin/docutils", "dunamai": "/usr/local/bin/dunamai", "f2py3.7": "/usr/local/bin/f2py3.7", "fonttools": "/usr/local/bin/fonttools", "get_objgraph": "/usr/local/bin/get_objgraph", "gif2h5": "/usr/local/bin/gif2h5", "git": "/usr/local/bin/git"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samap.
shpc-registry automated BioContainers addition for samap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samap:1.0.7--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samap/1.0.7--pyhdfd78af_0
$ module help quay.io/biocontainers/samap/1.0.7--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scalar

```bash
$ singularity exec <container> /usr/local/bin/scalar
$ podman run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scalar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dunamai

```bash
$ singularity exec <container> /usr/local/bin/dunamai
$ podman run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dunamai   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git

```bash
$ singularity exec <container> /usr/local/bin/git
$ podman run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git   -v ${PWD} -w ${PWD} <container> -c " $@"
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