---
layout: container
name:  "quay.io/biocontainers/varnet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/varnet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/varnet/container.yaml"
updated_at: "2026-10-10 19:29:29.406206"
latest: "1.5.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/varnet"
aliases:
 - "varnet-filter"
 - "varnet-predict"
 - "protoc-24.4.0"
 - "cffi-gen-src"
 - "flatc"
 - "import_pb_to_tensorboard"
 - "estimator_ckpt_converter"
 - "google-oauthlib-tool"
 - "tf_upgrade_v2"
 - "toco_from_protos"
 - "tflite_convert"
 - "saved_model_cli"
 - "toco"
 - "idna"
 - "tensorboard"
 - "h2benchmark"
 - "checksum-profile"
 - "markdown_py"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
 - "pyrsa-sign"
 - "pyrsa-verify"
 - "elasticurl"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
versions:
 - "1.5.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for varnet"
config: {"url": "https://biocontainers.pro/tools/varnet", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for varnet", "latest": {"1.5.3--pyhdfd78af_0": "sha256:8e38a1f5a72aec8c3fdcdb932c0660d65b306728376b9f3c3211b77f0ecef723"}, "tags": {"1.5.3--pyhdfd78af_0": "sha256:8e38a1f5a72aec8c3fdcdb932c0660d65b306728376b9f3c3211b77f0ecef723"}, "docker": "quay.io/biocontainers/varnet", "aliases": {"varnet-filter": "/usr/local/bin/varnet-filter", "varnet-predict": "/usr/local/bin/varnet-predict", "protoc-24.4.0": "/usr/local/bin/protoc-24.4.0", "cffi-gen-src": "/usr/local/bin/cffi-gen-src", "flatc": "/usr/local/bin/flatc", "import_pb_to_tensorboard": "/usr/local/bin/import_pb_to_tensorboard", "estimator_ckpt_converter": "/usr/local/bin/estimator_ckpt_converter", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "tf_upgrade_v2": "/usr/local/bin/tf_upgrade_v2", "toco_from_protos": "/usr/local/bin/toco_from_protos", "tflite_convert": "/usr/local/bin/tflite_convert", "saved_model_cli": "/usr/local/bin/saved_model_cli", "toco": "/usr/local/bin/toco", "idna": "/usr/local/bin/idna", "tensorboard": "/usr/local/bin/tensorboard", "h2benchmark": "/usr/local/bin/h2benchmark", "checksum-profile": "/usr/local/bin/checksum-profile", "markdown_py": "/usr/local/bin/markdown_py", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub", "pyrsa-sign": "/usr/local/bin/pyrsa-sign", "pyrsa-verify": "/usr/local/bin/pyrsa-verify", "elasticurl": "/usr/local/bin/elasticurl", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/varnet.
singularity registry hpc automated addition for varnet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/varnet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/varnet:1.5.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/varnet/1.5.3--pyhdfd78af_0
$ module help quay.io/biocontainers/varnet/1.5.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### varnet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### varnet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### varnet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### varnet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### varnet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### varnet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### varnet-filter

```bash
$ singularity exec <container> /usr/local/bin/varnet-filter
$ podman run --it --rm --entrypoint /usr/local/bin/varnet-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varnet-filter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varnet-predict

```bash
$ singularity exec <container> /usr/local/bin/varnet-predict
$ podman run --it --rm --entrypoint /usr/local/bin/varnet-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varnet-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-24.4.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-24.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-24.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-24.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flatc

```bash
$ singularity exec <container> /usr/local/bin/flatc
$ podman run --it --rm --entrypoint /usr/local/bin/flatc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flatc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### import_pb_to_tensorboard

```bash
$ singularity exec <container> /usr/local/bin/import_pb_to_tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estimator_ckpt_converter

```bash
$ singularity exec <container> /usr/local/bin/estimator_ckpt_converter
$ podman run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estimator_ckpt_converter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### google-oauthlib-tool

```bash
$ singularity exec <container> /usr/local/bin/google-oauthlib-tool
$ podman run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/google-oauthlib-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tf_upgrade_v2

```bash
$ singularity exec <container> /usr/local/bin/tf_upgrade_v2
$ podman run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco_from_protos

```bash
$ singularity exec <container> /usr/local/bin/toco_from_protos
$ podman run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tflite_convert

```bash
$ singularity exec <container> /usr/local/bin/tflite_convert
$ podman run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tflite_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### saved_model_cli

```bash
$ singularity exec <container> /usr/local/bin/saved_model_cli
$ podman run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/saved_model_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### toco

```bash
$ singularity exec <container> /usr/local/bin/toco
$ podman run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tensorboard

```bash
$ singularity exec <container> /usr/local/bin/tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown_py

```bash
$ singularity exec <container> /usr/local/bin/markdown_py
$ podman run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-keygen

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-priv2pub

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-priv2pub
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-sign

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-sign
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-sign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-sign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-verify

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-verify
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-verify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-verify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
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