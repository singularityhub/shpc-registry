---
layout: container
name:  "quay.io/biocontainers/simba"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/simba/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/simba/container.yaml"
updated_at: "2024-12-25 02:57:05.324706"
latest: "1.2--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/simba"
aliases:
 - "torchbiggraph_config"
 - "torchbiggraph_eval"
 - "torchbiggraph_example_fb15k"
 - "torchbiggraph_example_livejournal"
 - "torchbiggraph_export_to_tsv"
 - "torchbiggraph_import_from_parquet"
 - "torchbiggraph_import_from_tsv"
 - "torchbiggraph_partitionserver"
 - "torchbiggraph_train"
 - "torchrun"
 - "convert-caffe2-to-onnx"
 - "convert-onnx-to-caffe2"
 - "ninja"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "numba"
 - "pycc"
 - "natsort"
versions:
 - "1.1--pyhdfd78af_0"
 - "1.2--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for simba"
config: {"url": "https://biocontainers.pro/tools/simba", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for simba", "latest": {"1.2--pyh7cba7a3_0": "sha256:943a1dd16bcc1fbf7c695d1a2b2b836839623374951f31c9eda66c3d6a33aae3"}, "tags": {"1.1--pyhdfd78af_0": "sha256:8947ee7a83ad53fcc315209ff5fef1dbb49da2419dab574d82df465b43452448", "1.2--pyh7cba7a3_0": "sha256:943a1dd16bcc1fbf7c695d1a2b2b836839623374951f31c9eda66c3d6a33aae3"}, "docker": "quay.io/biocontainers/simba", "aliases": {"torchbiggraph_config": "/usr/local/bin/torchbiggraph_config", "torchbiggraph_eval": "/usr/local/bin/torchbiggraph_eval", "torchbiggraph_example_fb15k": "/usr/local/bin/torchbiggraph_example_fb15k", "torchbiggraph_example_livejournal": "/usr/local/bin/torchbiggraph_example_livejournal", "torchbiggraph_export_to_tsv": "/usr/local/bin/torchbiggraph_export_to_tsv", "torchbiggraph_import_from_parquet": "/usr/local/bin/torchbiggraph_import_from_parquet", "torchbiggraph_import_from_tsv": "/usr/local/bin/torchbiggraph_import_from_tsv", "torchbiggraph_partitionserver": "/usr/local/bin/torchbiggraph_partitionserver", "torchbiggraph_train": "/usr/local/bin/torchbiggraph_train", "torchrun": "/usr/local/bin/torchrun", "convert-caffe2-to-onnx": "/usr/local/bin/convert-caffe2-to-onnx", "convert-onnx-to-caffe2": "/usr/local/bin/convert-onnx-to-caffe2", "ninja": "/usr/local/bin/ninja", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "natsort": "/usr/local/bin/natsort"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/simba.
shpc-registry automated BioContainers addition for simba
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/simba
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/simba:1.2--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/simba/1.2--pyh7cba7a3_0
$ module help quay.io/biocontainers/simba/1.2--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### simba-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### simba-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### simba-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### simba-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### simba-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### simba-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### torchbiggraph_config

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_config
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchbiggraph_eval

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_eval
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchbiggraph_example_fb15k

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_example_fb15k
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_example_fb15k   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_example_fb15k   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchbiggraph_example_livejournal

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_example_livejournal
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_example_livejournal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_example_livejournal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchbiggraph_export_to_tsv

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_export_to_tsv
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_export_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_export_to_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchbiggraph_import_from_parquet

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_import_from_parquet
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_import_from_parquet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_import_from_parquet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchbiggraph_import_from_tsv

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_import_from_tsv
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_import_from_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_import_from_tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchbiggraph_partitionserver

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_partitionserver
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_partitionserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_partitionserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchbiggraph_train

```bash
$ singularity exec <container> /usr/local/bin/torchbiggraph_train
$ podman run --it --rm --entrypoint /usr/local/bin/torchbiggraph_train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchbiggraph_train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchrun

```bash
$ singularity exec <container> /usr/local/bin/torchrun
$ podman run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchrun   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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