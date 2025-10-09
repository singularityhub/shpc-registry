---
layout: container
name:  "quay.io/biocontainers/fermikit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fermikit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fermikit/container.yaml"
updated_at: "2025-10-09 04:34:04.517508"
latest: "0.14.dev1--pl5321h86e5fe9_2"
container_url: "https://biocontainers.pro/tools/fermikit"
aliases:
 - "bfc"
 - "fermi2"
 - "fermi2.pl"
 - "hapdip.js"
 - "htsbox"
 - "ropebwt2"
 - "run-calling"
 - "trimadap-mt"
 - "seqtk"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "k8"
versions:
 - "0.14.dev1--pl5321h86e5fe9_2"
description: "singularity registry hpc automated addition for fermikit"
config: {"url": "https://biocontainers.pro/tools/fermikit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fermikit", "latest": {"0.14.dev1--pl5321h86e5fe9_2": "sha256:14b203f68c425e5a8a727205f9176ab5a2213b3aa55a3d930a32dc56bd86b38d"}, "tags": {"0.14.dev1--pl5321h86e5fe9_2": "sha256:14b203f68c425e5a8a727205f9176ab5a2213b3aa55a3d930a32dc56bd86b38d"}, "docker": "quay.io/biocontainers/fermikit", "aliases": {"bfc": "/usr/local/bin/bfc", "fermi2": "/usr/local/bin/fermi2", "fermi2.pl": "/usr/local/bin/fermi2.pl", "hapdip.js": "/usr/local/bin/hapdip.js", "htsbox": "/usr/local/bin/htsbox", "ropebwt2": "/usr/local/bin/ropebwt2", "run-calling": "/usr/local/bin/run-calling", "trimadap-mt": "/usr/local/bin/trimadap-mt", "seqtk": "/usr/local/bin/seqtk", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "k8": "/usr/local/bin/k8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fermikit.
singularity registry hpc automated addition for fermikit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fermikit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fermikit:0.14.dev1--pl5321h86e5fe9_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fermikit/0.14.dev1--pl5321h86e5fe9_2
$ module help quay.io/biocontainers/fermikit/0.14.dev1--pl5321h86e5fe9_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fermikit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fermikit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fermikit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fermikit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fermikit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fermikit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bfc

```bash
$ singularity exec <container> /usr/local/bin/bfc
$ podman run --it --rm --entrypoint /usr/local/bin/bfc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bfc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fermi2

```bash
$ singularity exec <container> /usr/local/bin/fermi2
$ podman run --it --rm --entrypoint /usr/local/bin/fermi2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fermi2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fermi2.pl

```bash
$ singularity exec <container> /usr/local/bin/fermi2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fermi2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fermi2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapdip.js

```bash
$ singularity exec <container> /usr/local/bin/hapdip.js
$ podman run --it --rm --entrypoint /usr/local/bin/hapdip.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapdip.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsbox

```bash
$ singularity exec <container> /usr/local/bin/htsbox
$ podman run --it --rm --entrypoint /usr/local/bin/htsbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ropebwt2

```bash
$ singularity exec <container> /usr/local/bin/ropebwt2
$ podman run --it --rm --entrypoint /usr/local/bin/ropebwt2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ropebwt2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-calling

```bash
$ singularity exec <container> /usr/local/bin/run-calling
$ podman run --it --rm --entrypoint /usr/local/bin/run-calling   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-calling   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trimadap-mt

```bash
$ singularity exec <container> /usr/local/bin/trimadap-mt
$ podman run --it --rm --entrypoint /usr/local/bin/trimadap-mt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trimadap-mt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqtk

```bash
$ singularity exec <container> /usr/local/bin/seqtk
$ podman run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqtk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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