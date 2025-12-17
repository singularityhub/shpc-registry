---
layout: container
name:  "quay.io/biocontainers/export2graphlan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/export2graphlan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/export2graphlan/container.yaml"
updated_at: "2025-12-17 15:53:34.623138"
latest: "0.22--py_0"
container_url: "https://biocontainers.pro/tools/export2graphlan"
aliases:
 - "export2graphlan.py"
 - "hclust2.py"
 - "compile-et.pl"
 - "prerr.properties"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "certutil"
 - "nspr-config"
 - "nss-config"
 - "pk12util"
 - "f2py2"
versions:
 - "0.22--py_0"
description: "shpc-registry automated BioContainers addition for export2graphlan"
config: {"url": "https://biocontainers.pro/tools/export2graphlan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for export2graphlan", "latest": {"0.22--py_0": "sha256:ff6e1a0ae7e114485b0c66aaa0f612b4b9c6677ce0465d37bc0ea7b8ed3cbc31"}, "tags": {"0.22--py_0": "sha256:ff6e1a0ae7e114485b0c66aaa0f612b4b9c6677ce0465d37bc0ea7b8ed3cbc31"}, "docker": "quay.io/biocontainers/export2graphlan", "aliases": {"export2graphlan.py": "/usr/local/bin/export2graphlan.py", "hclust2.py": "/usr/local/bin/hclust2.py", "compile-et.pl": "/usr/local/bin/compile-et.pl", "prerr.properties": "/usr/local/bin/prerr.properties", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util", "f2py2": "/usr/local/bin/f2py2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/export2graphlan.
shpc-registry automated BioContainers addition for export2graphlan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/export2graphlan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/export2graphlan:0.22--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/export2graphlan/0.22--py_0
$ module help quay.io/biocontainers/export2graphlan/0.22--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### export2graphlan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### export2graphlan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### export2graphlan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### export2graphlan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### export2graphlan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### export2graphlan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### export2graphlan.py

```bash
$ singularity exec <container> /usr/local/bin/export2graphlan.py
$ podman run --it --rm --entrypoint /usr/local/bin/export2graphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/export2graphlan.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hclust2.py

```bash
$ singularity exec <container> /usr/local/bin/hclust2.py
$ podman run --it --rm --entrypoint /usr/local/bin/hclust2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hclust2.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
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