---
layout: container
name:  "quay.io/biocontainers/bioconductor-targetsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-targetsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-targetsearch/container.yaml"
updated_at: "2024-10-15 03:08:35.862170"
latest: "2.4.1--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-targetsearch"
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
 - "1.50.1--r41hc0cfd56_1"
 - "2.0.0--r42hc0cfd56_0"
 - "2.0.0--r42ha9d7317_2"
 - "2.2.0--r43ha9d7317_0"
 - "2.4.1--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-targetsearch"
config: {"url": "https://biocontainers.pro/tools/bioconductor-targetsearch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-targetsearch", "latest": {"2.4.1--r43ha9d7317_1": "sha256:4e1cf675775f4a82cf0c56aac8eac91611107ac0fe0776e3dbed3faf9c14f61e"}, "tags": {"1.50.1--r41hc0cfd56_1": "sha256:030f627cdc84a6349e1a7cc56810f259f559c52858aca99aee1cfdfa766f0d00", "2.0.0--r42hc0cfd56_0": "sha256:245f206a795316a3f7378813f463d10de0b4f48e1d822c264152c813ba16a3e2", "2.0.0--r42ha9d7317_2": "sha256:8530ec287e955ebf292684fdeac119eb02204fabbc20a2a25345c64a7ae06c74", "2.2.0--r43ha9d7317_0": "sha256:77f4fc9745020b4aeaf601ddcead5042afebe8d637fc9e9a4012d55d7c0cf491", "2.4.1--r43ha9d7317_1": "sha256:4e1cf675775f4a82cf0c56aac8eac91611107ac0fe0776e3dbed3faf9c14f61e"}, "docker": "quay.io/biocontainers/bioconductor-targetsearch", "aliases": {"zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-targetsearch.
shpc-registry automated BioContainers addition for bioconductor-targetsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-targetsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-targetsearch:2.4.1--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-targetsearch/2.4.1--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-targetsearch/2.4.1--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-targetsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-targetsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-targetsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-targetsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-targetsearch-inspect-deffile:

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