---
layout: container
name:  "quay.io/biocontainers/guidemaker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/guidemaker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/guidemaker/container.yaml"
updated_at: "2024-04-21 02:46:47.254697"
latest: "0.4.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/guidemaker"
aliases:
 - "base58"
 - "black"
 - "black-primer"
 - "blackd"
 - "csv-import"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "guidemaker"
 - "jupyter-dejavu"
 - "jupyter-execute"
 - "onnxruntime_test"
 - "orc-memory"
 - "orc-scan"
 - "pdoc"
 - "pdoc3"
 - "pybind11-config"
 - "send2trash"
 - "streamlit"
 - "streamlit.cmd"
 - "timezone-dump"
 - "watchmedo"
 - "orc-contents"
 - "orc-metadata"
 - "orc-statistics"
 - "plasma-store-server"
 - "plasma_store"
 - "sha256_profile"
 - "coverage"
 - "gflags_completions.sh"
 - "mako-render"
 - "grpc_cpp_plugin"
versions:
 - "0.3.4--pyhdfd78af_0"
 - "0.3.6--pyhdfd78af_0"
 - "0.4.1--pyhdfd78af_0"
 - "0.4.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for guidemaker"
config: {"url": "https://biocontainers.pro/tools/guidemaker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for guidemaker", "latest": {"0.4.2--pyhdfd78af_0": "sha256:14062045f818e0461968308ba7071e218bc02150b1c2a1173cf60f93f2dcca31"}, "tags": {"0.3.4--pyhdfd78af_0": "sha256:9ffc309a7fdc7dad98bca348e8d6ca538548b2e0ca4b24961c88f40fdcb6c83d", "0.3.6--pyhdfd78af_0": "sha256:5b2323eaf10fbdf5eb814e726325ecff4c177514bb4e6e3c2dd46f6a6f37e9bf", "0.4.1--pyhdfd78af_0": "sha256:0f251e8233708e4a00b4699dc359ef8b9bf25b22e656d3046c4b06ccb86de76b", "0.4.2--pyhdfd78af_0": "sha256:14062045f818e0461968308ba7071e218bc02150b1c2a1173cf60f93f2dcca31"}, "docker": "quay.io/biocontainers/guidemaker", "aliases": {"base58": "/usr/local/bin/base58", "black": "/usr/local/bin/black", "black-primer": "/usr/local/bin/black-primer", "blackd": "/usr/local/bin/blackd", "csv-import": "/usr/local/bin/csv-import", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "guidemaker": "/usr/local/bin/guidemaker", "jupyter-dejavu": "/usr/local/bin/jupyter-dejavu", "jupyter-execute": "/usr/local/bin/jupyter-execute", "onnxruntime_test": "/usr/local/bin/onnxruntime_test", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "pdoc": "/usr/local/bin/pdoc", "pdoc3": "/usr/local/bin/pdoc3", "pybind11-config": "/usr/local/bin/pybind11-config", "send2trash": "/usr/local/bin/send2trash", "streamlit": "/usr/local/bin/streamlit", "streamlit.cmd": "/usr/local/bin/streamlit.cmd", "timezone-dump": "/usr/local/bin/timezone-dump", "watchmedo": "/usr/local/bin/watchmedo", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata", "orc-statistics": "/usr/local/bin/orc-statistics", "plasma-store-server": "/usr/local/bin/plasma-store-server", "plasma_store": "/usr/local/bin/plasma_store", "sha256_profile": "/usr/local/bin/sha256_profile", "coverage": "/usr/local/bin/coverage", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh", "mako-render": "/usr/local/bin/mako-render", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/guidemaker.
shpc-registry automated BioContainers addition for guidemaker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/guidemaker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/guidemaker:0.4.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/guidemaker/0.4.2--pyhdfd78af_0
$ module help quay.io/biocontainers/guidemaker/0.4.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### guidemaker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### guidemaker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### guidemaker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### guidemaker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### guidemaker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### guidemaker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### base58

```bash
$ singularity exec <container> /usr/local/bin/base58
$ podman run --it --rm --entrypoint /usr/local/bin/base58   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base58   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black

```bash
$ singularity exec <container> /usr/local/bin/black
$ podman run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### black-primer

```bash
$ singularity exec <container> /usr/local/bin/black-primer
$ podman run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/black-primer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blackd

```bash
$ singularity exec <container> /usr/local/bin/blackd
$ podman run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blackd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl

```bash
$ singularity exec <container> /usr/local/bin/elasticurl
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elasticurl_cpp

```bash
$ singularity exec <container> /usr/local/bin/elasticurl_cpp
$ podman run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elasticurl_cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### guidemaker

```bash
$ singularity exec <container> /usr/local/bin/guidemaker
$ podman run --it --rm --entrypoint /usr/local/bin/guidemaker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/guidemaker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-dejavu

```bash
$ singularity exec <container> /usr/local/bin/jupyter-dejavu
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-dejavu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-execute

```bash
$ singularity exec <container> /usr/local/bin/jupyter-execute
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-execute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onnxruntime_test

```bash
$ singularity exec <container> /usr/local/bin/onnxruntime_test
$ podman run --it --rm --entrypoint /usr/local/bin/onnxruntime_test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onnxruntime_test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-memory

```bash
$ singularity exec <container> /usr/local/bin/orc-memory
$ podman run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-memory   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-scan

```bash
$ singularity exec <container> /usr/local/bin/orc-scan
$ podman run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-scan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdoc

```bash
$ singularity exec <container> /usr/local/bin/pdoc
$ podman run --it --rm --entrypoint /usr/local/bin/pdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdoc3

```bash
$ singularity exec <container> /usr/local/bin/pdoc3
$ podman run --it --rm --entrypoint /usr/local/bin/pdoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamlit

```bash
$ singularity exec <container> /usr/local/bin/streamlit
$ podman run --it --rm --entrypoint /usr/local/bin/streamlit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamlit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamlit.cmd

```bash
$ singularity exec <container> /usr/local/bin/streamlit.cmd
$ podman run --it --rm --entrypoint /usr/local/bin/streamlit.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamlit.cmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watchmedo

```bash
$ singularity exec <container> /usr/local/bin/watchmedo
$ podman run --it --rm --entrypoint /usr/local/bin/watchmedo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchmedo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-contents

```bash
$ singularity exec <container> /usr/local/bin/orc-contents
$ podman run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-contents   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-metadata

```bash
$ singularity exec <container> /usr/local/bin/orc-metadata
$ podman run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-metadata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orc-statistics

```bash
$ singularity exec <container> /usr/local/bin/orc-statistics
$ podman run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orc-statistics   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma-store-server

```bash
$ singularity exec <container> /usr/local/bin/plasma-store-server
$ podman run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma-store-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plasma_store

```bash
$ singularity exec <container> /usr/local/bin/plasma_store
$ podman run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plasma_store   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sha256_profile

```bash
$ singularity exec <container> /usr/local/bin/sha256_profile
$ podman run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sha256_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
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