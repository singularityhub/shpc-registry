---
layout: container
name:  "quay.io/biocontainers/fuc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fuc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fuc/container.yaml"
updated_at: "2025-01-23 03:25:04.297094"
latest: "0.38.0--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/fuc"
aliases:
 - "fuc"
 - "tabulate"
 - "natsort"
 - "xslt-config"
 - "xsltproc"
 - "f2py3.9"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "2to3-3.9"
 - "idle3.9"
versions:
 - "0.9.0--pyh5e36f6f_0"
 - "0.36.0--pyh5e36f6f_0"
 - "0.35.0--pyh5e36f6f_0"
 - "0.34.0--pyh5e36f6f_0"
 - "0.33.1--pyh5e36f6f_0"
 - "0.32.0--pyh5e36f6f_0"
 - "0.37.0--pyh7cba7a3_0"
 - "0.38.0--pyh7e72e81_0"
description: "shpc-registry automated BioContainers addition for fuc"
config: {"url": "https://biocontainers.pro/tools/fuc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fuc", "latest": {"0.38.0--pyh7e72e81_0": "sha256:3c01bfaf6e8200f1dd7ed0a610a985aee6e074f4dda2714ad57ca156f8d27408"}, "tags": {"0.9.0--pyh5e36f6f_0": "sha256:483a1c3e35eb1653ef635d93fca4c17ab9bd787302967177c5bd176a48a190af", "0.36.0--pyh5e36f6f_0": "sha256:26ed9446f1bbe96fb72f0e05c378a0cb76eb7f35ae15ac091f7e8af7576857d3", "0.35.0--pyh5e36f6f_0": "sha256:9113b4a6bcf6e404e5907b373f7188c22a8db1e95c354ce487d83c91c2e0562a", "0.34.0--pyh5e36f6f_0": "sha256:943592f2da83decdcec4df86d3f31cabfd0839749c60f782676564199179ed09", "0.33.1--pyh5e36f6f_0": "sha256:aa7dbe054bc0a250daee81328a8841af3d5bf8dd9cec990b813ff756db590750", "0.32.0--pyh5e36f6f_0": "sha256:be45359dbbb969b18b55dd895971f1c31a928e05c0b74de6fb43d72a82d8ff6c", "0.37.0--pyh7cba7a3_0": "sha256:f056c0b0db67e1e714b3129545c44ce5c9355ec97b2923322fc2ebef151503ce", "0.38.0--pyh7e72e81_0": "sha256:3c01bfaf6e8200f1dd7ed0a610a985aee6e074f4dda2714ad57ca156f8d27408"}, "docker": "quay.io/biocontainers/fuc", "aliases": {"fuc": "/usr/local/bin/fuc", "tabulate": "/usr/local/bin/tabulate", "natsort": "/usr/local/bin/natsort", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "f2py3.9": "/usr/local/bin/f2py3.9", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fuc.
shpc-registry automated BioContainers addition for fuc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fuc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fuc:0.38.0--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fuc/0.38.0--pyh7e72e81_0
$ module help quay.io/biocontainers/fuc/0.38.0--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fuc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fuc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fuc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fuc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fuc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fuc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fuc

```bash
$ singularity exec <container> /usr/local/bin/fuc
$ podman run --it --rm --entrypoint /usr/local/bin/fuc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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