---
layout: container
name:  "quay.io/biocontainers/perl-bio-monophylizer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-monophylizer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-monophylizer/container.yaml"
updated_at: "2026-01-03 03:40:57.339096"
latest: "1.0.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-bio-monophylizer"
aliases:
 - "monophylizer.pl"
 - "imgsize"
 - "xml_grep"
 - "xml_merge"
 - "xml_pp"
 - "xml_spellcheck"
 - "xml_split"
 - "webtidy"
 - "tidyp"
 - "tpage"
 - "ttree"
 - "bdf2gdfont.pl"
 - "htmltree"
 - "lwp-download"
 - "lwp-dump"
 - "lwp-mirror"
 - "lwp-request"
 - "bdftogd"
 - "gd2copypal"
 - "gd2togif"
 - "gd2topng"
 - "gdcmpgif"
 - "gdparttopng"
 - "gdtopng"
 - "giftogd2"
 - "pngtogd"
versions:
 - "1.0.0--hdfd78af_0"
description: "singularity registry hpc automated addition for perl-bio-monophylizer"
config: {"url": "https://biocontainers.pro/tools/perl-bio-monophylizer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-bio-monophylizer", "latest": {"1.0.0--hdfd78af_0": "sha256:48bc185cd8c69ec021839aeb0fe5c89c35b0f53ec2946b8594ac97c3cc4c41e5"}, "tags": {"1.0.0--hdfd78af_0": "sha256:48bc185cd8c69ec021839aeb0fe5c89c35b0f53ec2946b8594ac97c3cc4c41e5"}, "docker": "quay.io/biocontainers/perl-bio-monophylizer", "aliases": {"monophylizer.pl": "/usr/local/bin/monophylizer.pl", "imgsize": "/usr/local/bin/imgsize", "xml_grep": "/usr/local/bin/xml_grep", "xml_merge": "/usr/local/bin/xml_merge", "xml_pp": "/usr/local/bin/xml_pp", "xml_spellcheck": "/usr/local/bin/xml_spellcheck", "xml_split": "/usr/local/bin/xml_split", "webtidy": "/usr/local/bin/webtidy", "tidyp": "/usr/local/bin/tidyp", "tpage": "/usr/local/bin/tpage", "ttree": "/usr/local/bin/ttree", "bdf2gdfont.pl": "/usr/local/bin/bdf2gdfont.pl", "htmltree": "/usr/local/bin/htmltree", "lwp-download": "/usr/local/bin/lwp-download", "lwp-dump": "/usr/local/bin/lwp-dump", "lwp-mirror": "/usr/local/bin/lwp-mirror", "lwp-request": "/usr/local/bin/lwp-request", "bdftogd": "/usr/local/bin/bdftogd", "gd2copypal": "/usr/local/bin/gd2copypal", "gd2togif": "/usr/local/bin/gd2togif", "gd2topng": "/usr/local/bin/gd2topng", "gdcmpgif": "/usr/local/bin/gdcmpgif", "gdparttopng": "/usr/local/bin/gdparttopng", "gdtopng": "/usr/local/bin/gdtopng", "giftogd2": "/usr/local/bin/giftogd2", "pngtogd": "/usr/local/bin/pngtogd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-monophylizer.
singularity registry hpc automated addition for perl-bio-monophylizer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-monophylizer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-monophylizer:1.0.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-monophylizer/1.0.0--hdfd78af_0
$ module help quay.io/biocontainers/perl-bio-monophylizer/1.0.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-monophylizer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-monophylizer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-monophylizer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-monophylizer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-monophylizer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-monophylizer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### monophylizer.pl

```bash
$ singularity exec <container> /usr/local/bin/monophylizer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/monophylizer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monophylizer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imgsize

```bash
$ singularity exec <container> /usr/local/bin/imgsize
$ podman run --it --rm --entrypoint /usr/local/bin/imgsize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imgsize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_grep

```bash
$ singularity exec <container> /usr/local/bin/xml_grep
$ podman run --it --rm --entrypoint /usr/local/bin/xml_grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_merge

```bash
$ singularity exec <container> /usr/local/bin/xml_merge
$ podman run --it --rm --entrypoint /usr/local/bin/xml_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_merge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_pp

```bash
$ singularity exec <container> /usr/local/bin/xml_pp
$ podman run --it --rm --entrypoint /usr/local/bin/xml_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_pp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_spellcheck

```bash
$ singularity exec <container> /usr/local/bin/xml_spellcheck
$ podman run --it --rm --entrypoint /usr/local/bin/xml_spellcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_spellcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xml_split

```bash
$ singularity exec <container> /usr/local/bin/xml_split
$ podman run --it --rm --entrypoint /usr/local/bin/xml_split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xml_split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### webtidy

```bash
$ singularity exec <container> /usr/local/bin/webtidy
$ podman run --it --rm --entrypoint /usr/local/bin/webtidy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/webtidy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tidyp

```bash
$ singularity exec <container> /usr/local/bin/tidyp
$ podman run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tidyp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tpage

```bash
$ singularity exec <container> /usr/local/bin/tpage
$ podman run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ttree

```bash
$ singularity exec <container> /usr/local/bin/ttree
$ podman run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ttree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdf2gdfont.pl

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htmltree

```bash
$ singularity exec <container> /usr/local/bin/htmltree
$ podman run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htmltree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-download

```bash
$ singularity exec <container> /usr/local/bin/lwp-download
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-dump

```bash
$ singularity exec <container> /usr/local/bin/lwp-dump
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-mirror

```bash
$ singularity exec <container> /usr/local/bin/lwp-mirror
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-mirror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-mirror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-request

```bash
$ singularity exec <container> /usr/local/bin/lwp-request
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-request   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-request   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2copypal

```bash
$ singularity exec <container> /usr/local/bin/gd2copypal
$ podman run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2togif

```bash
$ singularity exec <container> /usr/local/bin/gd2togif
$ podman run --it --rm --entrypoint /usr/local/bin/gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2topng

```bash
$ singularity exec <container> /usr/local/bin/gd2topng
$ podman run --it --rm --entrypoint /usr/local/bin/gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdcmpgif

```bash
$ singularity exec <container> /usr/local/bin/gdcmpgif
$ podman run --it --rm --entrypoint /usr/local/bin/gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdparttopng

```bash
$ singularity exec <container> /usr/local/bin/gdparttopng
$ podman run --it --rm --entrypoint /usr/local/bin/gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdtopng

```bash
$ singularity exec <container> /usr/local/bin/gdtopng
$ podman run --it --rm --entrypoint /usr/local/bin/gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftogd2

```bash
$ singularity exec <container> /usr/local/bin/giftogd2
$ podman run --it --rm --entrypoint /usr/local/bin/giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngtogd

```bash
$ singularity exec <container> /usr/local/bin/pngtogd
$ podman run --it --rm --entrypoint /usr/local/bin/pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
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