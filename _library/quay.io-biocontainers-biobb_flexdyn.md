---
layout: container
name:  "quay.io/biocontainers/biobb_flexdyn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biobb_flexdyn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biobb_flexdyn/container.yaml"
updated_at: "2023-04-14 03:19:11.684136"
latest: "3.9.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/biobb_flexdyn"
aliases:
 - "NOLB"
 - "concoord_disco"
 - "concoord_dist"
 - "dist"
 - "dist.exe"
 - "evol"
 - "imc"
 - "imod_imode"
 - "imod_imove"
 - "imode_gcc"
 - "imodview"
 - "imove"
 - "nolb_nma"
 - "prody"
 - "prody_anm"
 - "disco"
 - "tjbench"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "normalizer"
 - "f2py3.9"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
 - "jpgicc"
 - "linkicc"
 - "psicc"
 - "tificc"
 - "transicc"
versions:
 - "3.9.0--pyhdfd78af_1"
description: "singularity registry hpc automated addition for biobb_flexdyn"
config: {"url": "https://biocontainers.pro/tools/biobb_flexdyn", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for biobb_flexdyn", "latest": {"3.9.0--pyhdfd78af_1": "sha256:bbbde590c430ece6699d465f7ebd67a3e9f3999f5a5d1921cdb3684d65d78891"}, "tags": {"3.9.0--pyhdfd78af_1": "sha256:bbbde590c430ece6699d465f7ebd67a3e9f3999f5a5d1921cdb3684d65d78891"}, "docker": "quay.io/biocontainers/biobb_flexdyn", "aliases": {"NOLB": "/usr/local/bin/NOLB", "concoord_disco": "/usr/local/bin/concoord_disco", "concoord_dist": "/usr/local/bin/concoord_dist", "dist": "/usr/local/bin/dist", "dist.exe": "/usr/local/bin/dist.exe", "evol": "/usr/local/bin/evol", "imc": "/usr/local/bin/imc", "imod_imode": "/usr/local/bin/imod_imode", "imod_imove": "/usr/local/bin/imod_imove", "imode_gcc": "/usr/local/bin/imode_gcc", "imodview": "/usr/local/bin/imodview", "imove": "/usr/local/bin/imove", "nolb_nma": "/usr/local/bin/nolb_nma", "prody": "/usr/local/bin/prody", "prody_anm": "/usr/local/bin/prody_anm", "disco": "/usr/local/bin/disco", "tjbench": "/usr/local/bin/tjbench", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "normalizer": "/usr/local/bin/normalizer", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "psicc": "/usr/local/bin/psicc", "tificc": "/usr/local/bin/tificc", "transicc": "/usr/local/bin/transicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biobb_flexdyn.
singularity registry hpc automated addition for biobb_flexdyn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biobb_flexdyn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biobb_flexdyn:3.9.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biobb_flexdyn/3.9.0--pyhdfd78af_1
$ module help quay.io/biocontainers/biobb_flexdyn/3.9.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biobb_flexdyn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biobb_flexdyn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biobb_flexdyn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biobb_flexdyn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biobb_flexdyn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biobb_flexdyn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NOLB

```bash
$ singularity exec <container> /usr/local/bin/NOLB
$ podman run --it --rm --entrypoint /usr/local/bin/NOLB   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NOLB   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoord_disco

```bash
$ singularity exec <container> /usr/local/bin/concoord_disco
$ podman run --it --rm --entrypoint /usr/local/bin/concoord_disco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoord_disco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### concoord_dist

```bash
$ singularity exec <container> /usr/local/bin/concoord_dist
$ podman run --it --rm --entrypoint /usr/local/bin/concoord_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/concoord_dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dist

```bash
$ singularity exec <container> /usr/local/bin/dist
$ podman run --it --rm --entrypoint /usr/local/bin/dist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dist.exe

```bash
$ singularity exec <container> /usr/local/bin/dist.exe
$ podman run --it --rm --entrypoint /usr/local/bin/dist.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dist.exe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evol

```bash
$ singularity exec <container> /usr/local/bin/evol
$ podman run --it --rm --entrypoint /usr/local/bin/evol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imc

```bash
$ singularity exec <container> /usr/local/bin/imc
$ podman run --it --rm --entrypoint /usr/local/bin/imc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imod_imode

```bash
$ singularity exec <container> /usr/local/bin/imod_imode
$ podman run --it --rm --entrypoint /usr/local/bin/imod_imode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imod_imode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imod_imove

```bash
$ singularity exec <container> /usr/local/bin/imod_imove
$ podman run --it --rm --entrypoint /usr/local/bin/imod_imove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imod_imove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imode_gcc

```bash
$ singularity exec <container> /usr/local/bin/imode_gcc
$ podman run --it --rm --entrypoint /usr/local/bin/imode_gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imode_gcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imodview

```bash
$ singularity exec <container> /usr/local/bin/imodview
$ podman run --it --rm --entrypoint /usr/local/bin/imodview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imodview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imove

```bash
$ singularity exec <container> /usr/local/bin/imove
$ podman run --it --rm --entrypoint /usr/local/bin/imove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nolb_nma

```bash
$ singularity exec <container> /usr/local/bin/nolb_nma
$ podman run --it --rm --entrypoint /usr/local/bin/nolb_nma   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nolb_nma   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prody

```bash
$ singularity exec <container> /usr/local/bin/prody
$ podman run --it --rm --entrypoint /usr/local/bin/prody   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prody   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prody_anm

```bash
$ singularity exec <container> /usr/local/bin/prody_anm
$ podman run --it --rm --entrypoint /usr/local/bin/prody_anm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prody_anm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### disco

```bash
$ singularity exec <container> /usr/local/bin/disco
$ podman run --it --rm --entrypoint /usr/local/bin/disco   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/disco   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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