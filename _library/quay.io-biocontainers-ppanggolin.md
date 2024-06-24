---
layout: container
name:  "quay.io/biocontainers/ppanggolin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ppanggolin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ppanggolin/container.yaml"
updated_at: "2024-06-24 03:35:16.821478"
latest: "1.2.105--py310h4b81fae_1"
container_url: "https://biocontainers.pro/tools/ppanggolin"
aliases:
 - "gawk-5.0.1"
 - "ppanggolin"
 - "mmseqs"
 - "aragorn"
 - "cmalign"
 - "cmbuild"
 - "cmcalibrate"
 - "cmconvert"
 - "cmemit"
 - "cmfetch"
 - "cmpress"
 - "cmscan"
versions:
 - "v0.3.88--py36h516909a_1"
 - "1.2.74--py38hbff2b2d_1"
 - "1.1.136--py37h73a75cf_1"
 - "1.0.13--py36h516909a_0"
 - "1.2.105--py39hbf8eff0_0"
 - "1.2.105--py310h4b81fae_1"
description: "shpc-registry automated BioContainers addition for ppanggolin"
config: {"url": "https://biocontainers.pro/tools/ppanggolin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ppanggolin", "latest": {"1.2.105--py310h4b81fae_1": "sha256:3d6f75af210f47a192485e94f4a2a7eac228036975023306532f70282285a24b"}, "tags": {"v0.3.88--py36h516909a_1": "sha256:042eac580f6968117ee323c4840d0478333a6c0595561c21632b08675b95e54a", "1.2.74--py38hbff2b2d_1": "sha256:cc90238050f7954da4ba0da234a309675acd1b22c55e750b98ac63ba1e537fc3", "1.1.136--py37h73a75cf_1": "sha256:ac677fcb63237c628d8a6d0004eed60b2493919a61402e630f502106e76288c6", "1.0.13--py36h516909a_0": "sha256:383be1b487824b606911306d8d44bda5bf05f201cfdb5e9b57b3d31bd062e171", "1.2.105--py39hbf8eff0_0": "sha256:866d8c387968084e15160ec5e0d9602a4896709bd802a9800e4b0c8c0b42f2ac", "1.2.105--py310h4b81fae_1": "sha256:3d6f75af210f47a192485e94f4a2a7eac228036975023306532f70282285a24b"}, "docker": "quay.io/biocontainers/ppanggolin", "aliases": {"gawk-5.0.1": "/usr/local/bin/gawk-5.0.1", "ppanggolin": "/usr/local/bin/ppanggolin", "mmseqs": "/usr/local/bin/mmseqs", "aragorn": "/usr/local/bin/aragorn", "cmalign": "/usr/local/bin/cmalign", "cmbuild": "/usr/local/bin/cmbuild", "cmcalibrate": "/usr/local/bin/cmcalibrate", "cmconvert": "/usr/local/bin/cmconvert", "cmemit": "/usr/local/bin/cmemit", "cmfetch": "/usr/local/bin/cmfetch", "cmpress": "/usr/local/bin/cmpress", "cmscan": "/usr/local/bin/cmscan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ppanggolin.
shpc-registry automated BioContainers addition for ppanggolin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ppanggolin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ppanggolin:1.2.105--py310h4b81fae_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ppanggolin/1.2.105--py310h4b81fae_1
$ module help quay.io/biocontainers/ppanggolin/1.2.105--py310h4b81fae_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ppanggolin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ppanggolin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ppanggolin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ppanggolin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ppanggolin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ppanggolin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gawk-5.0.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.0.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.0.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.0.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ppanggolin

```bash
$ singularity exec <container> /usr/local/bin/ppanggolin
$ podman run --it --rm --entrypoint /usr/local/bin/ppanggolin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ppanggolin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmseqs

```bash
$ singularity exec <container> /usr/local/bin/mmseqs
$ podman run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aragorn

```bash
$ singularity exec <container> /usr/local/bin/aragorn
$ podman run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aragorn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmalign

```bash
$ singularity exec <container> /usr/local/bin/cmalign
$ podman run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmbuild

```bash
$ singularity exec <container> /usr/local/bin/cmbuild
$ podman run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmcalibrate

```bash
$ singularity exec <container> /usr/local/bin/cmcalibrate
$ podman run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmconvert

```bash
$ singularity exec <container> /usr/local/bin/cmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmemit

```bash
$ singularity exec <container> /usr/local/bin/cmemit
$ podman run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfetch

```bash
$ singularity exec <container> /usr/local/bin/cmfetch
$ podman run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpress

```bash
$ singularity exec <container> /usr/local/bin/cmpress
$ podman run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmscan

```bash
$ singularity exec <container> /usr/local/bin/cmscan
$ podman run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
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