---
layout: container
name:  "quay.io/biocontainers/pcasuite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pcasuite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pcasuite/container.yaml"
updated_at: "2025-02-03 02:57:34.361410"
latest: "1.0.0--h7baada4_5"
container_url: "https://biocontainers.pro/tools/pcasuite"
aliases:
 - "bison"
 - "flex"
 - "flex++"
 - "genpcz"
 - "m4"
 - "pcaunzip"
 - "pcazip"
 - "pczdump"
 - "yacc"
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
 - "1.0.0--h52efb1e_1"
 - "1.0.0--h52efb1e_2"
 - "1.0.0--h27c8258_3"
 - "1.0.0--hc018b49_4"
 - "1.0.0--h7baada4_5"
description: "singularity registry hpc automated addition for pcasuite"
config: {"url": "https://biocontainers.pro/tools/pcasuite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pcasuite", "latest": {"1.0.0--h7baada4_5": "sha256:1c5df860e2666234027ab810c86bb893124223c531a308ddc641d7587af9ed21"}, "tags": {"1.0.0--h52efb1e_1": "sha256:acc77c9379704b671b27c4a5d2ace64c935aa91ec9f2fcb6c37b17085a8021f9", "1.0.0--h52efb1e_2": "sha256:7ccc05f63410969619e2f6b032970045eff3ed13380188772e24cd48b7d8c1c8", "1.0.0--h27c8258_3": "sha256:39eea2a0286b564b9191b4591a6bec6ab23fcddd3c5da45d20c475cca98d9adc", "1.0.0--hc018b49_4": "sha256:dcfabdf805ef241c04cd6b0c0ba01d3dd256ad48dbd16a389168138e36dab5b5", "1.0.0--h7baada4_5": "sha256:1c5df860e2666234027ab810c86bb893124223c531a308ddc641d7587af9ed21"}, "docker": "quay.io/biocontainers/pcasuite", "aliases": {"bison": "/usr/local/bin/bison", "flex": "/usr/local/bin/flex", "flex++": "/usr/local/bin/flex++", "genpcz": "/usr/local/bin/genpcz", "m4": "/usr/local/bin/m4", "pcaunzip": "/usr/local/bin/pcaunzip", "pcazip": "/usr/local/bin/pcazip", "pczdump": "/usr/local/bin/pczdump", "yacc": "/usr/local/bin/yacc", "zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif", "hdf2jpeg": "/usr/local/bin/hdf2jpeg", "hdf8to24": "/usr/local/bin/hdf8to24", "hdfcomp": "/usr/local/bin/hdfcomp", "hdfed": "/usr/local/bin/hdfed", "hdfimport": "/usr/local/bin/hdfimport", "hdfls": "/usr/local/bin/hdfls", "hdfpack": "/usr/local/bin/hdfpack", "hdftopal": "/usr/local/bin/hdftopal", "hdftor8": "/usr/local/bin/hdftor8", "hdfunpac": "/usr/local/bin/hdfunpac", "hdiff": "/usr/local/bin/hdiff", "hdp": "/usr/local/bin/hdp", "hrepack": "/usr/local/bin/hrepack", "jpeg2hdf": "/usr/local/bin/jpeg2hdf", "paltohdf": "/usr/local/bin/paltohdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pcasuite.
singularity registry hpc automated addition for pcasuite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pcasuite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pcasuite:1.0.0--h7baada4_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pcasuite/1.0.0--h7baada4_5
$ module help quay.io/biocontainers/pcasuite/1.0.0--h7baada4_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pcasuite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pcasuite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pcasuite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pcasuite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pcasuite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pcasuite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bison

```bash
$ singularity exec <container> /usr/local/bin/bison
$ podman run --it --rm --entrypoint /usr/local/bin/bison   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bison   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flex

```bash
$ singularity exec <container> /usr/local/bin/flex
$ podman run --it --rm --entrypoint /usr/local/bin/flex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flex++

```bash
$ singularity exec <container> /usr/local/bin/flex++
$ podman run --it --rm --entrypoint /usr/local/bin/flex++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flex++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genpcz

```bash
$ singularity exec <container> /usr/local/bin/genpcz
$ podman run --it --rm --entrypoint /usr/local/bin/genpcz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genpcz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m4

```bash
$ singularity exec <container> /usr/local/bin/m4
$ podman run --it --rm --entrypoint /usr/local/bin/m4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcaunzip

```bash
$ singularity exec <container> /usr/local/bin/pcaunzip
$ podman run --it --rm --entrypoint /usr/local/bin/pcaunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcaunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcazip

```bash
$ singularity exec <container> /usr/local/bin/pcazip
$ podman run --it --rm --entrypoint /usr/local/bin/pcazip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcazip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pczdump

```bash
$ singularity exec <container> /usr/local/bin/pczdump
$ podman run --it --rm --entrypoint /usr/local/bin/pczdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pczdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yacc

```bash
$ singularity exec <container> /usr/local/bin/yacc
$ podman run --it --rm --entrypoint /usr/local/bin/yacc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yacc   -v ${PWD} -w ${PWD} <container> -c " $@"
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