---
layout: container
name:  "quay.io/biocontainers/pyfish"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyfish/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyfish/container.yaml"
updated_at: "2023-09-13 02:25:06.373754"
latest: "1.0.3--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/pyfish"
aliases:
 - "f2py3.11"
 - "pyfish"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "normalizer"
 - "brotli"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "python3.1"
 - "jpgicc"
 - "linkicc"
 - "psicc"
 - "tificc"
 - "transicc"
versions:
 - "1.0.2--pyh7cba7a3_0"
 - "1.0.3--pyh7cba7a3_0"
description: "singularity registry hpc automated addition for pyfish"
config: {"url": "https://biocontainers.pro/tools/pyfish", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyfish", "latest": {"1.0.3--pyh7cba7a3_0": "sha256:6a114a426187e401b276afdeb2cc6391add69e98e99e0ab9b2fb723fbeda80e1"}, "tags": {"1.0.2--pyh7cba7a3_0": "sha256:780fa592a1ee6ea88b84c230e95e45adddb24fbee1c0208086a77cf33f95c0b9", "1.0.3--pyh7cba7a3_0": "sha256:6a114a426187e401b276afdeb2cc6391add69e98e99e0ab9b2fb723fbeda80e1"}, "docker": "quay.io/biocontainers/pyfish", "aliases": {"f2py3.11": "/usr/local/bin/f2py3.11", "pyfish": "/usr/local/bin/pyfish", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "normalizer": "/usr/local/bin/normalizer", "brotli": "/usr/local/bin/brotli", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "python3.1": "/usr/local/bin/python3.1", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "psicc": "/usr/local/bin/psicc", "tificc": "/usr/local/bin/tificc", "transicc": "/usr/local/bin/transicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyfish.
singularity registry hpc automated addition for pyfish
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyfish
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyfish:1.0.3--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyfish/1.0.3--pyh7cba7a3_0
$ module help quay.io/biocontainers/pyfish/1.0.3--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyfish-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyfish-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyfish-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyfish-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyfish-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyfish-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### f2py3.11

```bash
$ singularity exec <container> /usr/local/bin/f2py3.11
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfish

```bash
$ singularity exec <container> /usr/local/bin/pyfish
$ podman run --it --rm --entrypoint /usr/local/bin/pyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psicc

```bash
$ singularity exec <container> /usr/local/bin/psicc
$ podman run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tificc

```bash
$ singularity exec <container> /usr/local/bin/tificc
$ podman run --it --rm --entrypoint /usr/local/bin/tificc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tificc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transicc

```bash
$ singularity exec <container> /usr/local/bin/transicc
$ podman run --it --rm --entrypoint /usr/local/bin/transicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transicc   -v ${PWD} -w ${PWD} <container> -c " $@"
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