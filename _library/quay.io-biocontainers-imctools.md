---
layout: container
name:  "quay.io/biocontainers/imctools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/imctools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/imctools/container.yaml"
updated_at: "2022-10-29 05:52:26.174840"
latest: "1.0.8--pyh864c0ab_0"
container_url: "https://biocontainers.pro/tools/imctools"
aliases:
 - "2to3-3.8"
 - "JxrDecApp"
 - "JxrEncApp"
 - "aec"
 - "brotli"
 - "cbrunsli"
 - "dbrunsli"
 - "f2py3.8"
 - "gif2rgb"
 - "gifbuild"
versions:
 - "1.0.8--pyh864c0ab_0"
description: "shpc-registry automated BioContainers addition for imctools"
config: {"url": "https://biocontainers.pro/tools/imctools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for imctools", "latest": {"1.0.8--pyh864c0ab_0": "sha256:89d3f1aa39091eb9a79f1084c99eb2d64f248bb5c4aee9d868e85c1ccf64498f"}, "tags": {"1.0.8--pyh864c0ab_0": "sha256:89d3f1aa39091eb9a79f1084c99eb2d64f248bb5c4aee9d868e85c1ccf64498f"}, "docker": "quay.io/biocontainers/imctools", "aliases": {"2to3-3.8": "/usr/local/bin/2to3-3.8", "JxrDecApp": "/usr/local/bin/JxrDecApp", "JxrEncApp": "/usr/local/bin/JxrEncApp", "aec": "/usr/local/bin/aec", "brotli": "/usr/local/bin/brotli", "cbrunsli": "/usr/local/bin/cbrunsli", "dbrunsli": "/usr/local/bin/dbrunsli", "f2py3.8": "/usr/local/bin/f2py3.8", "gif2rgb": "/usr/local/bin/gif2rgb", "gifbuild": "/usr/local/bin/gifbuild"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/imctools.
shpc-registry automated BioContainers addition for imctools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/imctools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/imctools:1.0.8--pyh864c0ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/imctools/1.0.8--pyh864c0ab_0
$ module help quay.io/biocontainers/imctools/1.0.8--pyh864c0ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### imctools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### imctools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### imctools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### imctools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### imctools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### imctools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrDecApp

```bash
$ singularity exec <container> /usr/local/bin/JxrDecApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrEncApp

```bash
$ singularity exec <container> /usr/local/bin/JxrEncApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aec

```bash
$ singularity exec <container> /usr/local/bin/aec
$ podman run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbrunsli

```bash
$ singularity exec <container> /usr/local/bin/cbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbrunsli

```bash
$ singularity exec <container> /usr/local/bin/dbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifbuild

```bash
$ singularity exec <container> /usr/local/bin/gifbuild
$ podman run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
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