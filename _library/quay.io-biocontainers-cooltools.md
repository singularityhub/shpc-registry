---
layout: container
name:  "quay.io/biocontainers/cooltools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cooltools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cooltools/container.yaml"
updated_at: "2025-05-01 03:29:43.091994"
latest: "0.7.1--py312hc9302aa_2"
container_url: "https://biocontainers.pro/tools/cooltools"
aliases:
 - "cooltools"
 - "tiff2fsspec"
 - "tiffcomment"
 - "JxrDecApp"
 - "JxrEncApp"
 - "cbrunsli"
 - "dbrunsli"
 - "imagecodecs"
 - "lsm2bin"
 - "tifffile"
 - "zfp"
 - "zopfli"
 - "zopflipng"
versions:
 - "0.5.1--py37h37892f8_1"
 - "0.5.2--py39h5371cbf_1"
 - "0.5.4--py310h1425a21_0"
 - "0.5.4--py38he5da3d1_1"
 - "0.6.1--py310h4b81fae_0"
 - "0.5.4--py38he5da3d1_2"
 - "0.7.0--py310hd6be1da_1"
 - "0.7.0--py311h1abe8b6_2"
 - "0.7.1--py311h1abe8b6_0"
 - "0.7.1--py310h20b60a1_1"
 - "0.7.1--py312hc9302aa_2"
description: "shpc-registry automated BioContainers addition for cooltools"
config: {"url": "https://biocontainers.pro/tools/cooltools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cooltools", "latest": {"0.7.1--py312hc9302aa_2": "sha256:a240d06deb42e5ff1ebad6ed1a8d2cdb66d20438e6a013df0e1c1878fba0cfd0"}, "tags": {"0.5.1--py37h37892f8_1": "sha256:84794ab72277c275326b75ca7a62a0bb7ed7d7dab600ed470df14bb9a9db45a0", "0.5.2--py39h5371cbf_1": "sha256:5222c15e76def0f9472cbaf8a5bb5f4f1fca48beb99349478c9503868d4ffb34", "0.5.4--py310h1425a21_0": "sha256:e6df06d651813a6b919dcc80aa48b1fa68a50605aeaec9c4b7ad8649df506785", "0.5.4--py38he5da3d1_1": "sha256:139e52cf9ade369d0458cf9961f010792dafb22d2ba5e57ee359a2723c672164", "0.6.1--py310h4b81fae_0": "sha256:0c61bbb0b34ad2ed6e83688fb972e8a9ae7c5627094c34fae2e0da2d10dee9e4", "0.5.4--py38he5da3d1_2": "sha256:1d86907547078b8b70d334f9ddf269fc59024bf32bcf7c2f5af19c27929e6f2c", "0.7.0--py310hd6be1da_1": "sha256:45f08644b253e2b2df2c77c404984e98353558cf7a043a9c1b0f35810f16b2da", "0.7.0--py311h1abe8b6_2": "sha256:32e78771662ffe95b23d060e4e1cdce89e429d283fedf5f99c9e275ed8e26654", "0.7.1--py311h1abe8b6_0": "sha256:38ce428f3eea6be383d9b3d3805896de460c7c64100e4a3e5c49146f9f714f35", "0.7.1--py310h20b60a1_1": "sha256:bb6a4bd33fe5f2bbefd02b37c44cbb8f36bd147a57a23f8bac0e848586d22ef8", "0.7.1--py312hc9302aa_2": "sha256:a240d06deb42e5ff1ebad6ed1a8d2cdb66d20438e6a013df0e1c1878fba0cfd0"}, "docker": "quay.io/biocontainers/cooltools", "aliases": {"cooltools": "/usr/local/bin/cooltools", "tiff2fsspec": "/usr/local/bin/tiff2fsspec", "tiffcomment": "/usr/local/bin/tiffcomment", "JxrDecApp": "/usr/local/bin/JxrDecApp", "JxrEncApp": "/usr/local/bin/JxrEncApp", "cbrunsli": "/usr/local/bin/cbrunsli", "dbrunsli": "/usr/local/bin/dbrunsli", "imagecodecs": "/usr/local/bin/imagecodecs", "lsm2bin": "/usr/local/bin/lsm2bin", "tifffile": "/usr/local/bin/tifffile", "zfp": "/usr/local/bin/zfp", "zopfli": "/usr/local/bin/zopfli", "zopflipng": "/usr/local/bin/zopflipng"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cooltools.
shpc-registry automated BioContainers addition for cooltools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cooltools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cooltools:0.7.1--py312hc9302aa_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cooltools/0.7.1--py312hc9302aa_2
$ module help quay.io/biocontainers/cooltools/0.7.1--py312hc9302aa_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cooltools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cooltools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cooltools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cooltools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cooltools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cooltools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cooltools

```bash
$ singularity exec <container> /usr/local/bin/cooltools
$ podman run --it --rm --entrypoint /usr/local/bin/cooltools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cooltools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2fsspec

```bash
$ singularity exec <container> /usr/local/bin/tiff2fsspec
$ podman run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiffcomment

```bash
$ singularity exec <container> /usr/local/bin/tiffcomment
$ podman run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiffcomment   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrDecApp

```bash
$ singularity exec <container> /usr/local/bin/JxrDecApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrDecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JxrEncApp

```bash
$ singularity exec <container> /usr/local/bin/JxrEncApp
$ podman run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JxrEncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cbrunsli

```bash
$ singularity exec <container> /usr/local/bin/cbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbrunsli

```bash
$ singularity exec <container> /usr/local/bin/dbrunsli
$ podman run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbrunsli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imagecodecs

```bash
$ singularity exec <container> /usr/local/bin/imagecodecs
$ podman run --it --rm --entrypoint /usr/local/bin/imagecodecs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imagecodecs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lsm2bin

```bash
$ singularity exec <container> /usr/local/bin/lsm2bin
$ podman run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lsm2bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tifffile

```bash
$ singularity exec <container> /usr/local/bin/tifffile
$ podman run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tifffile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfp

```bash
$ singularity exec <container> /usr/local/bin/zfp
$ podman run --it --rm --entrypoint /usr/local/bin/zfp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zopfli

```bash
$ singularity exec <container> /usr/local/bin/zopfli
$ podman run --it --rm --entrypoint /usr/local/bin/zopfli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zopfli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zopflipng

```bash
$ singularity exec <container> /usr/local/bin/zopflipng
$ podman run --it --rm --entrypoint /usr/local/bin/zopflipng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zopflipng   -v ${PWD} -w ${PWD} <container> -c " $@"
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