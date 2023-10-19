---
layout: container
name:  "quay.io/biocontainers/matchms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/matchms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/matchms/container.yaml"
updated_at: "2023-10-19 02:49:20.673073"
latest: "0.22.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/matchms"
aliases:
 - "numba"
 - "pycc"
 - "normalizer"
 - "xslt-config"
 - "xsltproc"
 - "chardetect"
 - "f2py3.9"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
versions:
 - "0.9.2--pyh5e36f6f_0"
 - "0.17.0--pyh7cba7a3_0"
 - "0.16.0--pyh5e36f6f_0"
 - "0.15.0--pyh5e36f6f_0"
 - "0.14.0--pyh5e36f6f_0"
 - "0.13.0--pyh5e36f6f_0"
 - "0.18.0--pyh7cba7a3_0"
 - "0.19.0--pyh7cba7a3_0"
 - "0.20.0--pyh7cba7a3_0"
 - "0.21.1--pyh7cba7a3_1"
 - "0.22.0--pyhdfd78af_0"
 - "0.21.2--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for matchms"
config: {"url": "https://biocontainers.pro/tools/matchms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for matchms", "latest": {"0.22.0--pyhdfd78af_0": "sha256:5edb5f66bf1f58ca9a08a90130f7f60f0f1ed3e5abed51bba960f83003cb50a6"}, "tags": {"0.9.2--pyh5e36f6f_0": "sha256:d1a8f1d785b8993724305e4684caae5bc194b9fbb99053883eacfead753f20c0", "0.17.0--pyh7cba7a3_0": "sha256:e627c7edc52623413aaaa9a8e0d5ab36745a674a134fc9068ebfca9c2b64fef4", "0.16.0--pyh5e36f6f_0": "sha256:cdf51e0e46be5f20c34b9ab1cb65a91fb2e442816ef18b1a9c7b6f684dc686b9", "0.15.0--pyh5e36f6f_0": "sha256:7eb8d5731823c178bef092c725dcb4c2caebef300ac97c4607ff23bba500602a", "0.14.0--pyh5e36f6f_0": "sha256:99c8f316ffe94fdff131082c7cd6b46034c5d88eacf11dd1d2dc3b752fd688c3", "0.13.0--pyh5e36f6f_0": "sha256:7063e83d9cbf4047af3950a2fa29ec82e374f446ac033cea554759df9517537b", "0.18.0--pyh7cba7a3_0": "sha256:c2ad348646f2dfb3544b4bc63f8c0bc485dc0e41372f6f92789d8c044c830b2b", "0.19.0--pyh7cba7a3_0": "sha256:89953c25bd9b6f146c757f773ffa85fccbbb6e74ad2933d037db7624d33484d6", "0.20.0--pyh7cba7a3_0": "sha256:0f5b62b6f60ee1dcff8fa0312bdeae42eea4bc6e3fdd7de5a5606c09eb4bb176", "0.21.1--pyh7cba7a3_1": "sha256:604aa431ee5865426ba8c5c891b653f87a6ace2ef4edb447d660bccec8205e58", "0.22.0--pyhdfd78af_0": "sha256:5edb5f66bf1f58ca9a08a90130f7f60f0f1ed3e5abed51bba960f83003cb50a6", "0.21.2--pyhdfd78af_0": "sha256:3729fbb9320fdddc713d39e8820b3c6f591206c832712d2ecf30a9b0933e30be"}, "docker": "quay.io/biocontainers/matchms", "aliases": {"numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "normalizer": "/usr/local/bin/normalizer", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "chardetect": "/usr/local/bin/chardetect", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/matchms.
shpc-registry automated BioContainers addition for matchms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/matchms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/matchms:0.22.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/matchms/0.22.0--pyhdfd78af_0
$ module help quay.io/biocontainers/matchms/0.22.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### matchms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### matchms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### matchms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### matchms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### matchms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### matchms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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