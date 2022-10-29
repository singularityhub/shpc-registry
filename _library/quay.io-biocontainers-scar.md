---
layout: container
name:  "quay.io/biocontainers/scar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scar/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scar/container.yaml"
updated_at: "2022-10-29 05:30:37.635396"
latest: "0.4.4--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/scar"
aliases:
 - "scar"
 - "2to3-3.9"
 - "brotli"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "docutils"
 - "f2py3.9"
 - "fonttools"
 - "gif2h5"
 - "google-oauthlib-tool"
 - "grpc_cpp_plugin"
versions:
 - "0.4.4--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for scar"
config: {"url": "https://biocontainers.pro/tools/scar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scar", "latest": {"0.4.4--pyhdfd78af_0": "sha256:abd805f097d4f9316cf1aae47187af07d341771d351117d7ab2492068adff903"}, "tags": {"0.4.4--pyhdfd78af_0": "sha256:abd805f097d4f9316cf1aae47187af07d341771d351117d7ab2492068adff903"}, "docker": "quay.io/biocontainers/scar", "aliases": {"scar": "/usr/local/bin/scar", "2to3-3.9": "/usr/local/bin/2to3-3.9", "brotli": "/usr/local/bin/brotli", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "docutils": "/usr/local/bin/docutils", "f2py3.9": "/usr/local/bin/f2py3.9", "fonttools": "/usr/local/bin/fonttools", "gif2h5": "/usr/local/bin/gif2h5", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scar.
shpc-registry automated BioContainers addition for scar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scar:0.4.4--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scar/0.4.4--pyhdfd78af_0
$ module help quay.io/biocontainers/scar/0.4.4--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scar

```bash
$ singularity exec <container> /usr/local/bin/scar
$ podman run --it --rm --entrypoint /usr/local/bin/scar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_cpp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_cpp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_cpp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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