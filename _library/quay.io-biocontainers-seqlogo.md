---
layout: container
name:  "quay.io/biocontainers/seqlogo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqlogo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqlogo/container.yaml"
updated_at: "2024-10-14 03:42:17.967880"
latest: "5.29.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/seqlogo"
aliases:
 - "transformseq"
 - "weblogo"
 - "dvipdf"
 - "eps2eps"
 - "gs"
 - "gsbj"
 - "gsdj"
 - "gsdj500"
 - "gslj"
 - "gslp"
versions:
 - "5.29.8--py_0"
 - "5.29.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for seqlogo"
config: {"url": "https://biocontainers.pro/tools/seqlogo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqlogo", "latest": {"5.29.9--pyhdfd78af_0": "sha256:388f998ddfda4b7c7b9902a3f9d3de4fc35a59bf0ed2b55ea281d18b026df1a7"}, "tags": {"5.29.8--py_0": "sha256:b1a477d345da2dbeb2c47f560cc75648aca2ef585d6d8c1906efc94e28f51b0d", "5.29.9--pyhdfd78af_0": "sha256:388f998ddfda4b7c7b9902a3f9d3de4fc35a59bf0ed2b55ea281d18b026df1a7"}, "docker": "quay.io/biocontainers/seqlogo", "aliases": {"transformseq": "/usr/local/bin/transformseq", "weblogo": "/usr/local/bin/weblogo", "dvipdf": "/usr/local/bin/dvipdf", "eps2eps": "/usr/local/bin/eps2eps", "gs": "/usr/local/bin/gs", "gsbj": "/usr/local/bin/gsbj", "gsdj": "/usr/local/bin/gsdj", "gsdj500": "/usr/local/bin/gsdj500", "gslj": "/usr/local/bin/gslj", "gslp": "/usr/local/bin/gslp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqlogo.
shpc-registry automated BioContainers addition for seqlogo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqlogo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqlogo:5.29.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqlogo/5.29.9--pyhdfd78af_0
$ module help quay.io/biocontainers/seqlogo/5.29.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqlogo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqlogo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqlogo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqlogo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqlogo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqlogo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### transformseq

```bash
$ singularity exec <container> /usr/local/bin/transformseq
$ podman run --it --rm --entrypoint /usr/local/bin/transformseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### weblogo

```bash
$ singularity exec <container> /usr/local/bin/weblogo
$ podman run --it --rm --entrypoint /usr/local/bin/weblogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weblogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dvipdf

```bash
$ singularity exec <container> /usr/local/bin/dvipdf
$ podman run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eps2eps

```bash
$ singularity exec <container> /usr/local/bin/eps2eps
$ podman run --it --rm --entrypoint /usr/local/bin/eps2eps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eps2eps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gs

```bash
$ singularity exec <container> /usr/local/bin/gs
$ podman run --it --rm --entrypoint /usr/local/bin/gs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsbj

```bash
$ singularity exec <container> /usr/local/bin/gsbj
$ podman run --it --rm --entrypoint /usr/local/bin/gsbj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsbj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsdj

```bash
$ singularity exec <container> /usr/local/bin/gsdj
$ podman run --it --rm --entrypoint /usr/local/bin/gsdj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsdj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsdj500

```bash
$ singularity exec <container> /usr/local/bin/gsdj500
$ podman run --it --rm --entrypoint /usr/local/bin/gsdj500   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsdj500   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gslj

```bash
$ singularity exec <container> /usr/local/bin/gslj
$ podman run --it --rm --entrypoint /usr/local/bin/gslj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gslj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gslp

```bash
$ singularity exec <container> /usr/local/bin/gslp
$ podman run --it --rm --entrypoint /usr/local/bin/gslp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gslp   -v ${PWD} -w ${PWD} <container> -c " $@"
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