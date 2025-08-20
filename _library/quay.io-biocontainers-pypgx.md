---
layout: container
name:  "quay.io/biocontainers/pypgx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pypgx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pypgx/container.yaml"
updated_at: "2025-08-20 03:22:42.862695"
latest: "0.25.0--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/pypgx"
aliases:
 - "fuc"
 - "pypgx"
 - "tabulate"
 - "natsort"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "xslt-config"
 - "xsltproc"
 - "jaotc"
versions:
 - "0.9.0--pyh5e36f6f_0"
 - "0.19.0--pyh7cba7a3_0"
 - "0.18.0--pyh5e36f6f_0"
 - "0.17.0--pyh5e36f6f_0"
 - "0.16.0--pyh5e36f6f_0"
 - "0.15.0--pyh5e36f6f_0"
 - "0.20.0--pyh7cba7a3_0"
 - "0.21.0--pyh7cba7a3_0"
 - "0.22.0--pyh7cba7a3_0"
 - "0.23.0--pyh7cba7a3_0"
 - "0.24.0--pyh7cba7a3_0"
 - "0.25.0--pyh7e72e81_0"
description: "shpc-registry automated BioContainers addition for pypgx"
config: {"url": "https://biocontainers.pro/tools/pypgx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pypgx", "latest": {"0.25.0--pyh7e72e81_0": "sha256:60f8f0d1adce902b3552b19c74597971375f349c298aa574ac7a420841cbc6ec"}, "tags": {"0.9.0--pyh5e36f6f_0": "sha256:86f03a8935c7c972a8e1823eff4439c472b5cc86daff176929abf6a6f01957e2", "0.19.0--pyh7cba7a3_0": "sha256:ec1484fc3e6d3ca332fd18c4750bd53537f4a2c50d484fe8da83822e07f8c4cb", "0.18.0--pyh5e36f6f_0": "sha256:2f5cf0fde84bd9539c2e790c535f971163fbd5a1cd14a3056d856d67c47916d3", "0.17.0--pyh5e36f6f_0": "sha256:64cab45134fa1c6739021a5ea59011c2faf753339fc7a3c146ee3c21589b4fca", "0.16.0--pyh5e36f6f_0": "sha256:073a2b683cb8c31cd3234861aedb8424c42677bb3c32b21719bcdb613e889228", "0.15.0--pyh5e36f6f_0": "sha256:28b73104906a4990a9129d8222d406feafaac81542c739f341dee719e229a372", "0.20.0--pyh7cba7a3_0": "sha256:8ff58238ba3715c738de130e8274553beef212cc1d0269fe617fb943a09d6689", "0.21.0--pyh7cba7a3_0": "sha256:0965024b75f2255ee328aae4999c49c405c7c759e39e3537de41d82095111e10", "0.22.0--pyh7cba7a3_0": "sha256:a282559940934709cb23b9f8cfff81fbf7a99581fb5e88915af065613d6e9945", "0.23.0--pyh7cba7a3_0": "sha256:2469b2bf6e62e906b75a0cc87c00ff48f259735b7d10cb1fedcdc0406b59d525", "0.24.0--pyh7cba7a3_0": "sha256:954a3729466b920dfbf0a665e85890c6219fa60b4d5c0b9c206b8a6afab8d7b4", "0.25.0--pyh7e72e81_0": "sha256:60f8f0d1adce902b3552b19c74597971375f349c298aa574ac7a420841cbc6ec"}, "docker": "quay.io/biocontainers/pypgx", "aliases": {"fuc": "/usr/local/bin/fuc", "pypgx": "/usr/local/bin/pypgx", "tabulate": "/usr/local/bin/tabulate", "natsort": "/usr/local/bin/natsort", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "jaotc": "/usr/local/bin/jaotc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pypgx.
shpc-registry automated BioContainers addition for pypgx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pypgx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pypgx:0.25.0--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pypgx/0.25.0--pyh7e72e81_0
$ module help quay.io/biocontainers/pypgx/0.25.0--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pypgx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pypgx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pypgx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pypgx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pypgx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pypgx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fuc

```bash
$ singularity exec <container> /usr/local/bin/fuc
$ podman run --it --rm --entrypoint /usr/local/bin/fuc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypgx

```bash
$ singularity exec <container> /usr/local/bin/pypgx
$ podman run --it --rm --entrypoint /usr/local/bin/pypgx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypgx   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftmerge

```bash
$ singularity exec <container> /usr/local/bin/pyftmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyftsubset

```bash
$ singularity exec <container> /usr/local/bin/pyftsubset
$ podman run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyftsubset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttx

```bash
$ singularity exec <container> /usr/local/bin/ttx
$ podman run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
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