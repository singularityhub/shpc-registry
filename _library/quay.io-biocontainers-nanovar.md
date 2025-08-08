---
layout: container
name:  "quay.io/biocontainers/nanovar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanovar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanovar/container.yaml"
updated_at: "2025-08-08 04:27:25.874881"
latest: "1.8.3--py311haab0aaa_0"
container_url: "https://biocontainers.pro/tools/nanovar"
aliases:
 - "cytocad"
 - "hs-blastn"
 - "import_pb_to_tensorboard"
 - "nanovar"
 - "rfmix2tagore.py"
 - "tagore"
 - "estimator_ckpt_converter"
 - "google-oauthlib-tool"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
 - "grpc_ruby_plugin"
 - "tf_upgrade_v2"
versions:
 - "1.4.1--py37h8902056_1"
 - "1.4.1--py38he5da3d1_2"
 - "1.5.0--py38he5da3d1_0"
 - "1.5.1--py39hf95cd2a_0"
 - "1.5.1--py38he5da3d1_0"
 - "1.4.1--py39hf95cd2a_2"
 - "1.8.1--py39hff71179_0"
 - "1.8.3--py311haab0aaa_0"
description: "shpc-registry automated BioContainers addition for nanovar"
config: {"url": "https://biocontainers.pro/tools/nanovar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanovar", "latest": {"1.8.3--py311haab0aaa_0": "sha256:a597027763e58e9ef3675e00c6fa9564d6534144fc0a6c068fe98f3eb0eee037"}, "tags": {"1.4.1--py37h8902056_1": "sha256:7ecf3a09a52418b6d2aaa01c176bfccea9ce7edcbbc4512e9a64e5d09f4a1706", "1.4.1--py38he5da3d1_2": "sha256:4bf04d517cc829cc5ce9e7c76e4ebe5a4bbfa261229c0413f476fd326cb0378d", "1.5.0--py38he5da3d1_0": "sha256:3a6e5bd46980d6588cd02d79ea3e3f266088aae8f7392181c6d3b3a8d2723e90", "1.5.1--py39hf95cd2a_0": "sha256:1309ccca4339b303c66b286b3c915d80b0a3be653b229472c4926b7e99f76d1b", "1.5.1--py38he5da3d1_0": "sha256:27b50c1f4a210c9600b9e4e42ea8c2589a611dacbddc9f4ad048be8b16c56ed4", "1.4.1--py39hf95cd2a_2": "sha256:a3ac134bc225f338c7da27813ec238315e4794daa77a7f9ce531a9fcb5e94b88", "1.8.1--py39hff71179_0": "sha256:a68f59200b42484132e2a2266ff10258e7d90346f360a9e9d20b43984cfe4198", "1.8.3--py311haab0aaa_0": "sha256:a597027763e58e9ef3675e00c6fa9564d6534144fc0a6c068fe98f3eb0eee037"}, "docker": "quay.io/biocontainers/nanovar", "aliases": {"cytocad": "/usr/local/bin/cytocad", "hs-blastn": "/usr/local/bin/hs-blastn", "import_pb_to_tensorboard": "/usr/local/bin/import_pb_to_tensorboard", "nanovar": "/usr/local/bin/nanovar", "rfmix2tagore.py": "/usr/local/bin/rfmix2tagore.py", "tagore": "/usr/local/bin/tagore", "estimator_ckpt_converter": "/usr/local/bin/estimator_ckpt_converter", "google-oauthlib-tool": "/usr/local/bin/google-oauthlib-tool", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin", "grpc_ruby_plugin": "/usr/local/bin/grpc_ruby_plugin", "tf_upgrade_v2": "/usr/local/bin/tf_upgrade_v2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanovar.
shpc-registry automated BioContainers addition for nanovar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanovar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanovar:1.8.3--py311haab0aaa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanovar/1.8.3--py311haab0aaa_0
$ module help quay.io/biocontainers/nanovar/1.8.3--py311haab0aaa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanovar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanovar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanovar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanovar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanovar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanovar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cytocad

```bash
$ singularity exec <container> /usr/local/bin/cytocad
$ podman run --it --rm --entrypoint /usr/local/bin/cytocad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cytocad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hs-blastn

```bash
$ singularity exec <container> /usr/local/bin/hs-blastn
$ podman run --it --rm --entrypoint /usr/local/bin/hs-blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hs-blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### import_pb_to_tensorboard

```bash
$ singularity exec <container> /usr/local/bin/import_pb_to_tensorboard
$ podman run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/import_pb_to_tensorboard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nanovar

```bash
$ singularity exec <container> /usr/local/bin/nanovar
$ podman run --it --rm --entrypoint /usr/local/bin/nanovar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nanovar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rfmix2tagore.py

```bash
$ singularity exec <container> /usr/local/bin/rfmix2tagore.py
$ podman run --it --rm --entrypoint /usr/local/bin/rfmix2tagore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rfmix2tagore.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tagore

```bash
$ singularity exec <container> /usr/local/bin/tagore
$ podman run --it --rm --entrypoint /usr/local/bin/tagore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tagore   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tf_upgrade_v2

```bash
$ singularity exec <container> /usr/local/bin/tf_upgrade_v2
$ podman run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tf_upgrade_v2   -v ${PWD} -w ${PWD} <container> -c " $@"
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