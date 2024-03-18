---
layout: container
name:  "quay.io/biocontainers/gat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gat/container.yaml"
updated_at: "2024-03-18 23:24:11.709857"
latest: "1.3.6--py39h87d955d_4"
container_url: "https://biocontainers.pro/tools/gat"
aliases:
 - "gat-compare.py"
 - "gat-great.py"
 - "gat-plot.py"
 - "gat-run.py"
 - "msgattrib"
 - "xkbcli"
 - "pg_config"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "certutil"
 - "nspr-config"
 - "nss-config"
 - "pk12util"
 - "qwebengine_convert_dict"
versions:
 - "1.3.6--py39h87d955d_4"
description: "shpc-registry automated BioContainers addition for gat"
config: {"url": "https://biocontainers.pro/tools/gat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gat", "latest": {"1.3.6--py39h87d955d_4": "sha256:51c4d1e5ae1ff06721294006b523ae4ac1cc20529f312fe30983c9f6bd759707"}, "tags": {"1.3.6--py39h87d955d_4": "sha256:51c4d1e5ae1ff06721294006b523ae4ac1cc20529f312fe30983c9f6bd759707"}, "docker": "quay.io/biocontainers/gat", "aliases": {"gat-compare.py": "/usr/local/bin/gat-compare.py", "gat-great.py": "/usr/local/bin/gat-great.py", "gat-plot.py": "/usr/local/bin/gat-plot.py", "gat-run.py": "/usr/local/bin/gat-run.py", "msgattrib": "/usr/local/bin/msgattrib", "xkbcli": "/usr/local/bin/xkbcli", "pg_config": "/usr/local/bin/pg_config", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gat.
shpc-registry automated BioContainers addition for gat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gat:1.3.6--py39h87d955d_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gat/1.3.6--py39h87d955d_4
$ module help quay.io/biocontainers/gat/1.3.6--py39h87d955d_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gat-compare.py

```bash
$ singularity exec <container> /usr/local/bin/gat-compare.py
$ podman run --it --rm --entrypoint /usr/local/bin/gat-compare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gat-compare.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gat-great.py

```bash
$ singularity exec <container> /usr/local/bin/gat-great.py
$ podman run --it --rm --entrypoint /usr/local/bin/gat-great.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gat-great.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gat-plot.py

```bash
$ singularity exec <container> /usr/local/bin/gat-plot.py
$ podman run --it --rm --entrypoint /usr/local/bin/gat-plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gat-plot.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gat-run.py

```bash
$ singularity exec <container> /usr/local/bin/gat-run.py
$ podman run --it --rm --entrypoint /usr/local/bin/gat-run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gat-run.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msgattrib

```bash
$ singularity exec <container> /usr/local/bin/msgattrib
$ podman run --it --rm --entrypoint /usr/local/bin/msgattrib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msgattrib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_config

```bash
$ singularity exec <container> /usr/local/bin/pg_config
$ podman run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
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