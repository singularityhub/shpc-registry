---
layout: container
name:  "quay.io/biocontainers/superdsm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/superdsm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/superdsm/container.yaml"
updated_at: "2025-10-20 03:25:39.518300"
latest: "0.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/superdsm"
aliases:
 - "corepack"
 - "dask"
 - "dav1d"
 - "dsdp5"
 - "gpustat"
 - "node"
 - "npm"
 - "npx"
 - "py-spy"
 - "ray"
 - "virtualenv"
 - "tiff2fsspec"
 - "aomdec"
 - "aomenc"
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
 - "imageio_download_bin"
 - "imageio_remove_bin"
 - "skivi"
 - "hwloc-gather-cpuid"
 - "hwloc-annotate"
 - "hwloc-bind"
 - "hwloc-calc"
 - "hwloc-compress-dir"
 - "hwloc-diff"
 - "hwloc-distrib"
 - "hwloc-gather-topology"
versions:
 - "0.1--pyhdfd78af_0"
 - "0.1.3--pyhdfd78af_1"
 - "0.2.0--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for superdsm"
config: {"url": "https://biocontainers.pro/tools/superdsm", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for superdsm", "latest": {"0.4.0--pyhdfd78af_0": "sha256:d2208db79cb7b3bda889706abf2456b4c923f8662f8271feeb31684e2d442cec"}, "tags": {"0.1--pyhdfd78af_0": "sha256:46b2af7c92f0621815d8fc6e4bdf853bcd72a3aef4ab04da8f5cdbe635e12efa", "0.1.3--pyhdfd78af_1": "sha256:9fb485080d519378158373c13bbca971e96b4277502fb69cf8408cbd550ca65d", "0.2.0--pyhdfd78af_0": "sha256:7bd6a8a422687499b403e7d176c1b260b93fef254869cee24757c25738f99972", "0.3.0--pyhdfd78af_0": "sha256:b9c9c74afbe748324957f05275993fd692124965aee44311cd71695102a4ddc8", "0.4.0--pyhdfd78af_0": "sha256:d2208db79cb7b3bda889706abf2456b4c923f8662f8271feeb31684e2d442cec"}, "docker": "quay.io/biocontainers/superdsm", "aliases": {"corepack": "/usr/local/bin/corepack", "dask": "/usr/local/bin/dask", "dav1d": "/usr/local/bin/dav1d", "dsdp5": "/usr/local/bin/dsdp5", "gpustat": "/usr/local/bin/gpustat", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "npx": "/usr/local/bin/npx", "py-spy": "/usr/local/bin/py-spy", "ray": "/usr/local/bin/ray", "virtualenv": "/usr/local/bin/virtualenv", "tiff2fsspec": "/usr/local/bin/tiff2fsspec", "aomdec": "/usr/local/bin/aomdec", "aomenc": "/usr/local/bin/aomenc", "tiffcomment": "/usr/local/bin/tiffcomment", "JxrDecApp": "/usr/local/bin/JxrDecApp", "JxrEncApp": "/usr/local/bin/JxrEncApp", "cbrunsli": "/usr/local/bin/cbrunsli", "dbrunsli": "/usr/local/bin/dbrunsli", "imagecodecs": "/usr/local/bin/imagecodecs", "lsm2bin": "/usr/local/bin/lsm2bin", "tifffile": "/usr/local/bin/tifffile", "zfp": "/usr/local/bin/zfp", "zopfli": "/usr/local/bin/zopfli", "zopflipng": "/usr/local/bin/zopflipng", "imageio_download_bin": "/usr/local/bin/imageio_download_bin", "imageio_remove_bin": "/usr/local/bin/imageio_remove_bin", "skivi": "/usr/local/bin/skivi", "hwloc-gather-cpuid": "/usr/local/bin/hwloc-gather-cpuid", "hwloc-annotate": "/usr/local/bin/hwloc-annotate", "hwloc-bind": "/usr/local/bin/hwloc-bind", "hwloc-calc": "/usr/local/bin/hwloc-calc", "hwloc-compress-dir": "/usr/local/bin/hwloc-compress-dir", "hwloc-diff": "/usr/local/bin/hwloc-diff", "hwloc-distrib": "/usr/local/bin/hwloc-distrib", "hwloc-gather-topology": "/usr/local/bin/hwloc-gather-topology"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/superdsm.
singularity registry hpc automated addition for superdsm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/superdsm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/superdsm:0.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/superdsm/0.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/superdsm/0.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### superdsm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### superdsm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### superdsm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### superdsm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### superdsm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### superdsm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dask

```bash
$ singularity exec <container> /usr/local/bin/dask
$ podman run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dav1d

```bash
$ singularity exec <container> /usr/local/bin/dav1d
$ podman run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dav1d   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dsdp5

```bash
$ singularity exec <container> /usr/local/bin/dsdp5
$ podman run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dsdp5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpustat

```bash
$ singularity exec <container> /usr/local/bin/gpustat
$ podman run --it --rm --entrypoint /usr/local/bin/gpustat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpustat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### node

```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm

```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py-spy

```bash
$ singularity exec <container> /usr/local/bin/py-spy
$ podman run --it --rm --entrypoint /usr/local/bin/py-spy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py-spy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ray

```bash
$ singularity exec <container> /usr/local/bin/ray
$ podman run --it --rm --entrypoint /usr/local/bin/ray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virtualenv

```bash
$ singularity exec <container> /usr/local/bin/virtualenv
$ podman run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tiff2fsspec

```bash
$ singularity exec <container> /usr/local/bin/tiff2fsspec
$ podman run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tiff2fsspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomdec

```bash
$ singularity exec <container> /usr/local/bin/aomdec
$ podman run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomdec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aomenc

```bash
$ singularity exec <container> /usr/local/bin/aomenc
$ podman run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aomenc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### imageio_download_bin

```bash
$ singularity exec <container> /usr/local/bin/imageio_download_bin
$ podman run --it --rm --entrypoint /usr/local/bin/imageio_download_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imageio_download_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imageio_remove_bin

```bash
$ singularity exec <container> /usr/local/bin/imageio_remove_bin
$ podman run --it --rm --entrypoint /usr/local/bin/imageio_remove_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imageio_remove_bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### skivi

```bash
$ singularity exec <container> /usr/local/bin/skivi
$ podman run --it --rm --entrypoint /usr/local/bin/skivi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/skivi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-cpuid

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-cpuid
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-cpuid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-annotate

```bash
$ singularity exec <container> /usr/local/bin/hwloc-annotate
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-annotate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-bind

```bash
$ singularity exec <container> /usr/local/bin/hwloc-bind
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-bind   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-calc

```bash
$ singularity exec <container> /usr/local/bin/hwloc-calc
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-calc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-compress-dir

```bash
$ singularity exec <container> /usr/local/bin/hwloc-compress-dir
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-compress-dir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-diff

```bash
$ singularity exec <container> /usr/local/bin/hwloc-diff
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-distrib

```bash
$ singularity exec <container> /usr/local/bin/hwloc-distrib
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-distrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hwloc-gather-topology

```bash
$ singularity exec <container> /usr/local/bin/hwloc-gather-topology
$ podman run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hwloc-gather-topology   -v ${PWD} -w ${PWD} <container> -c " $@"
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