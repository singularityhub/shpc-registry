---
layout: container
name:  "quay.io/biocontainers/progenomes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/progenomes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/progenomes/container.yaml"
updated_at: "2026-01-23 03:52:42.500359"
latest: "0.3.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/progenomes"
aliases:
 - "progenomes"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "protoc-31.1.0"
 - "protoc-gen-upb-31.1.0"
 - "protoc-gen-upbdefs-31.1.0"
 - "h2benchmark"
 - "protoc-gen-upb"
 - "protoc-gen-upbdefs"
 - "checksum-profile"
 - "elastishadow"
 - "elastipubsub5"
 - "mqtt5_app"
 - "mqtt5_canary"
 - "mqtt5canary"
 - "elasticurl"
 - "elasticurl_cpp"
 - "elastipubsub"
 - "csv-import"
 - "orc-memory"
 - "orc-scan"
 - "timezone-dump"
 - "orc-contents"
 - "orc-metadata"
versions:
 - "0.2.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for progenomes"
config: {"url": "https://biocontainers.pro/tools/progenomes", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for progenomes", "latest": {"0.3.0--pyhdfd78af_0": "sha256:2c8449dbaa544392a619d9df10c15741f1b53ab584c83628835ec3d107899da5"}, "tags": {"0.2.0--pyhdfd78af_0": "sha256:58d1d46554adfbfa9bd99e6e3dbcde6aba680026e51f089924b08e63257fc02b", "0.3.0--pyhdfd78af_0": "sha256:2c8449dbaa544392a619d9df10c15741f1b53ab584c83628835ec3d107899da5"}, "docker": "quay.io/biocontainers/progenomes", "aliases": {"progenomes": "/usr/local/bin/progenomes", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "protoc-31.1.0": "/usr/local/bin/protoc-31.1.0", "protoc-gen-upb-31.1.0": "/usr/local/bin/protoc-gen-upb-31.1.0", "protoc-gen-upbdefs-31.1.0": "/usr/local/bin/protoc-gen-upbdefs-31.1.0", "h2benchmark": "/usr/local/bin/h2benchmark", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "checksum-profile": "/usr/local/bin/checksum-profile", "elastishadow": "/usr/local/bin/elastishadow", "elastipubsub5": "/usr/local/bin/elastipubsub5", "mqtt5_app": "/usr/local/bin/mqtt5_app", "mqtt5_canary": "/usr/local/bin/mqtt5_canary", "mqtt5canary": "/usr/local/bin/mqtt5canary", "elasticurl": "/usr/local/bin/elasticurl", "elasticurl_cpp": "/usr/local/bin/elasticurl_cpp", "elastipubsub": "/usr/local/bin/elastipubsub", "csv-import": "/usr/local/bin/csv-import", "orc-memory": "/usr/local/bin/orc-memory", "orc-scan": "/usr/local/bin/orc-scan", "timezone-dump": "/usr/local/bin/timezone-dump", "orc-contents": "/usr/local/bin/orc-contents", "orc-metadata": "/usr/local/bin/orc-metadata"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/progenomes.
singularity registry hpc automated addition for progenomes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/progenomes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/progenomes:0.3.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/progenomes/0.3.0--pyhdfd78af_0
$ module help quay.io/biocontainers/progenomes/0.3.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### progenomes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### progenomes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### progenomes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### progenomes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### progenomes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### progenomes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### progenomes

```bash
$ singularity exec <container> /usr/local/bin/progenomes
$ podman run --it --rm --entrypoint /usr/local/bin/progenomes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/progenomes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-31.1.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-31.1.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-31.1.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h2benchmark

```bash
$ singularity exec <container> /usr/local/bin/h2benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h2benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
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