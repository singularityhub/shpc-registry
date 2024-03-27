---
layout: container
name:  "quay.io/biocontainers/bwa-meme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bwa-meme/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bwa-meme/container.yaml"
updated_at: "2024-03-27 02:52:17.063035"
latest: "1.0.6--hdcf5f25_2"
container_url: "https://biocontainers.pro/tools/bwa-meme"
aliases:
 - "build_rmis_dna.sh"
 - "bwa-meme"
 - "bwa-meme-train-prmi"
 - "bwa-meme_mode1"
 - "bwa-meme_mode1.avx"
 - "bwa-meme_mode1.avx2"
 - "bwa-meme_mode1.avx512bw"
 - "bwa-meme_mode1.sse41"
 - "bwa-meme_mode1.sse42"
 - "bwa-meme_mode2"
 - "bwa-meme_mode2.avx"
 - "bwa-meme_mode2.avx2"
 - "bwa-meme_mode2.avx512bw"
 - "bwa-meme_mode2.sse41"
 - "bwa-meme_mode2.sse42"
 - "bwa-meme_mode3.avx"
 - "bwa-meme_mode3.avx2"
 - "bwa-meme_mode3.avx512bw"
 - "bwa-meme_mode3.sse41"
 - "bwa-meme_mode3.sse42"
versions:
 - "1.0.5--hd03093a_0"
 - "1.0.6--hd03093a_0"
 - "1.0.6--hdcf5f25_2"
description: "singularity registry hpc automated addition for bwa-meme"
config: {"url": "https://biocontainers.pro/tools/bwa-meme", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bwa-meme", "latest": {"1.0.6--hdcf5f25_2": "sha256:aeb069f1d71dfb32f47746fd6b020a8cb7fccfdfe63fdb334a6e228f651bdffc"}, "tags": {"1.0.5--hd03093a_0": "sha256:8cb6127d4e75c6397363015937748f3f528100a52cfe448fe7fac4ebfbccc11e", "1.0.6--hd03093a_0": "sha256:fcc7964c726542cbda041ce5cccbcf9a5b4b0790e230a1dbda7439e428966313", "1.0.6--hdcf5f25_2": "sha256:aeb069f1d71dfb32f47746fd6b020a8cb7fccfdfe63fdb334a6e228f651bdffc"}, "docker": "quay.io/biocontainers/bwa-meme", "aliases": {"build_rmis_dna.sh": "/usr/local/bin/build_rmis_dna.sh", "bwa-meme": "/usr/local/bin/bwa-meme", "bwa-meme-train-prmi": "/usr/local/bin/bwa-meme-train-prmi", "bwa-meme_mode1": "/usr/local/bin/bwa-meme_mode1", "bwa-meme_mode1.avx": "/usr/local/bin/bwa-meme_mode1.avx", "bwa-meme_mode1.avx2": "/usr/local/bin/bwa-meme_mode1.avx2", "bwa-meme_mode1.avx512bw": "/usr/local/bin/bwa-meme_mode1.avx512bw", "bwa-meme_mode1.sse41": "/usr/local/bin/bwa-meme_mode1.sse41", "bwa-meme_mode1.sse42": "/usr/local/bin/bwa-meme_mode1.sse42", "bwa-meme_mode2": "/usr/local/bin/bwa-meme_mode2", "bwa-meme_mode2.avx": "/usr/local/bin/bwa-meme_mode2.avx", "bwa-meme_mode2.avx2": "/usr/local/bin/bwa-meme_mode2.avx2", "bwa-meme_mode2.avx512bw": "/usr/local/bin/bwa-meme_mode2.avx512bw", "bwa-meme_mode2.sse41": "/usr/local/bin/bwa-meme_mode2.sse41", "bwa-meme_mode2.sse42": "/usr/local/bin/bwa-meme_mode2.sse42", "bwa-meme_mode3.avx": "/usr/local/bin/bwa-meme_mode3.avx", "bwa-meme_mode3.avx2": "/usr/local/bin/bwa-meme_mode3.avx2", "bwa-meme_mode3.avx512bw": "/usr/local/bin/bwa-meme_mode3.avx512bw", "bwa-meme_mode3.sse41": "/usr/local/bin/bwa-meme_mode3.sse41", "bwa-meme_mode3.sse42": "/usr/local/bin/bwa-meme_mode3.sse42"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bwa-meme.
singularity registry hpc automated addition for bwa-meme
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bwa-meme
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bwa-meme:1.0.6--hdcf5f25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bwa-meme/1.0.6--hdcf5f25_2
$ module help quay.io/biocontainers/bwa-meme/1.0.6--hdcf5f25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bwa-meme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bwa-meme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bwa-meme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bwa-meme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bwa-meme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bwa-meme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### build_rmis_dna.sh

```bash
$ singularity exec <container> /usr/local/bin/build_rmis_dna.sh
$ podman run --it --rm --entrypoint /usr/local/bin/build_rmis_dna.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/build_rmis_dna.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme-train-prmi

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme-train-prmi
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme-train-prmi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme-train-prmi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode1

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode1
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode1.avx

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode1.avx
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode1.avx2

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode1.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode1.avx512bw

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode1.avx512bw
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode1.sse41

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode1.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode1.sse42

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode1.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode1.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode2

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode2.avx

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode2.avx
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode2.avx2

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode2.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode2.avx512bw

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode2.avx512bw
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode2.sse41

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode2.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode2.sse42

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode2.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode3.avx

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode3.avx
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode3.avx2

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode3.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode3.avx512bw

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode3.avx512bw
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode3.sse41

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode3.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-meme_mode3.sse42

```bash
$ singularity exec <container> /usr/local/bin/bwa-meme_mode3.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-meme_mode3.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
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