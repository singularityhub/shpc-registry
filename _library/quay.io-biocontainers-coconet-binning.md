---
layout: container
name:  "quay.io/biocontainers/coconet-binning"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/coconet-binning/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/coconet-binning/container.yaml"
updated_at: "2022-10-29 05:31:27.608168"
latest: "1.1.0--py_0"
container_url: "https://biocontainers.pro/tools/coconet-binning"
aliases:
 - "coconet"
 - "2to3-3.7"
 - "chardetect"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "cygdb"
 - "cython"
 - "cythonize"
 - "doesitcache"
 - "f2py3.7"
 - "gif2h5"
versions:
 - "1.1.0--py_0"
description: "shpc-registry automated BioContainers addition for coconet-binning"
config: {"url": "https://biocontainers.pro/tools/coconet-binning", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for coconet-binning", "latest": {"1.1.0--py_0": "sha256:a6f0996c05cb22d39afc382b114ee1ea528c6e2421a711d51a1a73f0d59de8da"}, "tags": {"1.1.0--py_0": "sha256:a6f0996c05cb22d39afc382b114ee1ea528c6e2421a711d51a1a73f0d59de8da"}, "docker": "quay.io/biocontainers/coconet-binning", "aliases": {"coconet": "/usr/local/bin/coconet", "2to3-3.7": "/usr/local/bin/2to3-3.7", "chardetect": "/usr/local/bin/chardetect", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "cygdb": "/usr/local/bin/cygdb", "cython": "/usr/local/bin/cython", "cythonize": "/usr/local/bin/cythonize", "doesitcache": "/usr/local/bin/doesitcache", "f2py3.7": "/usr/local/bin/f2py3.7", "gif2h5": "/usr/local/bin/gif2h5"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/coconet-binning.
shpc-registry automated BioContainers addition for coconet-binning
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/coconet-binning
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/coconet-binning:1.1.0--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/coconet-binning/1.1.0--py_0
$ module help quay.io/biocontainers/coconet-binning/1.1.0--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### coconet-binning-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### coconet-binning-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### coconet-binning-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### coconet-binning-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### coconet-binning-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### coconet-binning-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### coconet

```bash
$ singularity exec <container> /usr/local/bin/coconet
$ podman run --it --rm --entrypoint /usr/local/bin/coconet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coconet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-caffe2-to-onnx

```bash
$ singularity exec <container> /usr/local/bin/convert-caffe2-to-onnx
$ podman run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-caffe2-to-onnx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert-onnx-to-caffe2

```bash
$ singularity exec <container> /usr/local/bin/convert-onnx-to-caffe2
$ podman run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert-onnx-to-caffe2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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