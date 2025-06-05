---
layout: container
name:  "quay.io/biocontainers/recentrifuge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/recentrifuge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/recentrifuge/container.yaml"
updated_at: "2025-06-05 03:34:41.757786"
latest: "1.16.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/recentrifuge"
aliases:
 - "rcf"
 - "refasplit"
 - "remock"
 - "retaxdump"
 - "retest"
 - "rextract"
 - "fonttools"
 - "pyftmerge"
 - "pyftsubset"
 - "ttx"
 - "brotli"
 - "f2py3.10"
 - "img2webp"
 - "cwebp"
 - "dwebp"
 - "gif2webp"
versions:
 - "1.9.1--pyhdfd78af_0"
 - "1.10.0--pyhdfd78af_0"
 - "1.12.1--pyhdfd78af_0"
 - "1.12.2--pyhdfd78af_0"
 - "1.13.1--pyhdfd78af_0"
 - "1.14.0--pyhdfd78af_0"
 - "1.13.2--pyhdfd78af_0"
 - "1.15.0--pyhdfd78af_0"
 - "1.14.1--pyhdfd78af_0"
 - "1.15.1--pyhdfd78af_0"
 - "1.16.0--pyhdfd78af_0"
 - "1.16.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for recentrifuge"
config: {"url": "https://biocontainers.pro/tools/recentrifuge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for recentrifuge", "latest": {"1.16.1--pyhdfd78af_0": "sha256:49d3ee12a13bd4f054831ee6c18ab414655472140685d411650a08f64752dffa"}, "tags": {"1.9.1--pyhdfd78af_0": "sha256:32f8a055bd0ae507e7ce8c84fba2100b7a6554e36e8d7ca320367bbabd527897", "1.10.0--pyhdfd78af_0": "sha256:684bcf23dd5657424c7fea2a7505819c9ed42af7062521c73cad5ed406e2daaf", "1.12.1--pyhdfd78af_0": "sha256:f2b0e996b66c2f52c9b2aec34520be73d1628a7430da560318689c98a651109c", "1.12.2--pyhdfd78af_0": "sha256:49288c1152a1a50de019ac30e9e8155e459d172f07dfd710bd8ae6edae38470a", "1.13.1--pyhdfd78af_0": "sha256:0d1cc7a4feb1902194d77039574c241cf9d763d9d69e2a1381d7bb3e3e2b53b1", "1.14.0--pyhdfd78af_0": "sha256:6d915d255c1ebdc97c27b315df6955895977d1a9d7e02f2ebaab96fab8353119", "1.13.2--pyhdfd78af_0": "sha256:a537774b56e8411f769944db12f7413f83263e64ff02cb3b1da123add191bd79", "1.15.0--pyhdfd78af_0": "sha256:1cb4722355ff79b5c67ecb22f3f50c6bacaefe9aff820da43fc95196c196373f", "1.14.1--pyhdfd78af_0": "sha256:46564e3012188c48a8edc8376d05a517564c365ecd85f55d1b1a581006a71166", "1.15.1--pyhdfd78af_0": "sha256:c2bffd865d199fa3501a33387baff77786d77e59c0def899355f3b92271e468f", "1.16.0--pyhdfd78af_0": "sha256:56ad1b506ec3f3f44e1f5f549f0444b7a7b79b4d99982fa7bccc9f242f005bf5", "1.16.1--pyhdfd78af_0": "sha256:49d3ee12a13bd4f054831ee6c18ab414655472140685d411650a08f64752dffa"}, "docker": "quay.io/biocontainers/recentrifuge", "aliases": {"rcf": "/usr/local/bin/rcf", "refasplit": "/usr/local/bin/refasplit", "remock": "/usr/local/bin/remock", "retaxdump": "/usr/local/bin/retaxdump", "retest": "/usr/local/bin/retest", "rextract": "/usr/local/bin/rextract", "fonttools": "/usr/local/bin/fonttools", "pyftmerge": "/usr/local/bin/pyftmerge", "pyftsubset": "/usr/local/bin/pyftsubset", "ttx": "/usr/local/bin/ttx", "brotli": "/usr/local/bin/brotli", "f2py3.10": "/usr/local/bin/f2py3.10", "img2webp": "/usr/local/bin/img2webp", "cwebp": "/usr/local/bin/cwebp", "dwebp": "/usr/local/bin/dwebp", "gif2webp": "/usr/local/bin/gif2webp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/recentrifuge.
shpc-registry automated BioContainers addition for recentrifuge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/recentrifuge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/recentrifuge:1.16.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/recentrifuge/1.16.1--pyhdfd78af_0
$ module help quay.io/biocontainers/recentrifuge/1.16.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### recentrifuge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### recentrifuge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### recentrifuge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### recentrifuge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### recentrifuge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### recentrifuge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rcf

```bash
$ singularity exec <container> /usr/local/bin/rcf
$ podman run --it --rm --entrypoint /usr/local/bin/rcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refasplit

```bash
$ singularity exec <container> /usr/local/bin/refasplit
$ podman run --it --rm --entrypoint /usr/local/bin/refasplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refasplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remock

```bash
$ singularity exec <container> /usr/local/bin/remock
$ podman run --it --rm --entrypoint /usr/local/bin/remock   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remock   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retaxdump

```bash
$ singularity exec <container> /usr/local/bin/retaxdump
$ podman run --it --rm --entrypoint /usr/local/bin/retaxdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retaxdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retest

```bash
$ singularity exec <container> /usr/local/bin/retest
$ podman run --it --rm --entrypoint /usr/local/bin/retest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rextract

```bash
$ singularity exec <container> /usr/local/bin/rextract
$ podman run --it --rm --entrypoint /usr/local/bin/rextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rextract   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2webp

```bash
$ singularity exec <container> /usr/local/bin/img2webp
$ podman run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cwebp

```bash
$ singularity exec <container> /usr/local/bin/cwebp
$ podman run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwebp

```bash
$ singularity exec <container> /usr/local/bin/dwebp
$ podman run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwebp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2webp

```bash
$ singularity exec <container> /usr/local/bin/gif2webp
$ podman run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2webp   -v ${PWD} -w ${PWD} <container> -c " $@"
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