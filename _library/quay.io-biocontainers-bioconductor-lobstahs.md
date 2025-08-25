---
layout: container
name:  "quay.io/biocontainers/bioconductor-lobstahs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lobstahs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lobstahs/container.yaml"
updated_at: "2025-08-25 03:36:01.864624"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lobstahs"
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
 - "1.8.1--r351_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.10.0--r36_1"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lobstahs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lobstahs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lobstahs", "latest": {"1.32.0--r44hdfd78af_0": "sha256:3cd7051b07bba7c8e5258b398433b7a70c8158a0356e3aaf2e70515dfdd19786"}, "tags": {"1.8.1--r351_0": "sha256:6c065229050cf07cbea62153537f970cd6ccaad4a3fef12e9446abd3aacbc4c0", "1.18.0--r41hdfd78af_0": "sha256:c1970749d13cb73649a43d59633537eace7d83fe3f2fb6c67a5f5d8b6384d0f0", "1.16.0--r40hdfd78af_1": "sha256:89b15aef8c8d2995ff6a10fba9a298af6b41c28fcde2c4ea247d5ceb8f617559", "1.14.0--r40_0": "sha256:1ab2b46678970e32fae34ffa240239e12cb73c59c983c0e0389ea309e02a7765", "1.12.0--r36_0": "sha256:9cd46a2a4d50d55e3d12334e1f302cd3786d6f0d260d91da07469d27d2e2bfe7", "1.10.0--r36_1": "sha256:8c031bd9511e268d4ba067a4ddb11486b41f1e5dde08bafecd23eefeec5ecf96", "1.24.0--r42hdfd78af_0": "sha256:9c7787270e90634a0a971d70763bf8081cf8f2d08e018947d9f9c6c0c018db55", "1.26.0--r43hdfd78af_0": "sha256:6887a71cf68ca13c53c742e646043f72e476da5f179bb9b27983e94636dd640b", "1.28.0--r43hdfd78af_0": "sha256:09f92cbb52f53c07434d31fb350807ea562aa02a1e932c06dd2b524596925ac9", "1.32.0--r44hdfd78af_0": "sha256:3cd7051b07bba7c8e5258b398433b7a70c8158a0356e3aaf2e70515dfdd19786"}, "docker": "quay.io/biocontainers/bioconductor-lobstahs", "aliases": {"gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif", "hdf2jpeg": "/usr/local/bin/hdf2jpeg", "hdf8to24": "/usr/local/bin/hdf8to24", "hdfcomp": "/usr/local/bin/hdfcomp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lobstahs.
shpc-registry automated BioContainers addition for bioconductor-lobstahs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lobstahs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lobstahs:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lobstahs/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lobstahs/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lobstahs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lobstahs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lobstahs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lobstahs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lobstahs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lobstahs-inspect-deffile:

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