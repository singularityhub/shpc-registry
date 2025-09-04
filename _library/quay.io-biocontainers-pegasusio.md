---
layout: container
name:  "quay.io/biocontainers/pegasusio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pegasusio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pegasusio/container.yaml"
updated_at: "2025-09-04 03:22:39.754452"
latest: "0.10.0--py311haab0aaa_0"
container_url: "https://biocontainers.pro/tools/pegasusio"
aliases:
 - "pegasusio"
 - "natsort"
 - "mirror_server"
 - "mirror_server_stop"
 - "f2py3.9"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "h5clear"
 - "h5format_convert"
 - "h5watch"
versions:
 - "0.5.0--py39h38f01e4_0"
 - "0.9.0--py38he5da3d1_0"
 - "0.8.1--py310h4b81fae_0"
 - "0.7.1--py39hbf8eff0_1"
 - "0.6.2--py37h8902056_0"
 - "0.5.1.post1--py37h8902056_2"
 - "0.9.1--py38h0020b31_1"
 - "0.9.1--py311haab0aaa_2"
 - "0.10.0--py311haab0aaa_0"
description: "shpc-registry automated BioContainers addition for pegasusio"
config: {"url": "https://biocontainers.pro/tools/pegasusio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pegasusio", "latest": {"0.10.0--py311haab0aaa_0": "sha256:513e91e80ef55e8c8b29490387955d258908c69bc5cf2ce9f740baad741343a2"}, "tags": {"0.5.0--py39h38f01e4_0": "sha256:661d999a3ff8fc343d8d85e8313be7ead9827680d4a2918202b013bc4f55a5b8", "0.9.0--py38he5da3d1_0": "sha256:ea762655eb2cb9ce7312f9e93850a13ca59611c290533b7223529c25374c401b", "0.8.1--py310h4b81fae_0": "sha256:38df9a85d5d0a0fdfb55d50d761101ef770f2b4db2fb8095402022ae6d0871ec", "0.7.1--py39hbf8eff0_1": "sha256:adb47c6a71e07cd4084940b948e881f297663b240e3c1419ac698655b7df2b78", "0.6.2--py37h8902056_0": "sha256:ddc9de5399ca514b325ff279881d4789ca465fbaf8630eef76fe6c5e9e3c424f", "0.5.1.post1--py37h8902056_2": "sha256:2151a33f562faf35a3460018851c2a4a6638817071b0dc62f8aac9120188987d", "0.9.1--py38h0020b31_1": "sha256:73c552938e580b02b398c3c9775194aed133fdc9338daf7509b6d6a9f3756244", "0.9.1--py311haab0aaa_2": "sha256:215e9768e7697c3339d29a432fe93b86c25b21fb7adc52c37e8d9fba45b865ce", "0.10.0--py311haab0aaa_0": "sha256:513e91e80ef55e8c8b29490387955d258908c69bc5cf2ce9f740baad741343a2"}, "docker": "quay.io/biocontainers/pegasusio", "aliases": {"pegasusio": "/usr/local/bin/pegasusio", "natsort": "/usr/local/bin/natsort", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "h5clear": "/usr/local/bin/h5clear", "h5format_convert": "/usr/local/bin/h5format_convert", "h5watch": "/usr/local/bin/h5watch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pegasusio.
shpc-registry automated BioContainers addition for pegasusio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pegasusio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pegasusio:0.10.0--py311haab0aaa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pegasusio/0.10.0--py311haab0aaa_0
$ module help quay.io/biocontainers/pegasusio/0.10.0--py311haab0aaa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pegasusio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pegasusio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pegasusio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pegasusio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pegasusio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pegasusio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pegasusio

```bash
$ singularity exec <container> /usr/local/bin/pegasusio
$ podman run --it --rm --entrypoint /usr/local/bin/pegasusio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pegasusio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5clear

```bash
$ singularity exec <container> /usr/local/bin/h5clear
$ podman run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5clear   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5format_convert

```bash
$ singularity exec <container> /usr/local/bin/h5format_convert
$ podman run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5format_convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5watch

```bash
$ singularity exec <container> /usr/local/bin/h5watch
$ podman run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5watch   -v ${PWD} -w ${PWD} <container> -c " $@"
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