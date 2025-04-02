---
layout: container
name:  "quay.io/biocontainers/bioconductor-mobilitytransformr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mobilitytransformr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mobilitytransformr/container.yaml"
updated_at: "2025-04-02 03:06:52.652946"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mobilitytransformr"
aliases:
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
 - "hdf2jpeg"
 - "hdf8to24"
 - "hdfcomp"
 - "hdfed"
 - "hdfimport"
 - "hdfls"
 - "hdfpack"
 - "hdftopal"
 - "hdftor8"
 - "hdfunpac"
 - "hdiff"
 - "hdp"
 - "hrepack"
 - "jpeg2hdf"
 - "paltohdf"
versions:
 - "1.2.0--r42hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-mobilitytransformr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mobilitytransformr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-mobilitytransformr", "latest": {"1.6.0--r43hdfd78af_0": "sha256:9988160d2df6855f585f5e5bb053a99292c65622018144137effaae76b6bddf6"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:e0ee3bc11d065d7ec1af786fdf8887753eb459147ea5e2f40d9f0b2c48d44be2", "1.4.0--r43hdfd78af_0": "sha256:e1ba65a76162fc89d449fab37226eb5e9a763dcc686fd6dda791d8e525ba675e", "1.6.0--r43hdfd78af_0": "sha256:9988160d2df6855f585f5e5bb053a99292c65622018144137effaae76b6bddf6"}, "docker": "quay.io/biocontainers/bioconductor-mobilitytransformr", "aliases": {"zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif", "hdf2jpeg": "/usr/local/bin/hdf2jpeg", "hdf8to24": "/usr/local/bin/hdf8to24", "hdfcomp": "/usr/local/bin/hdfcomp", "hdfed": "/usr/local/bin/hdfed", "hdfimport": "/usr/local/bin/hdfimport", "hdfls": "/usr/local/bin/hdfls", "hdfpack": "/usr/local/bin/hdfpack", "hdftopal": "/usr/local/bin/hdftopal", "hdftor8": "/usr/local/bin/hdftor8", "hdfunpac": "/usr/local/bin/hdfunpac", "hdiff": "/usr/local/bin/hdiff", "hdp": "/usr/local/bin/hdp", "hrepack": "/usr/local/bin/hrepack", "jpeg2hdf": "/usr/local/bin/jpeg2hdf", "paltohdf": "/usr/local/bin/paltohdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mobilitytransformr.
singularity registry hpc automated addition for bioconductor-mobilitytransformr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mobilitytransformr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mobilitytransformr:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mobilitytransformr/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mobilitytransformr/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mobilitytransformr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mobilitytransformr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mobilitytransformr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mobilitytransformr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mobilitytransformr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mobilitytransformr-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### hdf2jpeg

```bash
$ singularity exec <container> /usr/local/bin/hdf2jpeg
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2jpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2jpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf8to24

```bash
$ singularity exec <container> /usr/local/bin/hdf8to24
$ podman run --it --rm --entrypoint /usr/local/bin/hdf8to24   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf8to24   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdfcomp

```bash
$ singularity exec <container> /usr/local/bin/hdfcomp
$ podman run --it --rm --entrypoint /usr/local/bin/hdfcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdfcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdfed

```bash
$ singularity exec <container> /usr/local/bin/hdfed
$ podman run --it --rm --entrypoint /usr/local/bin/hdfed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdfed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdfimport

```bash
$ singularity exec <container> /usr/local/bin/hdfimport
$ podman run --it --rm --entrypoint /usr/local/bin/hdfimport   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdfimport   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdfls

```bash
$ singularity exec <container> /usr/local/bin/hdfls
$ podman run --it --rm --entrypoint /usr/local/bin/hdfls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdfls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdfpack

```bash
$ singularity exec <container> /usr/local/bin/hdfpack
$ podman run --it --rm --entrypoint /usr/local/bin/hdfpack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdfpack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdftopal

```bash
$ singularity exec <container> /usr/local/bin/hdftopal
$ podman run --it --rm --entrypoint /usr/local/bin/hdftopal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdftopal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdftor8

```bash
$ singularity exec <container> /usr/local/bin/hdftor8
$ podman run --it --rm --entrypoint /usr/local/bin/hdftor8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdftor8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdfunpac

```bash
$ singularity exec <container> /usr/local/bin/hdfunpac
$ podman run --it --rm --entrypoint /usr/local/bin/hdfunpac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdfunpac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdiff

```bash
$ singularity exec <container> /usr/local/bin/hdiff
$ podman run --it --rm --entrypoint /usr/local/bin/hdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdp

```bash
$ singularity exec <container> /usr/local/bin/hdp
$ podman run --it --rm --entrypoint /usr/local/bin/hdp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hrepack

```bash
$ singularity exec <container> /usr/local/bin/hrepack
$ podman run --it --rm --entrypoint /usr/local/bin/hrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpeg2hdf

```bash
$ singularity exec <container> /usr/local/bin/jpeg2hdf
$ podman run --it --rm --entrypoint /usr/local/bin/jpeg2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpeg2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paltohdf

```bash
$ singularity exec <container> /usr/local/bin/paltohdf
$ podman run --it --rm --entrypoint /usr/local/bin/paltohdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paltohdf   -v ${PWD} -w ${PWD} <container> -c " $@"
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