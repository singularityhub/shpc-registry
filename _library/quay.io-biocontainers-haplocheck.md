---
layout: container
name:  "quay.io/biocontainers/haplocheck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/haplocheck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/haplocheck/container.yaml"
updated_at: "2026-01-05 05:51:33.995310"
latest: "1.3.3--h2a3209d_2"
container_url: "https://biocontainers.pro/tools/haplocheck"
aliases:
 - "cloudgene.yaml"
 - "haplocheck"
 - "haplocheck.jar"
 - "mutserve.jar"
 - "rCRS.fasta"
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "jjs"
versions:
 - "1.3.3--h4a94de4_0"
 - "1.3.3--h4a94de4_1"
 - "1.3.3--h2a3209d_2"
description: "shpc-registry automated BioContainers addition for haplocheck"
config: {"url": "https://biocontainers.pro/tools/haplocheck", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for haplocheck", "latest": {"1.3.3--h2a3209d_2": "sha256:1d4e006a69dab62cc0304509be83cc8c11f932cbf6a88fe4aacbb072e8eebacd"}, "tags": {"1.3.3--h4a94de4_0": "sha256:a2d2bace16d9c2cec327aa984d48a6b456b0ce228120975072f8e2ac4a798afc", "1.3.3--h4a94de4_1": "sha256:7b9bfe5941489313e2fcd9d33aca27821702c6667341674055236a44968d2400", "1.3.3--h2a3209d_2": "sha256:1d4e006a69dab62cc0304509be83cc8c11f932cbf6a88fe4aacbb072e8eebacd"}, "docker": "quay.io/biocontainers/haplocheck", "aliases": {"cloudgene.yaml": "/usr/local/bin/cloudgene.yaml", "haplocheck": "/usr/local/bin/haplocheck", "haplocheck.jar": "/usr/local/bin/haplocheck.jar", "mutserve.jar": "/usr/local/bin/mutserve.jar", "rCRS.fasta": "/usr/local/bin/rCRS.fasta", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "jjs": "/usr/local/bin/jjs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/haplocheck.
shpc-registry automated BioContainers addition for haplocheck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/haplocheck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/haplocheck:1.3.3--h2a3209d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/haplocheck/1.3.3--h2a3209d_2
$ module help quay.io/biocontainers/haplocheck/1.3.3--h2a3209d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### haplocheck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### haplocheck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### haplocheck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### haplocheck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### haplocheck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### haplocheck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cloudgene.yaml

```bash
$ singularity exec <container> /usr/local/bin/cloudgene.yaml
$ podman run --it --rm --entrypoint /usr/local/bin/cloudgene.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cloudgene.yaml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haplocheck

```bash
$ singularity exec <container> /usr/local/bin/haplocheck
$ podman run --it --rm --entrypoint /usr/local/bin/haplocheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplocheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haplocheck.jar

```bash
$ singularity exec <container> /usr/local/bin/haplocheck.jar
$ podman run --it --rm --entrypoint /usr/local/bin/haplocheck.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haplocheck.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutserve.jar

```bash
$ singularity exec <container> /usr/local/bin/mutserve.jar
$ podman run --it --rm --entrypoint /usr/local/bin/mutserve.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutserve.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rCRS.fasta

```bash
$ singularity exec <container> /usr/local/bin/rCRS.fasta
$ podman run --it --rm --entrypoint /usr/local/bin/rCRS.fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rCRS.fasta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /usr/local/bin/jjs
$ podman run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
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