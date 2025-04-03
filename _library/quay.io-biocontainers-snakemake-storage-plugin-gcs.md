---
layout: container
name:  "quay.io/biocontainers/snakemake-storage-plugin-gcs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-storage-plugin-gcs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-storage-plugin-gcs/container.yaml"
updated_at: "2025-04-03 03:24:21.810916"
latest: "1.1.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-storage-plugin-gcs"
aliases:
 - "protoc-24.4.0"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
 - "grpc_ruby_plugin"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
 - "pyrsa-sign"
 - "pyrsa-verify"
 - "protoc"
 - "normalizer"
versions:
 - "0.1.3--pyhdfd78af_0"
 - "0.1.4--pyhdfd78af_0"
 - "1.0.0--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_0"
 - "1.1.3--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-storage-plugin-gcs"
config: {"url": "https://biocontainers.pro/tools/snakemake-storage-plugin-gcs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-storage-plugin-gcs", "latest": {"1.1.3--pyhdfd78af_0": "sha256:10847bfdd10cd6e89f5a8f2fe7c0c60fb7b54e8b1ff2edbcbcb1680b6ab7cd74"}, "tags": {"0.1.3--pyhdfd78af_0": "sha256:54ce99bec39b26e088df29176519f677971eae61d26e71cc4d2624e2df205f10", "0.1.4--pyhdfd78af_0": "sha256:cbf27cdec6e2cca45c2d0042d662c03fd1f1e71301c5dbd486c3ed6052ee9bec", "1.0.0--pyhdfd78af_0": "sha256:142b8ffb456c00b046eda2208523b50dcc0d74954681c317b8343e304bc506b8", "1.1.1--pyhdfd78af_0": "sha256:ce69e4e5a85c0390bea8f4be352acc8af33729777a8e0f30e50c0b295032ceb7", "1.1.2--pyhdfd78af_0": "sha256:16dfb50ca33a93b5801a4071e6642360a84453676ba01ad4a3b794a6595aad3c", "1.1.3--pyhdfd78af_0": "sha256:10847bfdd10cd6e89f5a8f2fe7c0c60fb7b54e8b1ff2edbcbcb1680b6ab7cd74"}, "docker": "quay.io/biocontainers/snakemake-storage-plugin-gcs", "aliases": {"protoc-24.4.0": "/usr/local/bin/protoc-24.4.0", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin", "grpc_ruby_plugin": "/usr/local/bin/grpc_ruby_plugin", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub", "pyrsa-sign": "/usr/local/bin/pyrsa-sign", "pyrsa-verify": "/usr/local/bin/pyrsa-verify", "protoc": "/usr/local/bin/protoc", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-storage-plugin-gcs.
singularity registry hpc automated addition for snakemake-storage-plugin-gcs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-storage-plugin-gcs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-storage-plugin-gcs:1.1.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-storage-plugin-gcs/1.1.3--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-storage-plugin-gcs/1.1.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-storage-plugin-gcs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-storage-plugin-gcs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-storage-plugin-gcs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-storage-plugin-gcs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-storage-plugin-gcs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-storage-plugin-gcs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### protoc-24.4.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-24.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-24.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-24.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### protoc

```bash
$ singularity exec <container> /usr/local/bin/protoc
$ podman run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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