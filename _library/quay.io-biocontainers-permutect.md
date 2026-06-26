---
layout: container
name:  "quay.io/biocontainers/permutect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/permutect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/permutect/container.yaml"
updated_at: "2026-06-26 06:14:16.984163"
latest: "0.8.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/permutect"
aliases:
 - "c++"
 - "cc"
 - "cpp"
 - "edit_dataset"
 - "filter_variants"
 - "g++"
 - "gcc"
 - "gcc-ar"
 - "gcc-nm"
 - "gcc-ranlib"
 - "gcov"
 - "gcov-dump"
 - "gcov-tool"
 - "preprocess_dataset"
 - "prune_dataset"
 - "pytensor-cache"
 - "refine_artifact_model"
 - "train_artifact_model"
 - "fc-genconf"
 - "dot_sandbox"
 - "cyvcf2"
 - "get_gprof"
 - "torchfrtrace"
 - "gtk-builder-tool"
 - "gtk-encode-symbolic-svg"
 - "gtk-launch"
 - "gtk-query-immodules-3.0"
 - "gtk-query-settings"
 - "protoc-33.5.0"
 - "protoc-gen-upb-33.5.0"
 - "protoc-gen-upb_minitable-33.5.0"
 - "protoc-gen-upbdefs-33.5.0"
 - "pybind11-config"
 - "protoc-gen-upb_minitable"
 - "torch_shm_manager"
 - "wayland-scanner"
 - "hb-raster"
 - "hb-vector"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "get_objgraph"
 - "undill"
versions:
 - "0.8.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for permutect"
config: {"url": "https://biocontainers.pro/tools/permutect", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for permutect", "latest": {"0.8.0--pyhdfd78af_0": "sha256:fc69441df9f5681319f7f9bd9676e55879e97992bca06fcc96e7a7ff49ed06a9"}, "tags": {"0.8.0--pyhdfd78af_0": "sha256:fc69441df9f5681319f7f9bd9676e55879e97992bca06fcc96e7a7ff49ed06a9"}, "docker": "quay.io/biocontainers/permutect", "aliases": {"c++": "/usr/local/bin/c++", "cc": "/usr/local/bin/cc", "cpp": "/usr/local/bin/cpp", "edit_dataset": "/usr/local/bin/edit_dataset", "filter_variants": "/usr/local/bin/filter_variants", "g++": "/usr/local/bin/g++", "gcc": "/usr/local/bin/gcc", "gcc-ar": "/usr/local/bin/gcc-ar", "gcc-nm": "/usr/local/bin/gcc-nm", "gcc-ranlib": "/usr/local/bin/gcc-ranlib", "gcov": "/usr/local/bin/gcov", "gcov-dump": "/usr/local/bin/gcov-dump", "gcov-tool": "/usr/local/bin/gcov-tool", "preprocess_dataset": "/usr/local/bin/preprocess_dataset", "prune_dataset": "/usr/local/bin/prune_dataset", "pytensor-cache": "/usr/local/bin/pytensor-cache", "refine_artifact_model": "/usr/local/bin/refine_artifact_model", "train_artifact_model": "/usr/local/bin/train_artifact_model", "fc-genconf": "/usr/local/bin/fc-genconf", "dot_sandbox": "/usr/local/bin/dot_sandbox", "cyvcf2": "/usr/local/bin/cyvcf2", "get_gprof": "/usr/local/bin/get_gprof", "torchfrtrace": "/usr/local/bin/torchfrtrace", "gtk-builder-tool": "/usr/local/bin/gtk-builder-tool", "gtk-encode-symbolic-svg": "/usr/local/bin/gtk-encode-symbolic-svg", "gtk-launch": "/usr/local/bin/gtk-launch", "gtk-query-immodules-3.0": "/usr/local/bin/gtk-query-immodules-3.0", "gtk-query-settings": "/usr/local/bin/gtk-query-settings", "protoc-33.5.0": "/usr/local/bin/protoc-33.5.0", "protoc-gen-upb-33.5.0": "/usr/local/bin/protoc-gen-upb-33.5.0", "protoc-gen-upb_minitable-33.5.0": "/usr/local/bin/protoc-gen-upb_minitable-33.5.0", "protoc-gen-upbdefs-33.5.0": "/usr/local/bin/protoc-gen-upbdefs-33.5.0", "pybind11-config": "/usr/local/bin/pybind11-config", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "torch_shm_manager": "/usr/local/bin/torch_shm_manager", "wayland-scanner": "/usr/local/bin/wayland-scanner", "hb-raster": "/usr/local/bin/hb-raster", "hb-vector": "/usr/local/bin/hb-vector", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/permutect.
singularity registry hpc automated addition for permutect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/permutect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/permutect:0.8.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/permutect/0.8.0--pyhdfd78af_0
$ module help quay.io/biocontainers/permutect/0.8.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### permutect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### permutect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### permutect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### permutect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### permutect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### permutect-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c++

```bash
$ singularity exec <container> /usr/local/bin/c++
$ podman run --it --rm --entrypoint /usr/local/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cc

```bash
$ singularity exec <container> /usr/local/bin/cc
$ podman run --it --rm --entrypoint /usr/local/bin/cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cpp

```bash
$ singularity exec <container> /usr/local/bin/cpp
$ podman run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edit_dataset

```bash
$ singularity exec <container> /usr/local/bin/edit_dataset
$ podman run --it --rm --entrypoint /usr/local/bin/edit_dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edit_dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_variants

```bash
$ singularity exec <container> /usr/local/bin/filter_variants
$ podman run --it --rm --entrypoint /usr/local/bin/filter_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_variants   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g++

```bash
$ singularity exec <container> /usr/local/bin/g++
$ podman run --it --rm --entrypoint /usr/local/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc

```bash
$ singularity exec <container> /usr/local/bin/gcc
$ podman run --it --rm --entrypoint /usr/local/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ar

```bash
$ singularity exec <container> /usr/local/bin/gcc-ar
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-ar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-nm

```bash
$ singularity exec <container> /usr/local/bin/gcc-nm
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-nm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcc-ranlib

```bash
$ singularity exec <container> /usr/local/bin/gcc-ranlib
$ podman run --it --rm --entrypoint /usr/local/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcc-ranlib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov

```bash
$ singularity exec <container> /usr/local/bin/gcov
$ podman run --it --rm --entrypoint /usr/local/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-dump

```bash
$ singularity exec <container> /usr/local/bin/gcov-dump
$ podman run --it --rm --entrypoint /usr/local/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcov-tool

```bash
$ singularity exec <container> /usr/local/bin/gcov-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcov-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### preprocess_dataset

```bash
$ singularity exec <container> /usr/local/bin/preprocess_dataset
$ podman run --it --rm --entrypoint /usr/local/bin/preprocess_dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/preprocess_dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prune_dataset

```bash
$ singularity exec <container> /usr/local/bin/prune_dataset
$ podman run --it --rm --entrypoint /usr/local/bin/prune_dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prune_dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytensor-cache

```bash
$ singularity exec <container> /usr/local/bin/pytensor-cache
$ podman run --it --rm --entrypoint /usr/local/bin/pytensor-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytensor-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refine_artifact_model

```bash
$ singularity exec <container> /usr/local/bin/refine_artifact_model
$ podman run --it --rm --entrypoint /usr/local/bin/refine_artifact_model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refine_artifact_model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### train_artifact_model

```bash
$ singularity exec <container> /usr/local/bin/train_artifact_model
$ podman run --it --rm --entrypoint /usr/local/bin/train_artifact_model   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/train_artifact_model   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dot_sandbox

```bash
$ singularity exec <container> /usr/local/bin/dot_sandbox
$ podman run --it --rm --entrypoint /usr/local/bin/dot_sandbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dot_sandbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cyvcf2

```bash
$ singularity exec <container> /usr/local/bin/cyvcf2
$ podman run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cyvcf2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_gprof

```bash
$ singularity exec <container> /usr/local/bin/get_gprof
$ podman run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_gprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-encode-symbolic-svg

```bash
$ singularity exec <container> /usr/local/bin/gtk-encode-symbolic-svg
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-launch

```bash
$ singularity exec <container> /usr/local/bin/gtk-launch
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-3.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-settings

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-settings
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-33.5.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-33.5.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-33.5.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torch_shm_manager

```bash
$ singularity exec <container> /usr/local/bin/torch_shm_manager
$ podman run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torch_shm_manager   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wayland-scanner

```bash
$ singularity exec <container> /usr/local/bin/wayland-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-vector

```bash
$ singularity exec <container> /usr/local/bin/hb-vector
$ podman run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-vector   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-compile-repository

```bash
$ singularity exec <container> /usr/local/bin/gi-compile-repository
$ podman run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-decompile-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-decompile-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-inspect-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-inspect-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
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