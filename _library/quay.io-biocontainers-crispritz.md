---
layout: container
name:  "quay.io/biocontainers/crispritz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crispritz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crispritz/container.yaml"
updated_at: "2026-01-16 04:28:22.219991"
latest: "2.7.0--py38h9948957_2"
container_url: "https://biocontainers.pro/tools/crispritz"
aliases:
 - "crispritz.py"
 - "bam2bed"
 - "bam2bed-float128"
 - "bam2bed-megarow"
 - "bam2bed-typical"
 - "bam2bed_gnuParallel"
 - "bam2bed_gnuParallel-float128"
 - "bam2bed_gnuParallel-megarow"
 - "bam2bed_gnuParallel-typical"
 - "bam2bed_sge"
 - "bam2bed_sge-float128"
versions:
 - "2.3.7--py36hbd375b7_1"
 - "2.6.6--py39h68928f9_1"
 - "2.5.9--py36h0bca50a_0"
 - "2.4.9--py37h36a7b89_0"
 - "2.3.8--py36hbd375b7_0"
 - "2.6.6--py38h2123bcc_2"
 - "2.6.6--py39h2de1943_3"
 - "2.6.6--py39h2de1943_4"
 - "2.7.0--py39h2de1943_0"
 - "2.7.0--py38h9948957_2"
description: "shpc-registry automated BioContainers addition for crispritz"
config: {"url": "https://biocontainers.pro/tools/crispritz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for crispritz", "latest": {"2.7.0--py38h9948957_2": "sha256:626926416ff29fed189582d3a83a5c18ad85d306bb4e73735567c379d9f718ab"}, "tags": {"2.3.7--py36hbd375b7_1": "sha256:e364f3755211e99d5edb9fcf11d825aea867a2e42fb52a54933eab13e453d248", "2.6.6--py39h68928f9_1": "sha256:aba83fa7eac1e996bb427b677f61b5294f0b9bcc190eebdff381e856111e5261", "2.5.9--py36h0bca50a_0": "sha256:0a4287b76df13b7dd5174ba18eb215f446d59407b47e9a1278e80372b81eef73", "2.4.9--py37h36a7b89_0": "sha256:d3837be8632d7cb8230a722c7750c7e9c82e0e02ccad5e7e01a6550626ef18df", "2.3.8--py36hbd375b7_0": "sha256:1d1c7ebbc97433cabf6b8716c18b61910955b1e8e8f578462deb63428c6ba5c3", "2.6.6--py38h2123bcc_2": "sha256:2922606faaf65a8666b9d0ecddd2822e53d00af3833c3c95a867f5ab6aabfe3d", "2.6.6--py39h2de1943_3": "sha256:46679b08eea3f2fcf4d6ddf4ad80b3ad6d36449869bf1462c85c4b3adb1fbcec", "2.6.6--py39h2de1943_4": "sha256:936752acef7ce17233163ed0b68bee8b53bb22a1981e4dcc68bdb2fa39068043", "2.7.0--py39h2de1943_0": "sha256:92457c12fdf3a6e0a4b2a53251829396b96a7c4058648e260f993dfcf64a4d66", "2.7.0--py38h9948957_2": "sha256:626926416ff29fed189582d3a83a5c18ad85d306bb4e73735567c379d9f718ab"}, "docker": "quay.io/biocontainers/crispritz", "aliases": {"crispritz.py": "/usr/local/bin/crispritz.py", "bam2bed": "/usr/local/bin/bam2bed", "bam2bed-float128": "/usr/local/bin/bam2bed-float128", "bam2bed-megarow": "/usr/local/bin/bam2bed-megarow", "bam2bed-typical": "/usr/local/bin/bam2bed-typical", "bam2bed_gnuParallel": "/usr/local/bin/bam2bed_gnuParallel", "bam2bed_gnuParallel-float128": "/usr/local/bin/bam2bed_gnuParallel-float128", "bam2bed_gnuParallel-megarow": "/usr/local/bin/bam2bed_gnuParallel-megarow", "bam2bed_gnuParallel-typical": "/usr/local/bin/bam2bed_gnuParallel-typical", "bam2bed_sge": "/usr/local/bin/bam2bed_sge", "bam2bed_sge-float128": "/usr/local/bin/bam2bed_sge-float128"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crispritz.
shpc-registry automated BioContainers addition for crispritz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crispritz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crispritz:2.7.0--py38h9948957_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crispritz/2.7.0--py38h9948957_2
$ module help quay.io/biocontainers/crispritz/2.7.0--py38h9948957_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crispritz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crispritz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crispritz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crispritz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crispritz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crispritz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### crispritz.py

```bash
$ singularity exec <container> /usr/local/bin/crispritz.py
$ podman run --it --rm --entrypoint /usr/local/bin/crispritz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crispritz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed

```bash
$ singularity exec <container> /usr/local/bin/bam2bed
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
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