---
layout: container
name:  "quay.io/biocontainers/bioconductor-pth2o2lipids"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pth2o2lipids/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pth2o2lipids/container.yaml"
updated_at: "2023-09-11 03:02:56.994725"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pth2o2lipids"
aliases:
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
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pth2o2lipids"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pth2o2lipids", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pth2o2lipids", "latest": {"1.26.0--r43hdfd78af_0": "sha256:9c11ca652a4a0b27b507ba7ea020ec51b24288fd5b14df41051d3299df8a6fcd"}, "tags": {"1.8.0--r351_0": "sha256:17ae112b6e99c3d686a1e12495545fbf300b1e88f2f2fd5c42f04796d8a0a679", "1.24.0--r42hdfd78af_0": "sha256:f3ecf0474ab5d4b93f11615f443e89ef65f7889c7efdc0ac5a873fef2eec3c70", "1.20.0--r41hdfd78af_1": "sha256:4f846b685c76d4bf1b23ef5b7f785b6fd6f08bf4fe036856388ebf7d2327ae32", "1.18.0--r41hdfd78af_0": "sha256:60f61625e397d70e706c31092f69ce5b305f934f21430356f23371c734bd5957", "1.16.0--r40hdfd78af_1": "sha256:62dc311ff017e7a6cc2bb4b287344ab352dee1bd05abc7aa12e15e4ea9a376a2", "1.14.0--r40_0": "sha256:d67dd39fa895ac12dbaa20dbc3adf91072ddb2c318ddf881e6db59aeb2e94256", "1.26.0--r43hdfd78af_0": "sha256:9c11ca652a4a0b27b507ba7ea020ec51b24288fd5b14df41051d3299df8a6fcd"}, "docker": "quay.io/biocontainers/bioconductor-pth2o2lipids", "aliases": {"gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif", "hdf2jpeg": "/usr/local/bin/hdf2jpeg", "hdf8to24": "/usr/local/bin/hdf8to24", "hdfcomp": "/usr/local/bin/hdfcomp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pth2o2lipids.
shpc-registry automated BioContainers addition for bioconductor-pth2o2lipids
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pth2o2lipids
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pth2o2lipids:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pth2o2lipids/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pth2o2lipids/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pth2o2lipids-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pth2o2lipids-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pth2o2lipids-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pth2o2lipids-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pth2o2lipids-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pth2o2lipids-inspect-deffile:

```bash
$ singularity inspect -d <container>
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