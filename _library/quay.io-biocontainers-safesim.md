---
layout: container
name:  "quay.io/biocontainers/safesim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/safesim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/safesim/container.yaml"
updated_at: "2025-10-22 04:01:40.256736"
latest: "0.1.6.8d44580--h7d57edc_4"
container_url: "https://biocontainers.pro/tools/safesim"
aliases:
 - "fastq-grep"
 - "fastq-kmers"
 - "fastq-match"
 - "fastq-qscale"
 - "fastq-qual"
 - "fastq-qualadj"
 - "fastq-sample"
 - "fastq-sort"
 - "fastq-uniq"
 - "safemix"
 - "safemut"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.1.6.8d44580--h50ba451_0"
 - "0.1.6.8d44580--hac61d04_1"
 - "0.1.6.8d44580--h784672f_2"
 - "0.1.6.8d44580--hcec8cb8_3"
 - "0.1.6.8d44580--h7d57edc_4"
description: "singularity registry hpc automated addition for safesim"
config: {"url": "https://biocontainers.pro/tools/safesim", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for safesim", "latest": {"0.1.6.8d44580--h7d57edc_4": "sha256:48c7c5895caade918e9e6d04fdcdbfa06ffb32122a3170e08170351476da39bc"}, "tags": {"0.1.6.8d44580--h50ba451_0": "sha256:c45ddbde013cd30dc29a3960712dd0c5fe3eaecb2d0a0a876aa6fc2412b1eeb8", "0.1.6.8d44580--hac61d04_1": "sha256:453957e32d3632d6dd2f48c2ffa1adafb277fac25b275cff6546ef7627a35269", "0.1.6.8d44580--h784672f_2": "sha256:332f2023de9e0460ddb9dc361284cf3b3cdee234b70ae415604d0b5577476943", "0.1.6.8d44580--hcec8cb8_3": "sha256:18b14f3f85be9c7c620b900d0d62968585a934410048263d229c6af70e586ddf", "0.1.6.8d44580--h7d57edc_4": "sha256:48c7c5895caade918e9e6d04fdcdbfa06ffb32122a3170e08170351476da39bc"}, "docker": "quay.io/biocontainers/safesim", "aliases": {"fastq-grep": "/usr/local/bin/fastq-grep", "fastq-kmers": "/usr/local/bin/fastq-kmers", "fastq-match": "/usr/local/bin/fastq-match", "fastq-qscale": "/usr/local/bin/fastq-qscale", "fastq-qual": "/usr/local/bin/fastq-qual", "fastq-qualadj": "/usr/local/bin/fastq-qualadj", "fastq-sample": "/usr/local/bin/fastq-sample", "fastq-sort": "/usr/local/bin/fastq-sort", "fastq-uniq": "/usr/local/bin/fastq-uniq", "safemix": "/usr/local/bin/safemix", "safemut": "/usr/local/bin/safemut", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/safesim.
singularity registry hpc automated addition for safesim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/safesim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/safesim:0.1.6.8d44580--h7d57edc_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/safesim/0.1.6.8d44580--h7d57edc_4
$ module help quay.io/biocontainers/safesim/0.1.6.8d44580--h7d57edc_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### safesim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### safesim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### safesim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### safesim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### safesim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### safesim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-grep

```bash
$ singularity exec <container> /usr/local/bin/fastq-grep
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-kmers

```bash
$ singularity exec <container> /usr/local/bin/fastq-kmers
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-kmers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-match

```bash
$ singularity exec <container> /usr/local/bin/fastq-match
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-qscale

```bash
$ singularity exec <container> /usr/local/bin/fastq-qscale
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-qscale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-qscale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-qual

```bash
$ singularity exec <container> /usr/local/bin/fastq-qual
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-qual   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-qual   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-qualadj

```bash
$ singularity exec <container> /usr/local/bin/fastq-qualadj
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-qualadj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-qualadj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-sample

```bash
$ singularity exec <container> /usr/local/bin/fastq-sample
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-sort

```bash
$ singularity exec <container> /usr/local/bin/fastq-sort
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-uniq

```bash
$ singularity exec <container> /usr/local/bin/fastq-uniq
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### safemix

```bash
$ singularity exec <container> /usr/local/bin/safemix
$ podman run --it --rm --entrypoint /usr/local/bin/safemix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/safemix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### safemut

```bash
$ singularity exec <container> /usr/local/bin/safemut
$ podman run --it --rm --entrypoint /usr/local/bin/safemut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/safemut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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