---
layout: container
name:  "quay.io/biocontainers/vpt-segmentation-packing"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vpt-segmentation-packing/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vpt-segmentation-packing/container.yaml"
updated_at: "2025-12-15 04:11:55.655656"
latest: "1.0.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/vpt-segmentation-packing"
aliases:
 - "protoc-28.3.0"
 - "checksum-profile"
 - "elastishadow"
 - "geosop"
 - "elastipubsub5"
 - "mqtt5_app"
 - "mqtt5_canary"
 - "mqtt5canary"
 - "geos-config"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "csv-import"
 - "orc-memory"
 - "orc-scan"
 - "timezone-dump"
 - "orc-contents"
 - "orc-metadata"
 - "orc-statistics"
 - "gflags_completions.sh"
 - "numpy-config"
 - "grpc_cpp_plugin"
 - "grpc_csharp_plugin"
 - "grpc_node_plugin"
 - "grpc_objective_c_plugin"
 - "grpc_php_plugin"
versions:
 - "1.0.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for vpt-segmentation-packing"
config: {"url": "https://biocontainers.pro/tools/vpt-segmentation-packing", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vpt-segmentation-packing", "latest": {"1.0.1--pyhdfd78af_0": "sha256:84cbe83e7a94aecea892025591165f3164b51795088cb9f8d69cbe897ae3fd78"}, "tags": {"1.0.1--pyhdfd78af_0": "sha256:84cbe83e7a94aecea892025591165f3164b51795088cb9f8d69cbe897ae3fd78"}, "docker": "quay.io/biocontainers/vpt-segmentation-packing", "aliases": {"protoc-28.3.0": "/usr/local/bin/protoc-28.3.0", "checksum-profile": "/usr/local/bin/checksum-profile", "elastishadow": "/usr/local/bin/elastishadow", "geosop": "/usr/local/bin/geosop", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app", "mqtt5_canary": "/usr/local/bin/mqtt5_canary", "mqtt5canary": "/usr/local/bin/mqtt5canary", "geos-config": "/usr/local/bin/geos-config", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "csv-import": "/usr/local/bin/csv-import", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "timezone-dump": "/usr/local/bin/timezone-dump", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata", "orc-statistics": "/usr/local/bin/orc-statistics", "gflags_completions.sh": "/usr/local/bin/gflags_completions.sh", "numpy-config": "/usr/local/bin/numpy-config", "grpc_cpp_plugin": "/usr/local/bin/grpc_cpp_plugin", "grpc_csharp_plugin": "/usr/local/bin/grpc_csharp_plugin", "grpc_node_plugin": "/usr/local/bin/grpc_node_plugin", "grpc_objective_c_plugin": "/usr/local/bin/grpc_objective_c_plugin", "grpc_php_plugin": "/usr/local/bin/grpc_php_plugin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vpt-segmentation-packing.
singularity registry hpc automated addition for vpt-segmentation-packing
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vpt-segmentation-packing
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vpt-segmentation-packing:1.0.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vpt-segmentation-packing/1.0.1--pyhdfd78af_0
$ module help quay.io/biocontainers/vpt-segmentation-packing/1.0.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vpt-segmentation-packing-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vpt-segmentation-packing-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vpt-segmentation-packing-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vpt-segmentation-packing-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vpt-segmentation-packing-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vpt-segmentation-packing-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### protoc-28.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastishadow

```bash
$ singularity exec <container> /usr/local/bin/elastishadow
$ podman run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastipubsub5

```bash
$ singularity exec <container> /usr/local/bin/elastipubsub5
$ podman run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastipubsub5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_app

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_app
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_app   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5_canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5_canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5_canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mqtt5canary

```bash
$ singularity exec <container> /usr/local/bin/mqtt5canary
$ podman run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mqtt5canary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gflags_completions.sh

```bash
$ singularity exec <container> /usr/local/bin/gflags_completions.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gflags_completions.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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