---
layout: container
name:  "quay.io/biocontainers/r-erah"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-erah/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-erah/container.yaml"
updated_at: "2024-09-25 03:17:38.895633"
latest: "2.0.1--r43h21a89ab_0"
container_url: "https://biocontainers.pro/tools/r-erah"
aliases:
 - "h5fuse.sh"
 - "h5delete"
 - "zipcmp"
 - "zipmerge"
 - "ziptool"
 - "hb-info"
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
versions:
 - "1.1.2--r43hdbdd923_0"
 - "2.0.1--r43h21a89ab_0"
description: "singularity registry hpc automated addition for r-erah"
config: {"url": "https://biocontainers.pro/tools/r-erah", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-erah", "latest": {"2.0.1--r43h21a89ab_0": "sha256:a8db4695aecdcf7c0ba1b95cad420a1098273e85ba335651401f70669fc60e6f"}, "tags": {"1.1.2--r43hdbdd923_0": "sha256:ef13ca91c3f24f3d8ad02db0337ca18b1a8ed7c5b4b1cd65faae74faed87bdc6", "2.0.1--r43h21a89ab_0": "sha256:a8db4695aecdcf7c0ba1b95cad420a1098273e85ba335651401f70669fc60e6f"}, "docker": "quay.io/biocontainers/r-erah", "aliases": {"h5fuse.sh": "/usr/local/bin/h5fuse.sh", "h5delete": "/usr/local/bin/h5delete", "zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "hb-info": "/usr/local/bin/hb-info", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif", "hdf2jpeg": "/usr/local/bin/hdf2jpeg", "hdf8to24": "/usr/local/bin/hdf8to24", "hdfcomp": "/usr/local/bin/hdfcomp", "hdfed": "/usr/local/bin/hdfed", "hdfimport": "/usr/local/bin/hdfimport", "hdfls": "/usr/local/bin/hdfls", "hdfpack": "/usr/local/bin/hdfpack", "hdftopal": "/usr/local/bin/hdftopal", "hdftor8": "/usr/local/bin/hdftor8", "hdfunpac": "/usr/local/bin/hdfunpac", "hdiff": "/usr/local/bin/hdiff", "hdp": "/usr/local/bin/hdp", "hrepack": "/usr/local/bin/hrepack"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-erah.
singularity registry hpc automated addition for r-erah
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-erah
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-erah:2.0.1--r43h21a89ab_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-erah/2.0.1--r43h21a89ab_0
$ module help quay.io/biocontainers/r-erah/2.0.1--r43h21a89ab_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-erah-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-erah-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-erah-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-erah-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-erah-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-erah-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5delete

```bash
$ singularity exec <container> /usr/local/bin/h5delete
$ podman run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5delete   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
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