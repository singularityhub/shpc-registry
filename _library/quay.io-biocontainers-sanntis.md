---
layout: container
name:  "quay.io/biocontainers/sanntis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sanntis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sanntis/container.yaml"
updated_at: "2025-05-03 03:49:02.339847"
latest: "0.9.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sanntis"
aliases:
 - "import_pb_to_tensorboard"
 - "sanntis"
 - "sanntis_build_gb"
 - "estimator_ckpt_converter"
 - "google-oauthlib-tool"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
 - "grpc_ruby_plugin"
 - "jpackage"
 - "tf_upgrade_v2"
 - "tflite_convert"
 - "saved_model_cli"
 - "toco"
 - "toco_from_protos"
 - "tensorboard"
 - "cups-config"
 - "ippeveprinter"
 - "ipptool"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
 - "pyrsa-sign"
 - "pyrsa-verify"
versions:
 - "0.9.1--pyhdfd78af_0"
 - "0.9.3.2--pyhdfd78af_0"
 - "0.9.3.4--pyhdfd78af_0"
 - "0.9.3.5--pyhdfd78af_0"
 - "0.9.3.5--pyhdfd78af_1"
 - "0.9.4.0--pyhdfd78af_0"
 - "0.9.4.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for sanntis"
config: {"url": "https://biocontainers.pro/tools/sanntis", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sanntis", "latest": {"0.9.4.1--pyhdfd78af_0": "sha256:5ede775962fbc1b54599933b74a74190aa91d8b545b083c606cd14764abba5fd"}, "tags": {"0.9.1--pyhdfd78af_0": "sha256:f27c88b4d1cef391ab29b6c4a4c7fa8f0dce0f3aa79b98cff069d102aef229fa", "0.9.3.2--pyhdfd78af_0": "sha256:d06dc49982786e600ebffdbd248790d242f8c7067d55eaa3357fedd9140d119e", "0.9.3.4--pyhdfd78af_0": "sha256:37d8325a377b6825950fa9d62b35386532ff7946b4fe9ce3209d2133236e1ef8", "0.9.3.5--pyhdfd78af_0": "sha256:5335adff49cd176a753ad1759a706d2a0da68fc0b4486bb4c2c5def05e7936eb", "0.9.3.5--pyhdfd78af_1": "sha256:e1c4a73873faf227651e17ed569a58cdf2927e9f14434236bb506e4310ee4048", "0.9.4.0--pyhdfd78af_0": "sha256:3ccc7f45a7483cd4361992fb7b82af009a62993dbda79131910107cdd55672ce", "0.9.4.1--pyhdfd78af_0": "sha256:5ede775962fbc1b54599933b74a74190aa91d8b545b083c606cd14764abba5fd"}, "docker": "quay.io/biocontainers/sanntis", "aliases": {"import_pb_to_tensorboard": "/usr/local/bin/import_pb_to_tensorboard", "sanntis": "/usr/local/bin/sanntis", "sanntis_build_gb": "/usr/local/bin/sanntis_build_gb", "estimator_ckpt_converter": "/usr/local/bin/estimator_ckpt_converter", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin", "grpc_ruby_plugin": "/usr/local/bin/grpc_ruby_plugin", "jpackage": "/usr/local/bin/jpackage", "tf_upgrade_v2": "/usr/local/bin/tf_upgrade_v2", "tflite_convert": "/usr/local/bin/tflite_convert", "saved_model_cli": "/usr/local/bin/saved_model_cli", "toco": "/usr/local/bin/toco", "toco_from_protos": "/usr/local/bin/toco_from_protos", "tensorboard": "/usr/local/bin/tensorboard", "cups-config": "/usr/local/bin/cups-config", "ippeveprinter": "/usr/local/bin/ippeveprinter", "ipptool": "/usr/local/bin/ipptool", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub", "pyrsa-sign": "/usr/local/bin/pyrsa-sign", "pyrsa-verify": "/usr/local/bin/pyrsa-verify"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sanntis.
singularity registry hpc automated addition for sanntis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sanntis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sanntis:0.9.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sanntis/0.9.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/sanntis/0.9.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sanntis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sanntis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sanntis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sanntis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sanntis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sanntis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### import_pb_to_tensorboard

```bash
$ singularity exec <container> /usr/local/bin/import_pb_to_tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sanntis

```bash
$ singularity exec <container> /usr/local/bin/sanntis
$ podman run --it --rm --entrypoint /usr/local/bin/sanntis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sanntis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sanntis_build_gb

```bash
$ singularity exec <container> /usr/local/bin/sanntis_build_gb
$ podman run --it --rm --entrypoint /usr/local/bin/sanntis_build_gb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sanntis_build_gb   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### grpc_php_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_php_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_php_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_python_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_python_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_python_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grpc_ruby_plugin

```bash
$ singularity exec <container> /usr/local/bin/grpc_ruby_plugin
$ podman run --it --rm --entrypoint /usr/local/bin/grpc_ruby_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grpc_ruby_plugin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tf_upgrade_v2

```bash
$ singularity exec <container> /usr/local/bin/tf_upgrade_v2
$ podman run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### toco_from_protos

```bash
$ singularity exec <container> /usr/local/bin/toco_from_protos
$ podman run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toco_from_protos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tensorboard

```bash
$ singularity exec <container> /usr/local/bin/tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ippeveprinter

```bash
$ singularity exec <container> /usr/local/bin/ippeveprinter
$ podman run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ippeveprinter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipptool

```bash
$ singularity exec <container> /usr/local/bin/ipptool
$ podman run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipptool   -v ${PWD} -w ${PWD} <container> -c " $@"
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