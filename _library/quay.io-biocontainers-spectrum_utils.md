---
layout: container
name:  "quay.io/biocontainers/spectrum_utils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spectrum_utils/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/spectrum_utils/container.yaml"
updated_at: "2022-10-29 05:51:23.434695"
latest: "0.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/spectrum_utils"
aliases:
 - "2to3-3.10"
 - "brotli"
 - "f2py3.10"
 - "fonttools"
 - "idle3.10"
 - "jpgicc"
 - "jsonschema"
 - "linkicc"
 - "numba"
 - "opj_compress"
versions:
 - "0.4.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for spectrum_utils"
config: {"url": "https://biocontainers.pro/tools/spectrum_utils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spectrum_utils", "latest": {"0.4.1--pyhdfd78af_0": "sha256:45459d22a493021f0d988ef7d09b8fefe63947cd0a98e2418d26883c254b2700"}, "tags": {"0.4.1--pyhdfd78af_0": "sha256:45459d22a493021f0d988ef7d09b8fefe63947cd0a98e2418d26883c254b2700"}, "docker": "quay.io/biocontainers/spectrum_utils", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "fonttools": "/usr/local/bin/fonttools", "idle3.10": "/usr/local/bin/idle3.10", "jpgicc": "/usr/local/bin/jpgicc", "jsonschema": "/usr/local/bin/jsonschema", "linkicc": "/usr/local/bin/linkicc", "numba": "/usr/local/bin/numba", "opj_compress": "/usr/local/bin/opj_compress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spectrum_utils.
shpc-registry automated BioContainers addition for spectrum_utils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spectrum_utils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spectrum_utils:0.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spectrum_utils/0.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/spectrum_utils/0.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spectrum_utils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spectrum_utils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spectrum_utils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spectrum_utils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spectrum_utils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spectrum_utils-inspect-deffile:

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


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
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