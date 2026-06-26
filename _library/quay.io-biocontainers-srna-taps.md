---
layout: container
name:  "quay.io/biocontainers/srna-taps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/srna-taps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/srna-taps/container.yaml"
updated_at: "2026-06-26 06:39:19.904600"
latest: "0.2.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/srna-taps"
aliases:
 - "fc-genconf"
 - "idna"
 - "srnataps"
 - "trim_galore"
 - "gff2gff"
 - "roh-viz"
 - "vrfs-variances"
 - "phc"
 - "jnativescan"
 - "kaleido"
 - "mathjax-path"
 - "multiqc"
 - "dotenv"
 - "eido"
 - "plotly_get_chrome"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
 - "fastqc"
 - "rich-click"
 - "typer"
 - "hb-raster"
versions:
 - "0.2.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for srna-taps"
config: {"url": "https://biocontainers.pro/tools/srna-taps", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for srna-taps", "latest": {"0.2.2--pyhdfd78af_0": "sha256:3c0ab84290c4647f3dc6fc3a244d8a688ffcf858bcc641d913f13fcf1ecb79ea"}, "tags": {"0.2.2--pyhdfd78af_0": "sha256:3c0ab84290c4647f3dc6fc3a244d8a688ffcf858bcc641d913f13fcf1ecb79ea"}, "docker": "quay.io/biocontainers/srna-taps", "aliases": {"fc-genconf": "/usr/local/bin/fc-genconf", "idna": "/usr/local/bin/idna", "srnataps": "/usr/local/bin/srnataps", "trim_galore": "/usr/local/bin/trim_galore", "gff2gff": "/usr/local/bin/gff2gff", "roh-viz": "/usr/local/bin/roh-viz", "vrfs-variances": "/usr/local/bin/vrfs-variances", "phc": "/usr/local/bin/phc", "jnativescan": "/usr/local/bin/jnativescan", "kaleido": "/usr/local/bin/kaleido", "mathjax-path": "/usr/local/bin/mathjax-path", "multiqc": "/usr/local/bin/multiqc", "dotenv": "/usr/local/bin/dotenv", "eido": "/usr/local/bin/eido", "plotly_get_chrome": "/usr/local/bin/plotly_get_chrome", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "fastqc": "/usr/local/bin/fastqc", "rich-click": "/usr/local/bin/rich-click", "typer": "/usr/local/bin/typer", "hb-raster": "/usr/local/bin/hb-raster"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/srna-taps.
singularity registry hpc automated addition for srna-taps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/srna-taps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/srna-taps:0.2.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/srna-taps/0.2.2--pyhdfd78af_0
$ module help quay.io/biocontainers/srna-taps/0.2.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### srna-taps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### srna-taps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### srna-taps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### srna-taps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### srna-taps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### srna-taps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fc-genconf

```bash
$ singularity exec <container> /usr/local/bin/fc-genconf
$ podman run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fc-genconf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### srnataps

```bash
$ singularity exec <container> /usr/local/bin/srnataps
$ podman run --it --rm --entrypoint /usr/local/bin/srnataps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srnataps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_galore

```bash
$ singularity exec <container> /usr/local/bin/trim_galore
$ podman run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_galore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff

```bash
$ singularity exec <container> /usr/local/bin/gff2gff
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roh-viz

```bash
$ singularity exec <container> /usr/local/bin/roh-viz
$ podman run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vrfs-variances

```bash
$ singularity exec <container> /usr/local/bin/vrfs-variances
$ podman run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phc

```bash
$ singularity exec <container> /usr/local/bin/phc
$ podman run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jnativescan

```bash
$ singularity exec <container> /usr/local/bin/jnativescan
$ podman run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jnativescan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kaleido

```bash
$ singularity exec <container> /usr/local/bin/kaleido
$ podman run --it --rm --entrypoint /usr/local/bin/kaleido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kaleido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mathjax-path

```bash
$ singularity exec <container> /usr/local/bin/mathjax-path
$ podman run --it --rm --entrypoint /usr/local/bin/mathjax-path   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mathjax-path   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eido

```bash
$ singularity exec <container> /usr/local/bin/eido
$ podman run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plotly_get_chrome

```bash
$ singularity exec <container> /usr/local/bin/plotly_get_chrome
$ podman run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plotly_get_chrome   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hb-raster

```bash
$ singularity exec <container> /usr/local/bin/hb-raster
$ podman run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-raster   -v ${PWD} -w ${PWD} <container> -c " $@"
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