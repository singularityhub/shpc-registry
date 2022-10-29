---
layout: container
name:  "quay.io/biocontainers/hitac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hitac/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hitac/container.yaml"
updated_at: "2022-10-29 05:53:57.538017"
latest: "2.0.9--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/hitac"
aliases:
 - "hiclass"
 - "brotli"
 - "cwebp"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "doesitcache"
 - "dwebp"
 - "f2py3.9"
 - "fonttools"
 - "gif2h5"
versions:
 - "2.0.9--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for hitac"
config: {"url": "https://biocontainers.pro/tools/hitac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hitac", "latest": {"2.0.9--pyhdfd78af_1": "sha256:93e8fbf4c59aec2d7144867b2ccf5efb3d8895de6a1cdd25aec13f077536fdd4"}, "tags": {"2.0.9--pyhdfd78af_1": "sha256:93e8fbf4c59aec2d7144867b2ccf5efb3d8895de6a1cdd25aec13f077536fdd4"}, "docker": "quay.io/biocontainers/hitac", "aliases": {"hiclass": "/usr/local/bin/hiclass", "brotli": "/usr/local/bin/brotli", "cwebp": "/usr/local/bin/cwebp", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "doesitcache": "/usr/local/bin/doesitcache", "dwebp": "/usr/local/bin/dwebp", "f2py3.9": "/usr/local/bin/f2py3.9", "fonttools": "/usr/local/bin/fonttools", "gif2h5": "/usr/local/bin/gif2h5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hitac.
shpc-registry automated BioContainers addition for hitac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hitac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hitac:2.0.9--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hitac/2.0.9--pyhdfd78af_1
$ module help quay.io/biocontainers/hitac/2.0.9--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hitac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hitac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hitac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hitac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hitac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hitac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hiclass

```bash
$ singularity exec <container> /usr/local/bin/hiclass
$ podman run --it --rm --entrypoint /usr/local/bin/hiclass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hiclass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cygdb

```bash
$ singularity exec <container> /usr/local/bin/cygdb
$ podman run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cygdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cython

```bash
$ singularity exec <container> /usr/local/bin/cython
$ podman run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cython   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cythonize

```bash
$ singularity exec <container> /usr/local/bin/cythonize
$ podman run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cythonize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### doesitcache

```bash
$ singularity exec <container> /usr/local/bin/doesitcache
$ podman run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/doesitcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
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