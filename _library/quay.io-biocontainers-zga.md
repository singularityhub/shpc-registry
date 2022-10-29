---
layout: container
name:  "quay.io/biocontainers/zga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/zga/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/zga/container.yaml"
updated_at: "2022-10-29 05:51:05.073729"
latest: "0.0.9.post2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/zga"
aliases:
 - "dfast"
 - "dfast_file_downloader.py"
 - "file_downloader.py"
 - "flye-modules"
 - "flye-samtools"
 - "ghostx"
 - "mga"
 - "nxtrim"
 - "unicycler"
 - "unicycler_align"
 - "unicycler_check"
 - "unicycler_polish"
 - "unicycler_scrub"
 - "zga"
 - "a_sample_mt.sh"
 - "abba-baba"
 - "accn-at-a-time"
 - "ace2sam"
 - "addadapters.sh"
 - "addssu.sh"
 - "adjusthomopolymers.sh"
 - "align-columns"
 - "alimask"
 - "alltoall.sh"
versions:
 - "0.0.9.post2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for zga"
config: {"url": "https://biocontainers.pro/tools/zga", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for zga", "latest": {"0.0.9.post2--pyhdfd78af_1": "sha256:9934c00a59ba9ceb8ede393026a1255450d9a7a2a8ee7fe5891dd613654b00df"}, "tags": {"0.0.9.post2--pyhdfd78af_1": "sha256:9934c00a59ba9ceb8ede393026a1255450d9a7a2a8ee7fe5891dd613654b00df"}, "docker": "quay.io/biocontainers/zga", "aliases": {"dfast": "/usr/local/bin/dfast", "dfast_file_downloader.py": "/usr/local/bin/dfast_file_downloader.py", "file_downloader.py": "/usr/local/bin/file_downloader.py", "flye-modules": "/usr/local/bin/flye-modules", "flye-samtools": "/usr/local/bin/flye-samtools", "ghostx": "/usr/local/bin/ghostx", "mga": "/usr/local/bin/mga", "nxtrim": "/usr/local/bin/nxtrim", "unicycler": "/usr/local/bin/unicycler", "unicycler_align": "/usr/local/bin/unicycler_align", "unicycler_check": "/usr/local/bin/unicycler_check", "unicycler_polish": "/usr/local/bin/unicycler_polish", "unicycler_scrub": "/usr/local/bin/unicycler_scrub", "zga": "/usr/local/bin/zga", "a_sample_mt.sh": "/usr/local/bin/a_sample_mt.sh", "abba-baba": "/usr/local/bin/abba-baba", "accn-at-a-time": "/usr/local/bin/accn-at-a-time", "ace2sam": "/usr/local/bin/ace2sam", "addadapters.sh": "/usr/local/bin/addadapters.sh", "addssu.sh": "/usr/local/bin/addssu.sh", "adjusthomopolymers.sh": "/usr/local/bin/adjusthomopolymers.sh", "align-columns": "/usr/local/bin/align-columns", "alimask": "/usr/local/bin/alimask", "alltoall.sh": "/usr/local/bin/alltoall.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/zga.
shpc-registry automated BioContainers addition for zga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/zga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/zga:0.0.9.post2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/zga/0.0.9.post2--pyhdfd78af_1
$ module help quay.io/biocontainers/zga/0.0.9.post2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### zga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### zga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### zga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### zga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### zga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### zga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dfast

```bash
$ singularity exec <container> /usr/local/bin/dfast
$ podman run --it --rm --entrypoint /usr/local/bin/dfast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dfast_file_downloader.py

```bash
$ singularity exec <container> /usr/local/bin/dfast_file_downloader.py
$ podman run --it --rm --entrypoint /usr/local/bin/dfast_file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dfast_file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### file_downloader.py

```bash
$ singularity exec <container> /usr/local/bin/file_downloader.py
$ podman run --it --rm --entrypoint /usr/local/bin/file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/file_downloader.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-modules

```bash
$ singularity exec <container> /usr/local/bin/flye-modules
$ podman run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-modules   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flye-samtools

```bash
$ singularity exec <container> /usr/local/bin/flye-samtools
$ podman run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flye-samtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghostx

```bash
$ singularity exec <container> /usr/local/bin/ghostx
$ podman run --it --rm --entrypoint /usr/local/bin/ghostx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghostx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mga

```bash
$ singularity exec <container> /usr/local/bin/mga
$ podman run --it --rm --entrypoint /usr/local/bin/mga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mga   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nxtrim

```bash
$ singularity exec <container> /usr/local/bin/nxtrim
$ podman run --it --rm --entrypoint /usr/local/bin/nxtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nxtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler

```bash
$ singularity exec <container> /usr/local/bin/unicycler
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler_align

```bash
$ singularity exec <container> /usr/local/bin/unicycler_align
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler_align   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler_align   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler_check

```bash
$ singularity exec <container> /usr/local/bin/unicycler_check
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler_check   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler_check   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler_polish

```bash
$ singularity exec <container> /usr/local/bin/unicycler_polish
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler_polish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler_polish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unicycler_scrub

```bash
$ singularity exec <container> /usr/local/bin/unicycler_scrub
$ podman run --it --rm --entrypoint /usr/local/bin/unicycler_scrub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unicycler_scrub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zga

```bash
$ singularity exec <container> /usr/local/bin/zga
$ podman run --it --rm --entrypoint /usr/local/bin/zga   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zga   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### a_sample_mt.sh

```bash
$ singularity exec <container> /usr/local/bin/a_sample_mt.sh
$ podman run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/a_sample_mt.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abba-baba

```bash
$ singularity exec <container> /usr/local/bin/abba-baba
$ podman run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abba-baba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### accn-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/accn-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/accn-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addadapters.sh

```bash
$ singularity exec <container> /usr/local/bin/addadapters.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addadapters.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### addssu.sh

```bash
$ singularity exec <container> /usr/local/bin/addssu.sh
$ podman run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/addssu.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### adjusthomopolymers.sh

```bash
$ singularity exec <container> /usr/local/bin/adjusthomopolymers.sh
$ podman run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adjusthomopolymers.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### align-columns

```bash
$ singularity exec <container> /usr/local/bin/align-columns
$ podman run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/align-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alltoall.sh

```bash
$ singularity exec <container> /usr/local/bin/alltoall.sh
$ podman run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alltoall.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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