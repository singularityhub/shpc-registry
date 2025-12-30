---
layout: container
name:  "quay.io/biocontainers/amdirt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amdirt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/amdirt/container.yaml"
updated_at: "2025-12-30 04:06:55.858603"
latest: "1.6.5--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/amdirt"
aliases:
 - "AMDirT"
 - "streamlit"
 - "streamlit.cmd"
 - "watchmedo"
 - "markdown-it"
 - "csv-import"
 - "orc-memory"
 - "orc-scan"
 - "timezone-dump"
 - "orc-contents"
 - "orc-metadata"
 - "orc-statistics"
 - "plasma-store-server"
 - "plasma_store"
 - "tjbench"
 - "gflags_completions.sh"
 - "jupyter-kernel"
 - "jupyter-kernelspec"
 - "jupyter-run"
 - "f2py3.11"
 - "curve_keygen"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
 - "grpc_ruby_plugin"
 - "ipython3"
versions:
 - "1.4.3--pyhdfd78af_0"
 - "1.4.6--pyhdfd78af_0"
 - "1.5.0--pyhdfd78af_0"
 - "1.5.0--pyhdfd78af_1"
 - "1.6.0--pyhdfd78af_0"
 - "1.6.1--pyhdfd78af_0"
 - "1.6.2--pyhdfd78af_0"
 - "1.6.5--pyhdfd78af_0"
 - "1.6.5--pyhdfd78af_1"
description: "singularity registry hpc automated addition for amdirt"
config: {"url": "https://biocontainers.pro/tools/amdirt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for amdirt", "latest": {"1.6.5--pyhdfd78af_1": "sha256:a2d6ddda64486a0e4071ddd9bef7d155e56cca5181b87416465b784add2d153b"}, "tags": {"1.4.3--pyhdfd78af_0": "sha256:0c9b82ae40249523d2ff74f2ff51efa786a583106f8e8b496c723324cd80e843", "1.4.6--pyhdfd78af_0": "sha256:2847a4aaee53e840bd412192eb59a1925df61d880c549bb6414e0a04d0747892", "1.5.0--pyhdfd78af_0": "sha256:40c57ea2da544cdf015d4a9555bb8aad9253a0ea3db4abd7120c48d3b7e1bb91", "1.5.0--pyhdfd78af_1": "sha256:4f0a685801ecb4294b5fb3c2022c3093b89318eb279387f44072583d9f336d6d", "1.6.0--pyhdfd78af_0": "sha256:e3becb4083ad086742313953e4e2fd285f630c0c9dfae478b90458601781da6e", "1.6.1--pyhdfd78af_0": "sha256:70bc4ace25dfcc45d0dca44ce96a86b91df012eb0554aab9a9da75843ec276f6", "1.6.2--pyhdfd78af_0": "sha256:8f36f07d275d24f09de8ece09b643c6c6db3b0ae4c507906b9617352e6414fa1", "1.6.5--pyhdfd78af_0": "sha256:cea53336e83d0d0356ea0167eda508b52d34f5a8373123ef57dc9a76623bcb93", "1.6.5--pyhdfd78af_1": "sha256:a2d6ddda64486a0e4071ddd9bef7d155e56cca5181b87416465b784add2d153b"}, "docker": "quay.io/biocontainers/amdirt", "aliases": {"AMDirT": "/usr/local/bin/AMDirT", "streamlit": "/usr/local/bin/streamlit", "streamlit.cmd": "/usr/local/bin/streamlit.cmd", "watchmedo": "/usr/local/bin/watchmedo", "markdown-it": "/usr/local/bin/markdown-it", "csv-import": "/usr/local/bin/csv-import", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "timezone-dump": "/usr/local/bin/timezone-dump", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata", "orc-statistics": "/usr/local/bin/orc-statistics", "plasma-store-server": "/usr/local/bin/plasma-store-server", "plasma_store": "/usr/local/bin/plasma_store", "tjbench": "/usr/local/bin/tjbench", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh", "jupyter-kernel": "/usr/local/bin/jupyter-kernel", "jupyter-kernelspec": "/usr/local/bin/jupyter-kernelspec", "jupyter-run": "/usr/local/bin/jupyter-run", "f2py3.11": "/usr/local/bin/f2py3.11", "curve_keygen": "/usr/local/bin/curve_keygen", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin", "grpc_ruby_plugin": "/usr/local/bin/grpc_ruby_plugin", "ipython3": "/usr/local/bin/ipython3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amdirt.
singularity registry hpc automated addition for amdirt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amdirt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amdirt:1.6.5--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amdirt/1.6.5--pyhdfd78af_1
$ module help quay.io/biocontainers/amdirt/1.6.5--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amdirt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amdirt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amdirt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amdirt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amdirt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amdirt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### AMDirT

```bash
$ singularity exec <container> /usr/local/bin/AMDirT
$ podman run --it --rm --entrypoint /usr/local/bin/AMDirT   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AMDirT   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### watchmedo

```bash
$ singularity exec <container> /usr/local/bin/watchmedo
$ podman run --it --rm --entrypoint /usr/local/bin/watchmedo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watchmedo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown-it

```bash
$ singularity exec <container> /usr/local/bin/markdown-it
$ podman run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown-it   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csv-import

```bash
$ singularity exec <container> /usr/local/bin/csv-import
$ podman run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csv-import   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### timezone-dump

```bash
$ singularity exec <container> /usr/local/bin/timezone-dump
$ podman run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/timezone-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernel

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernel
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-kernelspec

```bash
$ singularity exec <container> /usr/local/bin/jupyter-kernelspec
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-kernelspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-run

```bash
$ singularity exec <container> /usr/local/bin/jupyter-run
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-run   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### curve_keygen

```bash
$ singularity exec <container> /usr/local/bin/curve_keygen
$ podman run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/curve_keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ipython3

```bash
$ singularity exec <container> /usr/local/bin/ipython3
$ podman run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipython3   -v ${PWD} -w ${PWD} <container> -c " $@"
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