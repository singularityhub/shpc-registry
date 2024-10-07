---
layout: container
name:  "quay.io/biocontainers/umi_tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/umi_tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/umi_tools/container.yaml"
updated_at: "2024-10-07 16:46:58.666459"
latest: "1.1.5--py38h0020b31_3"
container_url: "https://biocontainers.pro/tools/umi_tools"
aliases:
 - "umi_tools"
 - "compile-et.pl"
 - "prerr.properties"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "certutil"
 - "nspr-config"
 - "nss-config"
 - "pk12util"
 - "qwebengine_convert_dict"
versions:
 - "1.0.1--py37h516909a_0"
 - "1.1.5--py38he5da3d1_0"
 - "1.0.1--py38h0213d0e_2"
 - "1.1.5--py39hf95cd2a_1"
 - "1.1.5--py39hff71179_2"
 - "1.1.5--py38h0020b31_3"
description: "shpc-registry automated BioContainers addition for umi_tools"
config: {"url": "https://biocontainers.pro/tools/umi_tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for umi_tools", "latest": {"1.1.5--py38h0020b31_3": "sha256:dd609707e292996374dd3be87aa02e35001ba5f0c6152d627d882dc07288cf81"}, "tags": {"1.0.1--py37h516909a_0": "sha256:e2b2d075c8b704fb9a21ac5073ac1364a6e15ec0e25ad74c82ddbc299ad29401", "1.1.5--py38he5da3d1_0": "sha256:2abd15b17306a8369d5a4d2f1190ca474b35b6dd7dd6f95d3853bed998dc0e13", "1.0.1--py38h0213d0e_2": "sha256:b3398e88fed52c35a087b7396cda70e9df49010c6c766d5de66b7693072bdad0", "1.1.5--py39hf95cd2a_1": "sha256:68d4706dd8b470cba7edb1f821d5b12ca0f6ccf5f82587536465927c58e37c5b", "1.1.5--py39hff71179_2": "sha256:2ff326280ceef692585126b7f4369b0ed6cea786b0956b61876de9155e3f0c4f", "1.1.5--py38h0020b31_3": "sha256:dd609707e292996374dd3be87aa02e35001ba5f0c6152d627d882dc07288cf81"}, "docker": "quay.io/biocontainers/umi_tools", "aliases": {"umi_tools": "/usr/local/bin/umi_tools", "compile-et.pl": "/usr/local/bin/compile-et.pl", "prerr.properties": "/usr/local/bin/prerr.properties", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/umi_tools.
shpc-registry automated BioContainers addition for umi_tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/umi_tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/umi_tools:1.1.5--py38h0020b31_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/umi_tools/1.1.5--py38h0020b31_3
$ module help quay.io/biocontainers/umi_tools/1.1.5--py38h0020b31_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### umi_tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### umi_tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### umi_tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### umi_tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### umi_tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### umi_tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### umi_tools

```bash
$ singularity exec <container> /usr/local/bin/umi_tools
$ podman run --it --rm --entrypoint /usr/local/bin/umi_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/umi_tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compile-et.pl

```bash
$ singularity exec <container> /usr/local/bin/compile-et.pl
$ podman run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compile-et.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prerr.properties

```bash
$ singularity exec <container> /usr/local/bin/prerr.properties
$ podman run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prerr.properties   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlpreview

```bash
$ singularity exec <container> /usr/local/bin/qmlpreview
$ podman run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlpreview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvkgen

```bash
$ singularity exec <container> /usr/local/bin/qvkgen
$ podman run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvkgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nspr-config

```bash
$ singularity exec <container> /usr/local/bin/nspr-config
$ podman run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nspr-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nss-config

```bash
$ singularity exec <container> /usr/local/bin/nss-config
$ podman run --it --rm --entrypoint /usr/local/bin/nss-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nss-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pk12util

```bash
$ singularity exec <container> /usr/local/bin/pk12util
$ podman run --it --rm --entrypoint /usr/local/bin/pk12util   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pk12util   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qwebengine_convert_dict

```bash
$ singularity exec <container> /usr/local/bin/qwebengine_convert_dict
$ podman run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
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