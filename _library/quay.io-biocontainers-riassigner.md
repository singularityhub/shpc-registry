---
layout: container
name:  "quay.io/biocontainers/riassigner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/riassigner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/riassigner/container.yaml"
updated_at: "2024-11-05 03:12:22.112055"
latest: "0.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/riassigner"
aliases:
 - "pint-convert"
 - "xml2-config.bak"
 - "numba"
 - "pycc"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "normalizer"
 - "brotli"
 - "xslt-config"
versions:
 - "0.3.3--pyhdfd78af_0"
 - "0.3.3--pyhdfd78af_1"
 - "0.3.4--pyhdfd78af_1"
 - "0.3.4--pyhdfd78af_3"
 - "0.3.4--pyhdfd78af_4"
 - "0.4.0--pyhdfd78af_0"
 - "0.4.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for riassigner"
config: {"url": "https://biocontainers.pro/tools/riassigner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for riassigner", "latest": {"0.4.1--pyhdfd78af_0": "sha256:aca7aba4f86320f335d7e10f907ffea6fff38a54761a5cd170bde39a2f4ada0f"}, "tags": {"0.3.3--pyhdfd78af_0": "sha256:a4b56c866a9df417109b67788662226b2d1a58343891f542175f8592ed207cdc", "0.3.3--pyhdfd78af_1": "sha256:9263cd5da1716f29a0b4733dbc3a9dfa363c856cefd00b3d7d36869aaa141efe", "0.3.4--pyhdfd78af_1": "sha256:40b5ecfc42316878cd886b1c61e43c183e9cfd9cb01e81775b9199c3c3dfaa86", "0.3.4--pyhdfd78af_3": "sha256:18481d1c446b6c9196a60a8de59271331ee5931c2e8e834ca540e5b88a126e33", "0.3.4--pyhdfd78af_4": "sha256:2174d334db75b4b47789eb1b8569d3078fe3a81a143e3a7d3e10e6d4c9594b10", "0.4.0--pyhdfd78af_0": "sha256:8f2bfb3efb5b3ec6f90c6fe50b20145ab5d863002549799930877a148364a15e", "0.4.1--pyhdfd78af_0": "sha256:aca7aba4f86320f335d7e10f907ffea6fff38a54761a5cd170bde39a2f4ada0f"}, "docker": "quay.io/biocontainers/riassigner", "aliases": {"pint-convert": "/usr/local/bin/pint-convert", "xml2-config.bak": "/usr/local/bin/xml2-config.bak", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "normalizer": "/usr/local/bin/normalizer", "brotli": "/usr/local/bin/brotli", "xslt-config": "/usr/local/bin/xslt-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/riassigner.
shpc-registry automated BioContainers addition for riassigner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/riassigner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/riassigner:0.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/riassigner/0.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/riassigner/0.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### riassigner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### riassigner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### riassigner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### riassigner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### riassigner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### riassigner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pint-convert

```bash
$ singularity exec <container> /usr/local/bin/pint-convert
$ podman run --it --rm --entrypoint /usr/local/bin/pint-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pint-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml2-config.bak

```bash
$ singularity exec <container> /usr/local/bin/xml2-config.bak
$ podman run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml2-config.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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