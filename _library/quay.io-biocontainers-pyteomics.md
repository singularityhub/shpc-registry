---
layout: container
name:  "quay.io/biocontainers/pyteomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyteomics/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pyteomics/container.yaml"
updated_at: "2022-10-29 05:41:51.490706"
latest: "4.5.5--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/pyteomics"
aliases:
 - "2to3-3.10"
 - "brotli"
 - "f2py3.10"
 - "fonttools"
 - "idle3.10"
 - "jpgicc"
 - "linkicc"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
versions:
 - "4.5.5--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for pyteomics"
config: {"url": "https://biocontainers.pro/tools/pyteomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyteomics", "latest": {"4.5.5--pyh5e36f6f_0": "sha256:7e334105042562cf02d3ad1e30672a02a5f7accc49f2b98f1e122e1783a3cda3"}, "tags": {"4.5.5--pyh5e36f6f_0": "sha256:7e334105042562cf02d3ad1e30672a02a5f7accc49f2b98f1e122e1783a3cda3"}, "docker": "quay.io/biocontainers/pyteomics", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "fonttools": "/usr/local/bin/fonttools", "idle3.10": "/usr/local/bin/idle3.10", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyteomics.
shpc-registry automated BioContainers addition for pyteomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyteomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyteomics:4.5.5--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyteomics/4.5.5--pyh5e36f6f_0
$ module help quay.io/biocontainers/pyteomics/4.5.5--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyteomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyteomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyteomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyteomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyteomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyteomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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