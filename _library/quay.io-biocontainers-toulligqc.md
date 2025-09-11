---
layout: container
name:  "quay.io/biocontainers/toulligqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/toulligqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/toulligqc/container.yaml"
updated_at: "2025-09-11 03:45:00.622952"
latest: "2.7.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/toulligqc"
aliases:
 - "toulligqc"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.10"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "h5clear"
versions:
 - "2.2.2--pyhdfd78af_0"
 - "2.2.3--pyhdfd78af_0"
 - "2.3--pyhdfd78af_0"
 - "2.4--pyhdfd78af_0"
 - "2.5--pyhdfd78af_0"
 - "2.5.2--pyhdfd78af_0"
 - "2.7.1--pyhdfd78af_0"
 - "2.5.6--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for toulligqc"
config: {"url": "https://biocontainers.pro/tools/toulligqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for toulligqc", "latest": {"2.7.1--pyhdfd78af_0": "sha256:0a921ad2eb512b02e07ef07094f52bb55086da8937952b0fed0e20d9e424e70b"}, "tags": {"2.2.2--pyhdfd78af_0": "sha256:57b6eb1361c01302a4182e0ecb71de2fa16331a5e002be1e0018076896785560", "2.2.3--pyhdfd78af_0": "sha256:f4f5a10e5e0509d48d34d7f88c85109fe499d06cbe8b5d757e8b69c682715110", "2.3--pyhdfd78af_0": "sha256:f85195bb16da9c6ce9d319432f497c23a8c00930d658aeda17407f5a5811baa8", "2.4--pyhdfd78af_0": "sha256:39de3a9f8f8f136c6d3af2f36b7e8110e6ecc7d025e6806e6f6e75b805551430", "2.5--pyhdfd78af_0": "sha256:e163c52d8492729783f35005c675170219b90307e0f1fd43e488185633837381", "2.5.2--pyhdfd78af_0": "sha256:14c9665d824439441f21411721496aa601d082f683d9ec2587e80fa25d762058", "2.7.1--pyhdfd78af_0": "sha256:0a921ad2eb512b02e07ef07094f52bb55086da8937952b0fed0e20d9e424e70b", "2.5.6--pyhdfd78af_0": "sha256:0eb81d26798f4b710fbaedfef8157edfc3baedc1c58eda3ac93a29f48884fa96"}, "docker": "quay.io/biocontainers/toulligqc", "aliases": {"toulligqc": "/usr/local/bin/toulligqc", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "h5clear": "/usr/local/bin/h5clear"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/toulligqc.
shpc-registry automated BioContainers addition for toulligqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/toulligqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/toulligqc:2.7.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/toulligqc/2.7.1--pyhdfd78af_0
$ module help quay.io/biocontainers/toulligqc/2.7.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### toulligqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### toulligqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### toulligqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### toulligqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### toulligqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### toulligqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### toulligqc

```bash
$ singularity exec <container> /usr/local/bin/toulligqc
$ podman run --it --rm --entrypoint /usr/local/bin/toulligqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/toulligqc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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