---
layout: container
name:  "quay.io/biocontainers/epytope"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/epytope/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/epytope/container.yaml"
updated_at: "2024-09-12 03:06:31.878540"
latest: "3.3.1--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/epytope"
aliases:
 - "_mhcflurry-cluster-worker-entry-point"
 - "mhcflurry-calibrate-percentile-ranks"
 - "mhcflurry-class1-select-allele-specific-models"
 - "mhcflurry-class1-select-pan-allele-models"
 - "mhcflurry-class1-train-allele-specific-models"
 - "mhcflurry-class1-train-pan-allele-models"
 - "mhcflurry-downloads"
 - "mhcflurry-predict"
 - "pyomo"
 - "theano-cache"
 - "theano-nose"
 - "freeze_graph"
 - "mako-render"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
 - "grpc_python_plugin"
versions:
 - "3.1.0--pyh5e36f6f_0"
 - "3.2.0--pyh7cba7a3_0"
 - "3.3.0--pyh7cba7a3_0"
 - "3.3.1--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for epytope"
config: {"url": "https://biocontainers.pro/tools/epytope", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for epytope", "latest": {"3.3.1--pyh7cba7a3_0": "sha256:342cff55c785b0112120331de5f17f33bb29d69e343a6b78e9a99dd27ebc42b9"}, "tags": {"3.1.0--pyh5e36f6f_0": "sha256:5516aca1093fd09e4da49bd6e1d248703426ccec06cced9995f1e16bb36e2fe9", "3.2.0--pyh7cba7a3_0": "sha256:87c936925de98449e1f9d49eb02858584cac778a9ac8fb090c6519bee8145e5b", "3.3.0--pyh7cba7a3_0": "sha256:b6f410b05bc79f509e4577c7d11ca81ec7e285d3879f8e26f002c4aa5408fc47", "3.3.1--pyh7cba7a3_0": "sha256:342cff55c785b0112120331de5f17f33bb29d69e343a6b78e9a99dd27ebc42b9"}, "docker": "quay.io/biocontainers/epytope", "aliases": {"_mhcflurry-cluster-worker-entry-point": "/usr/local/bin/_mhcflurry-cluster-worker-entry-point", "mhcflurry-calibrate-percentile-ranks": "/usr/local/bin/mhcflurry-calibrate-percentile-ranks", "mhcflurry-class1-select-allele-specific-models": "/usr/local/bin/mhcflurry-class1-select-allele-specific-models", "mhcflurry-class1-select-pan-allele-models": "/usr/local/bin/mhcflurry-class1-select-pan-allele-models", "mhcflurry-class1-train-allele-specific-models": "/usr/local/bin/mhcflurry-class1-train-allele-specific-models", "mhcflurry-class1-train-pan-allele-models": "/usr/local/bin/mhcflurry-class1-train-pan-allele-models", "mhcflurry-downloads": "/usr/local/bin/mhcflurry-downloads", "mhcflurry-predict": "/usr/local/bin/mhcflurry-predict", "pyomo": "/usr/local/bin/pyomo", "theano-cache": "/usr/local/bin/theano-cache", "theano-nose": "/usr/local/bin/theano-nose", "freeze_graph": "/usr/local/bin/freeze_graph", "mako-render": "/usr/local/bin/mako-render", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin", "grpc_python_plugin": "/usr/local/bin/grpc_python_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/epytope.
shpc-registry automated BioContainers addition for epytope
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/epytope
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/epytope:3.3.1--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/epytope/3.3.1--pyh7cba7a3_0
$ module help quay.io/biocontainers/epytope/3.3.1--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### epytope-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### epytope-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### epytope-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### epytope-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### epytope-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### epytope-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### _mhcflurry-cluster-worker-entry-point

```bash
$ singularity exec <container> /usr/local/bin/_mhcflurry-cluster-worker-entry-point
$ podman run --it --rm --entrypoint /usr/local/bin/_mhcflurry-cluster-worker-entry-point   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_mhcflurry-cluster-worker-entry-point   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-calibrate-percentile-ranks

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-calibrate-percentile-ranks
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-calibrate-percentile-ranks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-calibrate-percentile-ranks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-select-allele-specific-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-select-allele-specific-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-allele-specific-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-allele-specific-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-select-pan-allele-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-select-pan-allele-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-pan-allele-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-select-pan-allele-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-train-allele-specific-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-train-allele-specific-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-allele-specific-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-allele-specific-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-class1-train-pan-allele-models

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-class1-train-pan-allele-models
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-pan-allele-models   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-class1-train-pan-allele-models   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-downloads

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-downloads
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-downloads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-downloads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mhcflurry-predict

```bash
$ singularity exec <container> /usr/local/bin/mhcflurry-predict
$ podman run --it --rm --entrypoint /usr/local/bin/mhcflurry-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mhcflurry-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyomo

```bash
$ singularity exec <container> /usr/local/bin/pyomo
$ podman run --it --rm --entrypoint /usr/local/bin/pyomo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyomo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-cache

```bash
$ singularity exec <container> /usr/local/bin/theano-cache
$ podman run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### theano-nose

```bash
$ singularity exec <container> /usr/local/bin/theano-nose
$ podman run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/theano-nose   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### freeze_graph

```bash
$ singularity exec <container> /usr/local/bin/freeze_graph
$ podman run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/freeze_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
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