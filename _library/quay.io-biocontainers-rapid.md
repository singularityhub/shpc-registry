---
layout: container
name:  "quay.io/biocontainers/rapid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rapid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rapid/container.yaml"
updated_at: "2024-09-07 02:43:10.752564"
latest: "1.0--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/rapid"
aliases:
 - "compPlot.Rmd"
 - "homePage.Rmd"
 - "master.html"
 - "rapidDiff.r"
 - "rapidDiff.sh"
 - "rapidNorm.r"
 - "rapidNorm.sh"
 - "rapidStats.r"
 - "rapidStats.sh"
 - "rapidVis.r"
 - "rapidVis.sh"
 - "rapid_ParseSam.pl"
 - "rapid_ToFasta.pl"
 - "statsPlot.Rmd"
 - "perl5.32.0"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
versions:
 - "1.0--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for rapid"
config: {"url": "https://biocontainers.pro/tools/rapid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rapid", "latest": {"1.0--hdfd78af_2": "sha256:beac1bf0d12f670ce2eba134e2a1dd60eb8a078b145b617003118df368b86065"}, "tags": {"1.0--hdfd78af_2": "sha256:beac1bf0d12f670ce2eba134e2a1dd60eb8a078b145b617003118df368b86065"}, "docker": "quay.io/biocontainers/rapid", "aliases": {"compPlot.Rmd": "/usr/local/bin/compPlot.Rmd", "homePage.Rmd": "/usr/local/bin/homePage.Rmd", "master.html": "/usr/local/bin/master.html", "rapidDiff.r": "/usr/local/bin/rapidDiff.r", "rapidDiff.sh": "/usr/local/bin/rapidDiff.sh", "rapidNorm.r": "/usr/local/bin/rapidNorm.r", "rapidNorm.sh": "/usr/local/bin/rapidNorm.sh", "rapidStats.r": "/usr/local/bin/rapidStats.r", "rapidStats.sh": "/usr/local/bin/rapidStats.sh", "rapidVis.r": "/usr/local/bin/rapidVis.r", "rapidVis.sh": "/usr/local/bin/rapidVis.sh", "rapid_ParseSam.pl": "/usr/local/bin/rapid_ParseSam.pl", "rapid_ToFasta.pl": "/usr/local/bin/rapid_ToFasta.pl", "statsPlot.Rmd": "/usr/local/bin/statsPlot.Rmd", "perl5.32.0": "/usr/local/bin/perl5.32.0", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/usr/local/bin/bowtie2-inspect-s"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rapid.
shpc-registry automated BioContainers addition for rapid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rapid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rapid:1.0--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rapid/1.0--hdfd78af_2
$ module help quay.io/biocontainers/rapid/1.0--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rapid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rapid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rapid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rapid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rapid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rapid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compPlot.Rmd

```bash
$ singularity exec <container> /usr/local/bin/compPlot.Rmd
$ podman run --it --rm --entrypoint /usr/local/bin/compPlot.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compPlot.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### homePage.Rmd

```bash
$ singularity exec <container> /usr/local/bin/homePage.Rmd
$ podman run --it --rm --entrypoint /usr/local/bin/homePage.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/homePage.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### master.html

```bash
$ singularity exec <container> /usr/local/bin/master.html
$ podman run --it --rm --entrypoint /usr/local/bin/master.html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/master.html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidDiff.r

```bash
$ singularity exec <container> /usr/local/bin/rapidDiff.r
$ podman run --it --rm --entrypoint /usr/local/bin/rapidDiff.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidDiff.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidDiff.sh

```bash
$ singularity exec <container> /usr/local/bin/rapidDiff.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rapidDiff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidDiff.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidNorm.r

```bash
$ singularity exec <container> /usr/local/bin/rapidNorm.r
$ podman run --it --rm --entrypoint /usr/local/bin/rapidNorm.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidNorm.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidNorm.sh

```bash
$ singularity exec <container> /usr/local/bin/rapidNorm.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rapidNorm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidNorm.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidStats.r

```bash
$ singularity exec <container> /usr/local/bin/rapidStats.r
$ podman run --it --rm --entrypoint /usr/local/bin/rapidStats.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidStats.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidStats.sh

```bash
$ singularity exec <container> /usr/local/bin/rapidStats.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rapidStats.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidStats.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidVis.r

```bash
$ singularity exec <container> /usr/local/bin/rapidVis.r
$ podman run --it --rm --entrypoint /usr/local/bin/rapidVis.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidVis.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapidVis.sh

```bash
$ singularity exec <container> /usr/local/bin/rapidVis.sh
$ podman run --it --rm --entrypoint /usr/local/bin/rapidVis.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapidVis.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapid_ParseSam.pl

```bash
$ singularity exec <container> /usr/local/bin/rapid_ParseSam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rapid_ParseSam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapid_ParseSam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rapid_ToFasta.pl

```bash
$ singularity exec <container> /usr/local/bin/rapid_ToFasta.pl
$ podman run --it --rm --entrypoint /usr/local/bin/rapid_ToFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapid_ToFasta.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### statsPlot.Rmd

```bash
$ singularity exec <container> /usr/local/bin/statsPlot.Rmd
$ podman run --it --rm --entrypoint /usr/local/bin/statsPlot.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/statsPlot.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
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