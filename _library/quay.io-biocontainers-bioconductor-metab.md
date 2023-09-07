---
layout: container
name:  "quay.io/biocontainers/bioconductor-metab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metab/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metab/container.yaml"
updated_at: "2023-09-07 03:07:41.684558"
latest: "1.33.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metab"
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
versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.33.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metab"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metab", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metab", "latest": {"1.33.0--r43hdfd78af_0": "sha256:3ac53c99f0b7e4fb3a7a7c36d8b3987600bd06984c3347f6bf4e2b4249a0593d"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:34c465eb05a106e0aab626bc27b427ec3032b74273ffa73f2177df12ec5aecb2", "1.32.0--r42hdfd78af_0": "sha256:6aeb1409e928fee6b5a46c111bf4d8480fe710a0cc17eccb5c4cf67a80735698", "1.33.0--r43hdfd78af_0": "sha256:3ac53c99f0b7e4fb3a7a7c36d8b3987600bd06984c3347f6bf4e2b4249a0593d"}, "docker": "quay.io/biocontainers/bioconductor-metab", "aliases": {"zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metab.
shpc-registry automated BioContainers addition for bioconductor-metab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metab:1.33.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metab/1.33.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metab/1.33.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metab-inspect-deffile:

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