---
layout: container
name:  "quay.io/biocontainers/lap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lap/container.yaml"
updated_at: "2023-01-27 02:49:10.812170"
latest: "1.1.r186--py27_0"
container_url: "https://biocontainers.pro/tools/lap"
aliases:
 - "SeqIO.py"
 - "calc_prob.py"
 - "gen_rand_samp.py"
 - "mean"
 - "mprobability"
 - "probability"
 - "stitch"
 - "sum_prob.py"
 - "sample"
 - "easy_install-2.7"
 - "perl5.22.0"
 - "c2ph"
 - "pstruct"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
versions:
 - "1.1.r186--py27_0"
description: "shpc-registry automated BioContainers addition for lap"
config: {"url": "https://biocontainers.pro/tools/lap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lap", "latest": {"1.1.r186--py27_0": "sha256:aee327206a3bc0aece939a7d063ee1b6c423561648706900855518a52b183536"}, "tags": {"1.1.r186--py27_0": "sha256:aee327206a3bc0aece939a7d063ee1b6c423561648706900855518a52b183536"}, "docker": "quay.io/biocontainers/lap", "aliases": {"SeqIO.py": "/usr/local/bin/SeqIO.py", "calc_prob.py": "/usr/local/bin/calc_prob.py", "gen_rand_samp.py": "/usr/local/bin/gen_rand_samp.py", "mean": "/usr/local/bin/mean", "mprobability": "/usr/local/bin/mprobability", "probability": "/usr/local/bin/probability", "stitch": "/usr/local/bin/stitch", "sum_prob.py": "/usr/local/bin/sum_prob.py", "sample": "/usr/local/bin/sample", "easy_install-2.7": "/usr/local/bin/easy_install-2.7", "perl5.22.0": "/usr/local/bin/perl5.22.0", "c2ph": "/usr/local/bin/c2ph", "pstruct": "/usr/local/bin/pstruct", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lap.
shpc-registry automated BioContainers addition for lap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lap:1.1.r186--py27_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lap/1.1.r186--py27_0
$ module help quay.io/biocontainers/lap/1.1.r186--py27_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SeqIO.py

```bash
$ singularity exec <container> /usr/local/bin/SeqIO.py
$ podman run --it --rm --entrypoint /usr/local/bin/SeqIO.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SeqIO.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calc_prob.py

```bash
$ singularity exec <container> /usr/local/bin/calc_prob.py
$ podman run --it --rm --entrypoint /usr/local/bin/calc_prob.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calc_prob.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gen_rand_samp.py

```bash
$ singularity exec <container> /usr/local/bin/gen_rand_samp.py
$ podman run --it --rm --entrypoint /usr/local/bin/gen_rand_samp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gen_rand_samp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mean

```bash
$ singularity exec <container> /usr/local/bin/mean
$ podman run --it --rm --entrypoint /usr/local/bin/mean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mprobability

```bash
$ singularity exec <container> /usr/local/bin/mprobability
$ podman run --it --rm --entrypoint /usr/local/bin/mprobability   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mprobability   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### probability

```bash
$ singularity exec <container> /usr/local/bin/probability
$ podman run --it --rm --entrypoint /usr/local/bin/probability   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probability   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### stitch

```bash
$ singularity exec <container> /usr/local/bin/stitch
$ podman run --it --rm --entrypoint /usr/local/bin/stitch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/stitch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sum_prob.py

```bash
$ singularity exec <container> /usr/local/bin/sum_prob.py
$ podman run --it --rm --entrypoint /usr/local/bin/sum_prob.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sum_prob.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample

```bash
$ singularity exec <container> /usr/local/bin/sample
$ podman run --it --rm --entrypoint /usr/local/bin/sample   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-2.7

```bash
$ singularity exec <container> /usr/local/bin/easy_install-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.22.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.22.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.22.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c2ph

```bash
$ singularity exec <container> /usr/local/bin/c2ph
$ podman run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c2ph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pstruct

```bash
$ singularity exec <container> /usr/local/bin/pstruct
$ podman run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
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