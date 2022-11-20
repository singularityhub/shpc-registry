---
layout: container
name:  "quay.io/biocontainers/epimuller"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/epimuller/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/epimuller/container.yaml"
updated_at: "2022-11-20 00:45:30.238325"
latest: "0.0.8--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/epimuller"
aliases:
 - "cairosvg"
 - "epimuller"
 - "epimuller-define"
 - "epimuller-draw"
 - "epimuller-parse"
 - "ete3"
 - "xkbcli"
 - "pg_config"
 - "qdistancefieldgenerator"
 - "qmlpreview"
 - "qvkgen"
 - "certutil"
 - "nspr-config"
 - "nss-config"
 - "pk12util"
versions:
 - "0.0.8--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for epimuller"
config: {"url": "https://biocontainers.pro/tools/epimuller", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for epimuller", "latest": {"0.0.8--pyhdfd78af_0": "sha256:d21ecefebd541f175a196af249b0fd46883f1c10620243ea499d984557ca090a"}, "tags": {"0.0.8--pyhdfd78af_0": "sha256:d21ecefebd541f175a196af249b0fd46883f1c10620243ea499d984557ca090a"}, "docker": "quay.io/biocontainers/epimuller", "aliases": {"cairosvg": "/usr/local/bin/cairosvg", "epimuller": "/usr/local/bin/epimuller", "epimuller-define": "/usr/local/bin/epimuller-define", "epimuller-draw": "/usr/local/bin/epimuller-draw", "epimuller-parse": "/usr/local/bin/epimuller-parse", "ete3": "/usr/local/bin/ete3", "xkbcli": "/usr/local/bin/xkbcli", "pg_config": "/usr/local/bin/pg_config", "qdistancefieldgenerator": "/usr/local/bin/qdistancefieldgenerator", "qmlpreview": "/usr/local/bin/qmlpreview", "qvkgen": "/usr/local/bin/qvkgen", "certutil": "/usr/local/bin/certutil", "nspr-config": "/usr/local/bin/nspr-config", "nss-config": "/usr/local/bin/nss-config", "pk12util": "/usr/local/bin/pk12util"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/epimuller.
shpc-registry automated BioContainers addition for epimuller
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/epimuller
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/epimuller:0.0.8--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/epimuller/0.0.8--pyhdfd78af_0
$ module help quay.io/biocontainers/epimuller/0.0.8--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### epimuller-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### epimuller-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### epimuller-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### epimuller-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### epimuller-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### epimuller-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cairosvg

```bash
$ singularity exec <container> /usr/local/bin/cairosvg
$ podman run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cairosvg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### epimuller

```bash
$ singularity exec <container> /usr/local/bin/epimuller
$ podman run --it --rm --entrypoint /usr/local/bin/epimuller   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epimuller   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### epimuller-define

```bash
$ singularity exec <container> /usr/local/bin/epimuller-define
$ podman run --it --rm --entrypoint /usr/local/bin/epimuller-define   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epimuller-define   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### epimuller-draw

```bash
$ singularity exec <container> /usr/local/bin/epimuller-draw
$ podman run --it --rm --entrypoint /usr/local/bin/epimuller-draw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epimuller-draw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### epimuller-parse

```bash
$ singularity exec <container> /usr/local/bin/epimuller-parse
$ podman run --it --rm --entrypoint /usr/local/bin/epimuller-parse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epimuller-parse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
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