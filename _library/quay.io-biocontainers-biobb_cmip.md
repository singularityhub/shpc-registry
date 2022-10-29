---
layout: container
name:  "quay.io/biocontainers/biobb_cmip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_cmip/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_cmip/container.yaml"
updated_at: "2022-10-29 05:31:48.764858"
latest: "3.7.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biobb_cmip"
aliases:
 - "avgEpsGrid"
 - "canal"
 - "check_structure"
 - "cmip"
 - "getPatch"
 - "grd2cube"
 - "gsd"
 - "mrcfile-header"
 - "mrcfile-validate"
 - "prepare_structure"
 - "surfnet2binaryGrid"
 - "titration"
 - "watden"
 - "2to3-3.7"
 - "brotli"
 - "cwebp"
 - "dwebp"
 - "f2py3.7"
 - "fonttools"
 - "gif2h5"
 - "gif2hdf"
 - "gif2rgb"
 - "gif2webp"
versions:
 - "3.7.8--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_cmip"
config: {"url": "https://biocontainers.pro/tools/biobb_cmip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_cmip", "latest": {"3.7.8--pyhdfd78af_0": "sha256:430bae684bf4158af6eb460f0426f336d4432a38004aaca692262f4ad1040cdc"}, "tags": {"3.7.8--pyhdfd78af_0": "sha256:430bae684bf4158af6eb460f0426f336d4432a38004aaca692262f4ad1040cdc"}, "docker": "quay.io/biocontainers/biobb_cmip", "aliases": {"avgEpsGrid": "/usr/local/bin/avgEpsGrid", "canal": "/usr/local/bin/canal", "check_structure": "/usr/local/bin/check_structure", "cmip": "/usr/local/bin/cmip", "getPatch": "/usr/local/bin/getPatch", "grd2cube": "/usr/local/bin/grd2cube", "gsd": "/usr/local/bin/gsd", "mrcfile-header": "/usr/local/bin/mrcfile-header", "mrcfile-validate": "/usr/local/bin/mrcfile-validate", "prepare_structure": "/usr/local/bin/prepare_structure", "surfnet2binaryGrid": "/usr/local/bin/surfnet2binaryGrid", "titration": "/usr/local/bin/titration", "watden": "/usr/local/bin/watden", "2to3-3.7": "/usr/local/bin/2to3-3.7", "brotli": "/usr/local/bin/brotli", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "f2py3.7": "/usr/local/bin/f2py3.7", "fonttools": "/usr/local/bin/fonttools", "gif2h5": "/usr/local/bin/gif2h5", "gif2hdf": "/usr/local/bin/gif2hdf", "gif2rgb": "/usr/local/bin/gif2rgb", "gif2webp": "/usr/local/bin/gif2webp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_cmip.
shpc-registry automated BioContainers addition for biobb_cmip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_cmip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_cmip:3.7.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_cmip/3.7.8--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_cmip/3.7.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_cmip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_cmip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_cmip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_cmip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_cmip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_cmip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### avgEpsGrid

```bash
$ singularity exec <container> /usr/local/bin/avgEpsGrid
$ podman run --it --rm --entrypoint /usr/local/bin/avgEpsGrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/avgEpsGrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canal

```bash
$ singularity exec <container> /usr/local/bin/canal
$ podman run --it --rm --entrypoint /usr/local/bin/canal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### check_structure

```bash
$ singularity exec <container> /usr/local/bin/check_structure
$ podman run --it --rm --entrypoint /usr/local/bin/check_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmip

```bash
$ singularity exec <container> /usr/local/bin/cmip
$ podman run --it --rm --entrypoint /usr/local/bin/cmip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getPatch

```bash
$ singularity exec <container> /usr/local/bin/getPatch
$ podman run --it --rm --entrypoint /usr/local/bin/getPatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getPatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grd2cube

```bash
$ singularity exec <container> /usr/local/bin/grd2cube
$ podman run --it --rm --entrypoint /usr/local/bin/grd2cube   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grd2cube   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsd

```bash
$ singularity exec <container> /usr/local/bin/gsd
$ podman run --it --rm --entrypoint /usr/local/bin/gsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mrcfile-header

```bash
$ singularity exec <container> /usr/local/bin/mrcfile-header
$ podman run --it --rm --entrypoint /usr/local/bin/mrcfile-header   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mrcfile-header   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mrcfile-validate

```bash
$ singularity exec <container> /usr/local/bin/mrcfile-validate
$ podman run --it --rm --entrypoint /usr/local/bin/mrcfile-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mrcfile-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prepare_structure

```bash
$ singularity exec <container> /usr/local/bin/prepare_structure
$ podman run --it --rm --entrypoint /usr/local/bin/prepare_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prepare_structure   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### surfnet2binaryGrid

```bash
$ singularity exec <container> /usr/local/bin/surfnet2binaryGrid
$ podman run --it --rm --entrypoint /usr/local/bin/surfnet2binaryGrid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/surfnet2binaryGrid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### titration

```bash
$ singularity exec <container> /usr/local/bin/titration
$ podman run --it --rm --entrypoint /usr/local/bin/titration   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/titration   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### watden

```bash
$ singularity exec <container> /usr/local/bin/watden
$ podman run --it --rm --entrypoint /usr/local/bin/watden   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/watden   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.7

```bash
$ singularity exec <container> /usr/local/bin/f2py3.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2hdf

```bash
$ singularity exec <container> /usr/local/bin/gif2hdf
$ podman run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2webp

```bash
$ singularity exec <container> /usr/local/bin/gif2webp
$ podman run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
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