---
layout: container
name:  "quay.io/biocontainers/biobb_cmip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_cmip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_cmip/container.yaml"
updated_at: "2024-04-26 02:43:31.834328"
latest: "4.1.1--pyhdfd78af_0"
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
 - "nc3tonc4"
 - "nc4tonc3"
 - "ncinfo"
 - "prepare_structure"
 - "surfnet2binaryGrid"
 - "titration"
 - "watden"
 - "zipcmp"
 - "zipmerge"
 - "ziptool"
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "hdf24to8"
 - "hdf2gif"
versions:
 - "3.7.8--pyhdfd78af_0"
 - "3.9.0--pyhdfd78af_0"
 - "4.0.0--pyhdfd78af_0"
 - "4.1.0--pyhdfd78af_0"
 - "4.1.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biobb_cmip"
config: {"url": "https://biocontainers.pro/tools/biobb_cmip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biobb_cmip", "latest": {"4.1.1--pyhdfd78af_0": "sha256:057aed2c02188fa50b7ab05e5a44c972828958e5f53a4123d0c63c18cff30c70"}, "tags": {"3.7.8--pyhdfd78af_0": "sha256:430bae684bf4158af6eb460f0426f336d4432a38004aaca692262f4ad1040cdc", "3.9.0--pyhdfd78af_0": "sha256:f7e6babe30ef13a969ca483ac69e69f61ff86204d6436545fe9ba75662f223a2", "4.0.0--pyhdfd78af_0": "sha256:a3134922abd70a96bef67cf438b3f782eeb988cc366242f9463c1be5e8709fd6", "4.1.0--pyhdfd78af_0": "sha256:1e24f52fe8b277c0533b4d57fd11622ab1e1193fd0355349766a3bc885dc3b2c", "4.1.1--pyhdfd78af_0": "sha256:057aed2c02188fa50b7ab05e5a44c972828958e5f53a4123d0c63c18cff30c70"}, "docker": "quay.io/biocontainers/biobb_cmip", "aliases": {"avgEpsGrid": "/usr/local/bin/avgEpsGrid", "canal": "/usr/local/bin/canal", "check_structure": "/usr/local/bin/check_structure", "cmip": "/usr/local/bin/cmip", "getPatch": "/usr/local/bin/getPatch", "grd2cube": "/usr/local/bin/grd2cube", "gsd": "/usr/local/bin/gsd", "mrcfile-header": "/usr/local/bin/mrcfile-header", "mrcfile-validate": "/usr/local/bin/mrcfile-validate", "nc3tonc4": "/usr/local/bin/nc3tonc4", "nc4tonc3": "/usr/local/bin/nc4tonc3", "ncinfo": "/usr/local/bin/ncinfo", "prepare_structure": "/usr/local/bin/prepare_structure", "surfnet2binaryGrid": "/usr/local/bin/surfnet2binaryGrid", "titration": "/usr/local/bin/titration", "watden": "/usr/local/bin/watden", "zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_cmip.
shpc-registry automated BioContainers addition for biobb_cmip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_cmip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_cmip:4.1.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_cmip/4.1.1--pyhdfd78af_0
$ module help quay.io/biocontainers/biobb_cmip/4.1.1--pyhdfd78af_0
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


#### nc3tonc4

```bash
$ singularity exec <container> /usr/local/bin/nc3tonc4
$ podman run --it --rm --entrypoint /usr/local/bin/nc3tonc4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc3tonc4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc4tonc3

```bash
$ singularity exec <container> /usr/local/bin/nc4tonc3
$ podman run --it --rm --entrypoint /usr/local/bin/nc4tonc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4tonc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncinfo

```bash
$ singularity exec <container> /usr/local/bin/ncinfo
$ podman run --it --rm --entrypoint /usr/local/bin/ncinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### zipcmp

```bash
$ singularity exec <container> /usr/local/bin/zipcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipmerge

```bash
$ singularity exec <container> /usr/local/bin/zipmerge
$ podman run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ziptool

```bash
$ singularity exec <container> /usr/local/bin/ziptool
$ podman run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2hdf

```bash
$ singularity exec <container> /usr/local/bin/gif2hdf
$ podman run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncdump

```bash
$ singularity exec <container> /usr/local/bin/h4_ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncgen

```bash
$ singularity exec <container> /usr/local/bin/h4_ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4cc

```bash
$ singularity exec <container> /usr/local/bin/h4cc
$ podman run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4redeploy

```bash
$ singularity exec <container> /usr/local/bin/h4redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf24to8

```bash
$ singularity exec <container> /usr/local/bin/hdf24to8
$ podman run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2gif

```bash
$ singularity exec <container> /usr/local/bin/hdf2gif
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
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