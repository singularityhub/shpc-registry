---
layout: container
name:  "quay.io/biocontainers/scar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scar/container.yaml"
updated_at: "2025-04-11 03:15:37.588938"
latest: "0.7.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/scar"
aliases:
 - "scar"
 - "torchrun"
 - "scanpy"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "ninja"
 - "docutils"
 - "google-oauthlib-tool"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
versions:
 - "0.4.4--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.5.1--pyhdfd78af_0"
 - "0.5.2--pyhdfd78af_0"
 - "0.6.0--pyhdfd78af_0"
 - "0.5.5--pyhdfd78af_0"
 - "0.7.0--pyhdfd78af_0"
 - "0.6.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for scar"
config: {"url": "https://biocontainers.pro/tools/scar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scar", "latest": {"0.7.0--pyhdfd78af_0": "sha256:7d2dbda2d1119abeeecbb82d92891143a850479e338917fd8593a28d32ce24c9"}, "tags": {"0.4.4--pyhdfd78af_0": "sha256:abd805f097d4f9316cf1aae47187af07d341771d351117d7ab2492068adff903", "0.5.0--pyhdfd78af_0": "sha256:65a0a57d21da302a03bba8fce7a48c05c70e54f22b0f311967a1e1ed6a74b4c5", "0.5.1--pyhdfd78af_0": "sha256:c20f9ba2f77364bb8ffbd239d98dbf28eb3e0658cd480dc9e2114dbfe2e45640", "0.5.2--pyhdfd78af_0": "sha256:991fbd4dd83bf1482ae78bcc6740e98de7c8672b32c3a611cc86500e40a16f59", "0.6.0--pyhdfd78af_0": "sha256:3b88414d6bdfc2d7fec1766ce71ff814afb1a9b3b942395a902f09a5042a3037", "0.5.5--pyhdfd78af_0": "sha256:0730022d96a4c8f6a48b237108fc3bd0ea3bc115eb57495bb00a5fc416695feb", "0.7.0--pyhdfd78af_0": "sha256:7d2dbda2d1119abeeecbb82d92891143a850479e338917fd8593a28d32ce24c9", "0.6.1--pyhdfd78af_0": "sha256:6e930ad6714d7576eec8d7fb8f802d2bf6be557b461f29786f9db446accc6f3d"}, "docker": "quay.io/biocontainers/scar", "aliases": {"scar": "/usr/local/bin/scar", "torchrun": "/usr/local/bin/torchrun", "scanpy": "/usr/local/bin/scanpy", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "ninja": "/usr/local/bin/ninja", "docutils": "/usr/local/bin/docutils", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scar.
shpc-registry automated BioContainers addition for scar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scar:0.7.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scar/0.7.0--pyhdfd78af_0
$ module help quay.io/biocontainers/scar/0.7.0--pyhdfd78af_0
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


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ninja

```bash
$ singularity exec <container> /usr/local/bin/ninja
$ podman run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ninja   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docutils

```bash
$ singularity exec <container> /usr/local/bin/docutils
$ podman run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docutils   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### grpc_csharp_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_csharp_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_csharp_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_node_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_node_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_node_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_objective_c_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_objective_c_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_objective_c_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
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