---
layout: container
name:  "quay.io/biocontainers/taxonomy_ranks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taxonomy_ranks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/taxonomy_ranks/container.yaml"
updated_at: "2023-06-11 03:31:08.377887"
latest: "0.0.10--py_0"
container_url: "https://biocontainers.pro/tools/taxonomy_ranks"
aliases:
 - "taxaranks"
 - "ete3"
 - "compile-et.pl"
 - "prerr.properties"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "certutil"
 - "nspr-config"
 - "nss-config"
 - "pk12util"
versions:
 - "0.0.8--py_0"
 - "0.0.10--py_0"
description: "shpc-registry automated BioContainers addition for taxonomy_ranks"
config: {"url": "https://biocontainers.pro/tools/taxonomy_ranks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for taxonomy_ranks", "latest": {"0.0.10--py_0": "sha256:1b7c283c8fbf1dc2bc533aace68c0374c8b8222f608203f089577ad262a43921"}, "tags": {"0.0.8--py_0": "sha256:3c201ed7dcd4967231596cf293e82cd2d7123ce59591dbe316db1d9618e9c23b", "0.0.10--py_0": "sha256:1b7c283c8fbf1dc2bc533aace68c0374c8b8222f608203f089577ad262a43921"}, "docker": "quay.io/biocontainers/taxonomy_ranks", "aliases": {"taxaranks": "/usr/local/bin/taxaranks", "ete3": "/usr/local/bin/ete3", "compile-et.pl": "/usr/local/bin/compile-et.pl", "prerr.properties": "/usr/local/bin/prerr.properties", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taxonomy_ranks.
shpc-registry automated BioContainers addition for taxonomy_ranks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taxonomy_ranks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taxonomy_ranks:0.0.10--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taxonomy_ranks/0.0.10--py_0
$ module help quay.io/biocontainers/taxonomy_ranks/0.0.10--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taxonomy_ranks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taxonomy_ranks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taxonomy_ranks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taxonomy_ranks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taxonomy_ranks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taxonomy_ranks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### taxaranks

```bash
$ singularity exec <container> /usr/local/bin/taxaranks
$ podman run --it --rm --entrypoint /usr/local/bin/taxaranks   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxaranks   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
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